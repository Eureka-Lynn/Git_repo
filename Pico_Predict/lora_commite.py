from machine import Pin,UART
import time

uart = UART(0,baudrate=19200)

while True :
    data = b'COM6'
    uart.write('A')
    # if uart.any():
    #     text = uart.readline()
    #     print(text)
    if uart.any():
        print(uart.readline())
    time.sleep(0.5)