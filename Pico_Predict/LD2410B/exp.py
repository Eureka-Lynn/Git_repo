from machine import UART,Pin
import time

radar = UART(0,baudrate=256000,tx = 0,rx = 1)

while 1:
    data = radar.read()
    while data:
        data = data.hex()
        print(data)
    time.sleep(0.1)