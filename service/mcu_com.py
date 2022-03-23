PWM_MAX = 0x7530

def motor_stop(serial_port):
    serial_port.write(b's\n')
    

def motor_load(serial_port, speed):
    payload = bytearray(b'l')
    payload.extend(speed.to_bytes(2,'big'))
    payload.extend(b'\n')
    serial_port.write(payload)

def motor_unload(serial_port, speed):
    payload = bytearray(b'u')
    payload.extend(speed.to_bytes(2,'big'))
    payload.extend(b'\n')
    serial_port.write(payload)

def adc_read(serial_port):
    in_data = serial_port.readline()
    lenght = int.from_bytes(in_data[0:3],'big')
    force = int.from_bytes(in_data[3:6],'big')
    return [lenght, force]

def motor_load_percent(serial_port, speed_percent):
    speed = int(PWM_MAX * (0.8*speed_percent + 10) / 100)
    motor_load(serial_port, speed)

def motor_unload_percent(serial_port, speed_percent):
    speed = int(PWM_MAX * (0.8*speed_percent + 10) / 100)
    motor_unload(serial_port, speed)

def adc_reset(serial_port):
    serial_port.write(b'r\n')


    