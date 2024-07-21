from machine import Pin,UART
import time
uart = UART(0,9600)
key = Pin(3,Pin.OUT)
key.value(0)
while True:
    message = input()
    uart.write(message)
    time.sleep(1)
    if uart.any():
        recieve = uart.read()
        print(recieve)
    time.sleep(0.1)