import serial

import mcu_com

import time

import math

try:
    port = serial.Serial("COM8", baudrate=115200)
except:
    pass

def run_motor(dir, speed):
    if dir == "l":
        mcu_com.motor_load_percent(port, speed)
    elif dir == "u":
        mcu_com.motor_unload_percent(port, speed)

def stop_motor():
    mcu_com.motor_stop(port)

def plot_generator():
    while True:
        yield math.sin(0.1*time.time())
        time.sleep(1)