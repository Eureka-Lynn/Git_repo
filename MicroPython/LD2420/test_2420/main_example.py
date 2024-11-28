from machine import UART,Pin,PWM
import time

uart = UART(0,baudrate=115200,tx=Pin(0),rx=Pin(1))
led = PWM(Pin(25,Pin.OUT))
lora = UART(1,baudrate=9600,tx=8,rx=9)
led.freq(1000)
led_duty = 0

while True:
    data = uart.read()
    if data:
        print(data)