from machine import Pin,UART
import time
uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
LED = Pin(2,Pin.OUT)

while True:
    mess = uart.read()
    if mess == b'open':
        LED.value(1)
        print('receive')
    if mess == b'close':
        LED.value(0)
        print('receive')
    time.sleep(0.1)