from machine import UART,Pin,PWM
import time
uart = UART(0,baudrate=115200,tx=Pin(0),rx=Pin(1))
led = PWM(Pin(25,Pin.OUT))
lora = UART(1,baudrate=9600,tx=8,rx=9)
led.freq(1000)
led_duty = 0

def LoRa_Message(mes):
     lora.write(mes)

def LED_PWM(n):
    if n >= led_duty :
            while led_duty <= n-1:
                led_duty += 1
                led.duty_u16(int(led_duty * 655.36))
    elif n <= led_duty:
            while led_duty >= n+1:
                led_duty -= 1
                led.duty_u16(int(led_duty * 655.36))

while True:
    data = uart.read()
    if data:
        print(str(data))
        print('------------------')
        target_data = data[7:-4]
        if data[0] == 0x01:
            target_state = True
        else:
            target_state = False
        distance = target_data[1:3]
        distance_cm = int.from_bytes(distance,'little')
        print('target_state:',target_state)
        print('distance:',distance_cm)
        time.sleep(0.01)