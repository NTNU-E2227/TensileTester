import serial
import mcu_com
import time
import math

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
        data = mcu_com.adc_read(port)
        t = time.time()
        yield [t, math.sin(0.1*t)] # [t, data[0]]  
        time.sleep(1)

        