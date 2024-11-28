from machine import UART,Pin,PWM
import time
uart = UART(0,baudrate=115200,tx=Pin(0),rx=Pin(1))
led = PWM(Pin(3,Pin.OUT))
lora = UART(1,baudrate=9600,tx=8,rx=9)
led.freq(10000)
led_duty = 0
led.duty_u16(0)
while True:
    data = uart.read()
    if data:
        num_data = int(data[10:-2])
        print(num_data)
        if num_data >= 200:
            num_data = 0
        else:
            num_data = 200 -num_data
        led.duty_u16(int(320 * num_data))
        
        