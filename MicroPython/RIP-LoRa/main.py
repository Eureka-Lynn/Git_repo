from machine import Pin,UART
import math
import time

lora = UART(9600,tx=0,rx=1)
radar = UART(115200,tx=6,rx=7)

def get_radar_data():
    data = radar.read()
    if data:
        target = data[7:-4]
        

def detect_person():
