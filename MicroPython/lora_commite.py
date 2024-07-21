from machine import Pin,UART
import time
uart = UART(0,9600)
# key = Pin(2,Pin.OUT)
while True :
    uart.write('this is a test message from COM3')
    print('sent message')
    
    time.sleep(1)
    
    text = uart.readline()    
    if text:
        print(text)