from machine import Pin,PWM
import utime

LED = PWM(Pin(25))

LED.freq(1000)
LED_duty = 0
LED.duty_u16(0)

while True:
    current = int(input('enter'))
    if current >= LED_duty :
       while LED_duty <= current-1:
           LED_duty += 1
           LED.duty_u16(int(LED_duty * 655.36))
           utime.sleep(0.01)
    if current <= LED_duty:
        while LED_duty >= current+1:
            LED_duty -= 1
            LED.duty_u16(int(LED_duty * 655.36))
            utime.sleep(0.01)
    print(LED_duty)