import decimal
import math
import serial
import serial.tools.list_ports
import time
import json
import numpy as np

class com_obj:
    def __init__(self):
        self.port = None
        self.portList = []
        self.direction = b"l"
        self.running = False
        self.timer_run = False
        self.speed = 0
        self.datalist = [[],[],[],[],[]]
        self.length_zero = 0
        self.time_zero = time.time()
        self.latest_data = [0,0,0,0,0]
        self.sRange = "1"
        self.datalog = False

        with open('config.txt') as f:
            data = f.read()
            self.conf = json.loads(data)

    def update_ports(self):
        port_name_list = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if port.serial_number == self.conf["id"]:
                self.set_port(port.device)
            port_name_list.append(port.device)
        if port_name_list == self.portList:
            return False
        self.portList = port_name_list
        return True

    def motor_stop(self):
        self.port.write(b's\n')
        self.running = False

    def motor_run(self):
        PWM_MAX = 0x6978
        PWM_MIN = 0x0BB8
        SPEED_MAX = 30.0
        SPEED_MIN = 0.0
        spd = int((self.speed - SPEED_MIN) * (PWM_MAX - PWM_MIN) / (SPEED_MAX - SPEED_MIN) + PWM_MIN)
        spd = hex(spd)[2:]
        while len(spd) < 4: spd = "0" + spd
        payload = bytearray(self.direction)
        payload.extend(spd.encode())
        payload.extend(b'\n')
        self.port.write(payload)
        self.running = True
        if not self.timer_run:
            self.reset_data()
            self.set_time_zero()
            self.timer_run = True

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
            self.motor_run()

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
            self.latest_data = [self.time(),length,force,self.strain(length),self.stress(force)]
            if self.datalog:
                self.datalist[0].append(self.latest_data[0])
                self.datalist[1].append(self.latest_data[1])
                self.datalist[2].append(self.latest_data[2])
                self.datalist[3].append(self.latest_data[3])
                self.datalist[4].append(self.latest_data[4])
            yield True

    def time(self):
        if self.timer_run:
            return round(time.time() - self.time_zero, 2)
        return 0

    def reset_data(self):
        self.datalist = [[],[],[],[],[]]

    def set_length_zero(self):
        self.length_zero = self.latest_data[1] + self.length_zero 
        self.reset_data()

    def set_time_zero(self):
        self.time_zero = time.time()
        if not self.datalog:
            self.timer_run = False

    def length_from_raw(self, length_raw):
        length = 0
        for a in range(0, 5):
            length += self.conf["D" + str(a)] * (length_raw ** a)
        return round(length - self.length_zero, 2)

    def force_from_raw(self, force_raw):
        force = 0
        for b in range(0, 5):
            force += self.conf["S" + self.sRange + str(b)] * (force_raw ** b)
        return round(force, 2)

    def trueStressStrain(self,force,length):
        A0 = self.conf["E0"] * self.conf["H0"]
        estress = force/A0
        estrain = length/(self.conf["L0"]*1e3)
        tstress = estress*(1+estrain)
        tstrain = math.log(1+estrain)
        return tstress, tstrain

    def stress(self, force):
        A0 = self.conf["E0"] * self.conf["H0"]
        stress = force/A0 #in MPa
        return round(stress, 2)

    def strain(self, dist):
        return round(dist / (self.conf["L0"] * 1e3), 4)

    def export(self, loc):
        data = zip(*self.datalist)
        data = list(data)
        sep = [map(str,l) for l in data]
        nl = [(';'.join(s)) for s in sep]
        self.conf["DR"] = len(self.datalist[0])
        param = { key: self.conf[key] for key in ["L0","L1","H0","H1","E0","DR"] }
        param = param.items()
        sep2 = [map(str,l1) for l1 in param]
        nl2 = [(';'.join(s2)) for s2 in sep2]
        tabell = ["Time; Length; Force; Strain; Stress;\ns;um;N;None;MPa"]
        header = '"Reference;ISO 6892"\n"Specimen geometry;flat"\n"Specimen thickness = E0"\n"Specimen width = H0\n"File length N data rows"\n"File width 5 data columns"'
        np.savetxt(loc,np.r_[nl2,tabell,nl],header = header,delimiter =";",fmt ='% 4s',comments = "")