from machine import Pin,UART
import time

lora = UART(9600,tx=0,rx=1)
