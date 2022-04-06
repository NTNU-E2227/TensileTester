import math
import serial
import serial.tools.list_ports
import time
import json
import numpy as np

class com_obj:
    def __init__(self):
        self.port = None
        self.direction = b"l"
        self.running = False
        self.timer_run = False
        self.speed = 0
        self.datalist = [[],[],[],[],[]]
        self.lengt_zero = 0
        self.time_zero = time.time()

        with open('config.txt') as f:
            data = f.read()
            self.conf = json.loads(data)
            ports = serial.tools.list_ports.comports()
            for port in ports:
                if port.serial_number == self.conf["id"]:
                    self.set_port(port.name)

    def motor_stop(self):
        self.port.write(b's\n')
        self.running = False

    def motor_run(self):
        payload = bytearray(self.direction)
        payload.extend(self.speed.to_bytes(2,'big'))
        payload.extend(b'\n')
        self.port.write(payload)
        self.running = True
        self.timer_run = True

    def motor_run_percent(self, speed_percent):
        PWM_MAX = 0x7530
        self.speed = int(PWM_MAX * (0.8*speed_percent + 10) / 100)
        self.motor_run()

    def adc_reset(self):
        self.port.write(b'r\n')

    def adc_read(self):
        in_data = self.port.readline()
        length = int.from_bytes(in_data[0:3],'big')
        force = int.from_bytes(in_data[3:6],'big')
        return [length, force]

    def set_direction(self, dir):
        self.direction = dir
        if self.running: 
            self.motor_run()

    def set_speed(self, spd):
        self.speed = spd
        if self.running:
            self.motor_run()

    def set_port(self, port_name):
        if self.port != None:
            self.port.close()
        self.port = serial.Serial(port_name, baudrate=115200)
    
    def generator(self):
        while True:
            if self.port == None:
                continue
            data = self.adc_read()
            if data[1] < 0xE000: continue
            length = self.length_from_raw(data[1])
            force = self.force_from_raw(data[1])
            self.datalist[0].append(self.time())
            self.datalist[1].append(self.time())
            self.datalist[2].append(data[0])
            self.datalist[3].append(self.time())
            self.datalist[4].append(length*100)
            yield True

    def time(self):
        if self.timer_run:
            return time.time() - self.time_zero 
        return 0

    def reset_data(self):
        self.datalist = [[],[],[],[],[]]

    def set_length_zero(self):
        self.lengt_zero = self.datalist[2][-1]

    def set_time_zero(self):
        self.time_zero = time.time()
        if not self.running:
            self.timer_run = False

    def length_from_raw(self, length_raw):
        length = 0
        for a in range(0, 5):
            length += self.conf["a" + str(a)] * (length_raw ** a)
        return length - self.lengt_zero

    def force_from_raw(self, force_raw):
        force = 0
        for a in range(0, 5):
            force += self.conf["a" + str(a)] * (force_raw ** a)
        return force

    def stress(self, force):
        A0 = self.conf["E0"] * self.conf["H0"]
        stress = force/A0
        return stress

    def strain(self, force, distance):  # Går ut ifra at metallene strekker seg lineært med påført kraft når elastiske.
        if self.conf["L1"] - self.conf["L0"] > 0:  # Sjekker om utregninger er nødvendige
            R0 = (self.conf["H1"] - self.conf["H0"]) / 2
            R0_L = 0
            for i in range(89):
                R0_L += R0 * (math.cos(math.radians(271 + i)) - math.cos(math.radians(270 + i))) * (
                        self.conf["H0"] / (self.conf["H0"] + 2 * (R0 * (1 + math.sin(math.radians(270.5 + i))))))
            linear_gauge_distance = distance * (self.conf["L0"] - R0) / ((self.conf["H0"] / self.conf["H1"]) * (
                    self.conf["L1"] - self.conf["L0"]) + (self.conf["L0"] - R0) + 2 * R0_L)
            # distance er strukket lengde dvs. forskjellen på prøvens lengde før og under spenning(ikke elektrisk men fysisk).

            def not_linear(Force_list, Length_list):
                if ((Force_list[-1] - Force_list[-11]) / (Length_list[-1] - Length_list[-11])) / (
                        (Force_list[-11] - Force_list[-21]) / (Length_list[-11] - Length_list[-21])) < 0.8:
                    if ((Force_list[-5] - Force_list[-15]) / (Length_list[-5] - Length_list[-15])) / (
                            (Force_list[-15] - Force_list[-25]) / (Length_list[-15] - Length_list[-25])) < 0.8:
                        return False
                    else:
                        return True
                else:
                    return True

            if len(self.datalist[1]) < 50:
                return linear_gauge_distance / (self.conf["L0"] - R0)
            elif not_linear(self.datalist[2], self.datalist[1]):  # Når metallet ikke lenger er i elastisk området
                distance_w_out_gauge = None

                def find_strain(A, Stresslist, Strainlist):
                    prev_n = 0
                    for n in range(len(Stresslist)):
                        if Stresslist[n] >= force / A:
                            if Stresslist[n] == force / A:
                                return Strainlist[n]
                            else:
                                a = (Strainlist[n] - Strainlist[prev_n]) / (Stresslist[n] - Stresslist[prev_n])
                                b = Strainlist[n] - a * Stresslist[n]
                                return a * force / A + b
                        prev_n = n

                for i in range(89):
                    A = 2 * (R0 * (1 + math.sin(math.radians(271 + i)))) * self.conf["E0"]
                    distance_w_out_gauge += 2 * find_strain(A, self.datalist[3], self.datalist[4]) * R0 * (
                            math.cos(math.radians(271 + i)) - math.cos(math.radians(270 + i)))
                A = self.conf["E0"] * self.conf["H1"]
                distance_w_out_gauge += (A, self.datalist[3], self.datalist[4]) * (self.conf["L1"] - self.conf["L0"])
                gauge = distance - distance_w_out_gauge
                return gauge / (self.conf["L0"] - R0)
            else:  # Når Metallet er elastisk
                return linear_gauge_distance / (self.conf["L0"] - R0)
        else:
            return distance / self.conf["L0"]

    def export(self, loc):
        data = zip(*self.datalist)
        data = list(data)
        sep = [map(str,l) for l in data]
        nl = [(';'.join(s)) for s in sep]
        param = { key: self.conf[key] for key in ["L0","L1","H0","H1","E0"] }
        param = param.items()
        sep2 = [map(str,l1) for l1 in param]
        nl2 = [(';'.join(s2)) for s2 in sep2]
        tabell = ["Time; Force; Length; Stress; Strain;"]
        header = '"Reference;ISO 6892"\n"Identification;TENSTAND"\n"Specimen geometry;flat"\n"Specimen thickness = ao"\n"Specimen width = bo"\n"Data acquisition rate 10Hz"\n"File length N data rows"\n"File with 5 data columns"'
        np.savetxt(loc,np.r_[nl2,tabell,nl],header = header,delimiter =";",fmt ='% 4s',comments = "")