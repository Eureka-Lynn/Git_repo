from machine import UART,Pin,PWM
import time
a
lora = UART(0,baudrate=19200,tx = Pin(0),rx = Pin(1))

while True:
    if lora.any():
        print(lora.read())
        print(time.time())
        time.sleep(1)