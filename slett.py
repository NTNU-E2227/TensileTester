
import serial.tools.list_ports

def port_ready():
    coms = []
    ports = serial.tools.list_ports.comports()
    for port in sorted(ports):
        p = format(port[0])
        coms.append(p)
    return coms


    
