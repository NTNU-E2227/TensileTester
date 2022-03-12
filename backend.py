import serial
import serial.tools.list_ports
import mcu_com
import time
import math

ports = [comport.name for comport in serial.tools.list_ports.comports()]

print(ports)

try:
    port = serial.Serial("COM8", baudrate=115200)
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
        t = time.time()
        yield [t, math.sin(0.1*t)]
        time.sleep(1)