from machine import UART,PWM,Pin
import time
lora = UART(0,baudrate=9600,tx=Pin(0),rx=Pin(1))
radar = UART(1,baudrate=115200,tx=8,rx=9)
led = Pin(25,Pin.OUT)

def lora_sent(message):
    pass
    uart.write()

def lora_listening():
    mess = uart.read()
    pass

def radar_scan():
    pass
    data = radar.read()
    if data:
        lora_sent()
        return data


while True:
    radar_scan()
    lora_listening()
    time.sleep(0.01)