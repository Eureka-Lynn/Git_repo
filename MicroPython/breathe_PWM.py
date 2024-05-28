from machine import Pin,PWM
import time

LED = PWM(Pin(1))

LED.freq(1000)
LED_duty = 0
LED.duty_u16(0)

while True:
    while LED_duty <= 65535:
        LED_duty += 1
        LED.duty_u16(LED_duty)
    while LED_duty > 0:
        LED_duty -= 1
        LED.duty_u16(LED_duty)
    time.sleep((0.1))