from machine import Pin,UART
import time
uart = UART(0,baudrate=9600)

pin = Pin(28,Pin.OUT)
pin.value(1)

key = Pin(3,Pin.OUT)
key.value(0)

while True:
    message = input()
    if message == 'break':
        break
    uart.write(message)
    time.sleep(1)
    if uart.any():
        recieve = uart.read()
        print(recieve)
    time.sleep(0.1)
key.value(1)