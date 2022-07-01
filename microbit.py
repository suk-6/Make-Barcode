import serial.tools.list_ports

# Microbit connect
ports = serial.tools.list_ports.comports()
com = ''
for port, desc, hwid in sorted(ports):
    if 'USB' in desc:
        com = port
if com != '':
    print('Micro:bit detected: ', com)
    
ser = serial.Serial(com, 9600, timeout=0, parity=serial.PARITY_NONE, rtscts=0)

def switch(on = 1):
    cmd = str(on) + '\n'
    cmd = str.encode(cmd)
    ser.write(cmd)
    print(cmd)