import serial
import serial.tools.list_ports
import mcu_com
import time
import math

ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))

try:
    port = serial.Serial("COM9", baudrate=115200)
except:
    port = None

def run_motor(dir, speed):
    if dir == "l":
        mcu_com.motor_load_percent(port, speed)
    elif dir == "u":
        mcu_com.motor_unload_percent(port, speed)

def stop_motor():
    mcu_com.motor_stop(port)


def stressPlot_generator(): #Generator for stress graf, yield [x,y] koordinater
    while True:
        #data = mcu_com.adc_read(port)
        t = time.time()
        yield [t, math.sin(0.1*t)] # [t, data[0]]  
        time.sleep(1)

def port_ready():
    coms = []
    ports = serial.tools.list_ports.comports()
    for port in sorted(ports):
        p = format(port[0])
        coms.append(p)
    return coms