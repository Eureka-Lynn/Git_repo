from machine import Pin,UART
import time
uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
LED = Pin(2,Pin.OUT)

while True:
    mess = input()
    if mess:
        uart.write(mess)
        LED.toggle()
    time.sleep(0.1)