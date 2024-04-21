from machine import Pin,UART
import time
uart = UART(0,9600)
key = Pin(2,Pin.OUT)
key.value(0)
uart.write('AT')
time.sleep(1)
print(uart.read())
uart.write('AT+S0?')
time.sleep(0.1)
uart.write('AT+C???')
time.sleep(0.1)
uart.write('AT+RX')
time.sleep(0.1)
print(uart.read())