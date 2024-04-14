from machine import Pin,PWM
import utime

LED = PWM(Pin(25))

LED.freq(1000)
LED.duty_u16(0)

while True:
    LED_duty = int(input('enter Brightness:'))
    assert LED_duty <= 100 and LED_duty >= 0 ,'Brightness range  [0,100]'
    LED.duty_u16(int(LED_duty * 655.36))
    print('Set Brightness {}'.format(LED_duty))