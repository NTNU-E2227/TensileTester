import serial
import serial.tools.list_ports
import service.mcu_com as mcu_com
import time
import service.config as config
import math

try:
    port = serial.Serial(config.COM, baudrate=115200)
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
        data = mcu_com.adc_read(port)
        t = time.time()
        if data[0] < 0x100000: continue
        if data[1] < 0x900000: continue
        yield [t, t, data[0], t, data[1]] 

def port_ready():
    coms = []
    ports = serial.tools.list_ports.comports()
    for port in sorted(ports):
        p = format(port[0])
        coms.append(p)
    return coms

def reset():
    mcu_com.adc_reset(port)

def stress(force):
    A0 = config.E0 * config.H0
    stress = force/A0
    return stress

def strain(force, distance): #Går ut ifra at metallene strekker seg lineært med påført kraft når elastiske.
    R1 = 4 # not quite sure if this one is correct, might have to put in one more input parameter

    R0 = config.H1 - config.H0 - R1
    strain = gauge_distance/config.L0
    return strain