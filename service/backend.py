import decimal
import math
import serial
import serial.tools.list_ports
import time
import json
import numpy as np
from decimal import Decimal
class com_obj:
    def __init__(self):
        self.port = None
        self.portList = []
        self.direction = b"l"
        self.linear = True
        self.youngs = 0
        self.running = False
        self.timer_run = False
        self.speed = 0
        self.datalist = [[],[],[],[],[]]
        self.length_zero = 0
        self.time_zero = time.time()
        self.latest_data = [0,0,0,0,0]

        with open('config.txt') as f:
            data = f.read()
            self.conf = json.loads(data)

    def update_ports(self):
        port_name_list = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if port.serial_number == self.conf["id"]:
                self.set_port("/dev/ttyACM0")
            port_name_list.append(port.name)
        if port_name_list == self.portList:
            return False
        self.portList = port_name_list
        return True

    def motor_stop(self):
        self.port.write(b's\n')
        self.running = False

    def motor_run(self):
        payload = bytearray(self.direction)
        spd = hex(self.speed)[2:]
        while len(spd) < 4: spd = "0" + spd
        payload.extend(spd.encode())
        payload.extend(b'\n')
        self.port.write(payload)
        self.running = True
        if not self.timer_run:
            self.reset_data()
            self.set_time_zero()
            self.timer_run = True

    def motor_run_percent(self, speed_percent):
        PWM_MAX = 0x7530
        self.speed = int(PWM_MAX * (0.8*speed_percent + 10) / 100)
        self.motor_run()

    def adc_reset(self):
        self.port.write(b'r\n')

    def adc_read(self):
        in_data = self.port.readline()
        length = int(in_data[0:6],16)
        force = int(in_data[6:12],16)
        return [length, force]

    def set_direction(self, dir):
        self.direction = dir
        if self.running:
            self.motor_run()

    def set_speed(self, spd):
        self.speed = spd
        if self.running:
            self.motor_run_percent(self.speed)

    def set_port(self, port_name):
        if self.port != None:
            self.port.close()
        self.port = serial.Serial(port_name, baudrate=115200)
        self.adc_reset()
        self.adc_read()

    def generator(self):
        while True:
            if self.port == None:
                yield False
                time.sleep(1)
                continue
            try:
                data = self.adc_read()
            except serial.serialutil.SerialException:
                yield False
                continue
            length = self.length_from_raw(data[0])
            force = self.force_from_raw(data[1])
            try:
                offset = 1000
                if not (self.datalist[1][-1]-offset < length < self.datalist[1][-1]+offset): continue
                if not (self.datalist[2][-1]-offset< force < self.datalist[2][-1]+offset): continue
            except: pass
            self.latest_data = [self.time(),length,force,self.time(),self.stress(force)]
            self.datalist[0].append(self.latest_data[0])
            self.datalist[1].append(self.latest_data[1])
            self.datalist[2].append(self.latest_data[2])
            self.datalist[3].append(self.latest_data[3])
            self.datalist[4].append(self.latest_data[4])
            yield True

    def time(self):
        if self.timer_run:
            return time.time() - self.time_zero
        return 0

    def reset_data(self):
        self.datalist = [[],[],[],[],[]]

    def set_length_zero(self):
        self.length_zero = self.datalist[1][-1] + self.length_zero 

    def set_time_zero(self):
        self.time_zero = time.time()
        if not self.running:
            self.timer_run = False

    def length_from_raw(self, length_raw):
        length = 0
        for a in range(0, 5):
            length += self.conf["a" + str(a)] * (length_raw ** a)
        return length - self.length_zero

    def force_from_raw(self, force_raw):
        force = 0
        for b in range(0, 5):
            force += self.conf["b" + str(b)] * (force_raw ** b)
        return force

    def stress(self, force):
        A0 = self.conf["E0"] * self.conf["H0"]
        stress = force/A0 #in MPa
        return stress

    def strain(self, force, distance):  # Går ut ifra at metallene strekker seg lineært med påført kraft når elastiske.
        if self.conf["L1"] - self.conf["L0"] > 0 and self.speed != 0 :  # Sjekker om utregninger er nødvendige
            R0 = (self.conf["H1"] - self.conf["H0"]) / 2
            R0_L = 0
            for i in range(89):
                R0_L += R0 * (math.cos(math.radians(271 + i)) - math.cos(math.radians(270 + i))) * (
                        self.conf["H0"] / (self.conf["H0"] + 2 * R0 * (1 + math.sin(math.radians(270.5 + i)))))
            linear_gauge_distance = distance * (self.conf["L0"] - 2 * R0) / ((self.conf["H0"] / self.conf["H1"]) * ( #Lengde i mikrometer
                    self.conf["L1"] - self.conf["L0"]) + (self.conf["L0"] - 2 * R0) + 2 * R0_L)
            # distance er strukket lengde dvs. forskjellen på prøvens lengde før og under spenning(ikke elektrisk men fysisk).

            def check_linear(Force_list, Length_list):
                if len(Force_list)<50:
                    print("linear")
                    return True
                elif Force_list[-50] < 0:
                    print("linear")
                    return True
                print("Force:", Force_list[-1], Force_list[-11], Force_list[-21], Force_list[-5], Force_list[-15])
                print("Length:", Length_list[-1],Length_list[-11],Length_list[-21],Length_list[-5],Length_list[-15])
                try:
                    if (Decimal(Force_list[-1] - Force_list[-11]) / Decimal(Length_list[-1] - Length_list[-11])) / (
                            Decimal(Force_list[-11] - Force_list[-21]) / Decimal(Length_list[-11] - Length_list[-21])) < 0.5:
                        if (Decimal(Force_list[-5] - Force_list[-15]) / Decimal(Length_list[-5] - Length_list[-15])) /(
                                Decimal(Force_list[-15] - Force_list[-25]) / Decimal(Length_list[-15] - Length_list[-25])) < 0.5:
                            return False
                        else:
                            return True
                    else:
                        return True
                except:
                    return True

            if check_linear(self.datalist[2], self.datalist[1]) == False:
                print("\n NONLINEAR\n")
                if self.linear == True:
                    n_max = self.datalist[4][-1]
                    n_min = self.datalist[4][1]
                    for i in range((len(self.datalist[4]))):
                        if self.datalist[4][i] > self.datalist[4][n_max]:
                            n_max = i
                        if self.datalist[4][i] < self.datalist[4][n_min]:
                            n_min = i
                    y_min = self.datalist[4][n_min] + ((self.datalist[4][n_max]-self.datalist[4][n_min])/3)
                    y_max = self.datalist[4][n_min] + 2 * ((self.datalist[4][n_max]-self.datalist[4][n_min])/3)
                    y_min_n = 0
                    y_max_n = 0
                    for i in range((len(self.datalist[4]))):
                        if self.datalist[4][i] > y_min:
                            y_min_n = i
                    for i in range((len(self.datalist[4]))-y_min_n):
                        if self.datalist[4][i+y_min_n] > y_max:
                            y_max_n = i
                    self.youngs = (self.datalist[4][y_max_n]-self.datalist[4][y_min_n])/(self.datalist[3][y_max_n]-self.datalist[3][y_min_n])
                self.linear = False

            if self.linear:  # Når Metallet er elastisk
                print("linear")
                return (linear_gauge_distance/1000) / (self.conf["L0"] - 2 * R0)
            else:  # Når metallet ikke lenger er i elastisk området
                print("nonlinear")
                non_gauge_length = 1 - linear_gauge_distance/distance
                non_gauge_distance = (non_gauge_length/(1-non_gauge_length))((self.conf["L0"] - 2 * R0)*(force/(self.conf["E0"]*self.conf["H0"])))
                return distance-non_gauge_distance
        else:
            return (distance/1000) / self.conf["L0"]

    def export(self, loc):
        data = zip(*self.datalist)
        data = list(data)
        sep = [map(str,l) for l in data]
        nl = [(';'.join(s)) for s in sep]
        param = { key: self.conf[key] for key in ["L0","L1","H0","H1","E0"] }
        param = param.items()
        sep2 = [map(str,l1) for l1 in param]
        nl2 = [(';'.join(s2)) for s2 in sep2]
        tabell = ["Time; Length; Force; Strain; Stress;\ns;um;N;None;MPa"]
        header = '"Reference;ISO 6892"\n"Specimen geometry;flat"\n"Specimen thickness = E0"\n"Specimen width = H0\n"Data acquisition rate 8Hz"\n"File length N data rows"\n"File width 5 data columns"'
        np.savetxt(loc,np.r_[nl2,tabell,nl],header = header,delimiter =";",fmt ='% 4s',comments = "")