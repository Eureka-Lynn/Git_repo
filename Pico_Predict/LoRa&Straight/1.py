from machine import Pin,UART
import time
lora = UART(0,baudrate = 19200,tx = Pin(0),rx = Pin(1))
LED = Pin(2,Pin.OUT)

while True:
    mess = input()
    lora.write(mess)
    time.sleep(0.1)