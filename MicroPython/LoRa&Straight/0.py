from machine import Pin,UART
import time
uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
lora = UART()
LED = Pin(2,Pin.OUT)

while True:
    if uart.any():
        sent_time = uart.read()
        sent_time = int(sent_time)
        ins_time = int(time.ticks_ms())
        diff = ins_time - sent_time
        print(sent_time)
        print('----------------------------')
        print(ins_time)
        print('----------------------------')
        print(diff)
        time.sleep(0.1)