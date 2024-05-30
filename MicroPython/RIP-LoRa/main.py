from machine import Pin,UART,PWM
import math
import time

lora = UART(9600,tx=0,rx=1)
radar = UART(115200,tx=6,rx=7)
led = PWM(Pin(25,Pin.OUT))
current_brightness = 0
led.freq(1000)

# 获取雷达数据
def get_radar_data():
    global target
    data = radar.read()
    if data:
        target = data[7:-4]

# 判断状态，有人为True
def detect_person(target):
    match target[0]:
        case 0x01:
            return True
        case _:
            return False

# 获取距离数据，无人情况为无穷大
def get_distance(target):
    if detect_person(target):
        distance = int.from_bytes(target[1:3],'little')
        return distance
    else:
        return float('inf')

# 通过时间戳方式分配节点ID
def get_node_id():
    return int(time.time() * 1000) % 10000

# 广播信息
def send_message(node_id,current_brightness):
    time_stamp = time.time()
    message = '{0}:{1}:{2}'.format(node_id,time_stamp,current_brightness)
    lora.write(message)

# 接收信息
def receive_message():
    if lora.any():
        message = lora.read()
        return message
    return None

# 调光
def change_brightness(LED_Duty):
    while LED_Duty > current_brightness:
        current_brightness += 1
        led.duty_u16(current_brightness)
    while LED_Duty < current_brightness:
        current_brightness -= 1
        led.duty_u16(current_brightness)

# 处理LoRa信息
def handle_LoRa(message):
    Lora_Data = message.split(':')
    Node_id = Lora_Data[0]
    Time_Stamp = Lora_Data[1]
    Node_Brightness = Lora_Data[2]
    return Node_id,Time_Stamp,Node_Brightness

# 相邻节点发现
def find_neighbor():
    pass