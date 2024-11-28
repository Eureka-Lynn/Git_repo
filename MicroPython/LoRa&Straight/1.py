from machine import Pin,UART
import time
lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))
LED = Pin(2,Pin.OUT)

while True:
    time_stamp = time.ticks_ms()
    ins_time = str(time_stamp)
    uart.write(ins_time)
    time.sleep(0.1)