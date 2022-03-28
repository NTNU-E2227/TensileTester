import serial
import serial.tools.list_ports
import service.mcu_com as mcu_com
import time
import service.config as config

def stress(force):
    A0 = config.E0 * config.H0
    stress = force/A0
    return stress

def strain(force, distance): #Går ut ifra at metallene strekker seg lineært med påført kraft når elastiske.
    R1 = 4 # not quite sure if this one is correct, might have to put in one more input parameter

    R0 = config.H1 - config.H0 - R1
    strain = gauge_distance/config.L0
    return strain

class com_obj:
    def __init__(self):
        self.port = None
        self.direction = b"l"
        self.running = False
        self.speed = 0
        self.datalist = [[],[],[],[],[]]

    def motor_stop(self):
        self.port.write(b's\n')
        self.running = False

    def motor_run(self):
        payload = bytearray(self.direction)
        payload.extend(self.speed.to_bytes(2,'big'))
        payload.extend(b'\n')
        self.port.write(payload)
        self.running = True

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
            while self.port == None:
                pass
            data = self.adc_read()
            t = time.time()
            self.datalist[0].append(t)
            self.datalist[1].append(t)
            self.datalist[2].append(data[0])
            self.datalist[3].append(t)
            self.datalist[4].append(data[1])
            yield True

    def reset_data(self):
        self.datalist = [[],[],[],[],[]]