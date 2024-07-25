from machine import Pin,UART
import time
uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
LED = Pin(2,Pin.OUT)

while True:
    mess = uart.read()
    if mess:
        print('send:',end='')
        print(mess)
        print('----------------------------')
        print('instance:',end='')
        print(time.time())
        print('\n')
        time.sleep(1)