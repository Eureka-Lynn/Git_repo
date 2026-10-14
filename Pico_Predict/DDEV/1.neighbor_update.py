from ds1307 import DS1307  # 引入 DS1307 RTC 库
import time
import machine
import ujson
from machine import Pin, I2C,UART

# 初始化LoRa
lora = UART(0,baudrate=19200)

# 初始化I2C
i2c = I2C(0, scl=Pin(15), sda=Pin(14))  # 根据硬件连接设置SCL和SDA
rtc = DS1307(i2c)  # 初始化DS1307 RTC

# 获取序列号作为唯一标识符
id = machine.unique_id()
# 转化字符串
unique_id_str = ''.join(['{:02x}'.format(b) for b in unique_id])

# 假设的邻居表（节点和它们的时间戳）
neighbor_table = {}

def get_timestamp():
    """获取当前时间戳"""
    current_time = rtc.datetime()  # 获取当前时间
    timestamp = time.mktime(current_time[:6])  # 转换为时间戳（秒）
    return timestamp

def sent_node():
    """广播消息并记录时间戳"""
    time = get_timestamp()

    message = {
        'node_id':unique_id_str,
        'timestamp':time
    }

    # 将字典转换为 JSON 字符串,lora没法直接发dict
    message_str = ujson.dumps(message_dict)
    lora.write(message_str)
    print("发送探测信号...")

def get_neighbors():
    data = lora.read()
    if data:
        # 转回dict
        data_dict = ujson.loads(data)
        node_id = data_dict.get('node_id')
        send_time = data_dict.get('timestamp')
        timestamp = get_timestamp()
        time_diff = timestamp - send_time
        if time_diff <= 1:
            # 记录邻居信息及时间戳
            print(f"发现邻居：{node_id}，时间戳：{timestamp}")
            return node_id, timestamp
        else :
            print('超出范围')
    else:
        print('无数据')

def update_neighbor_table(node_id, timestamp):
    """更新邻居表，将接收到的邻居信息和时间戳保存"""
    neighbor_table[node_id] = timestamp
    print(f"邻居表已更新：{neighbor_table}")

# 示例流程
sent_node()
node_id, timestamp = get_neighbors()  # 获取邻居信息并获取时间戳
update_neighbor_table(node_id, timestamp)  # 更新邻居表
time.sleep(0.5)  # 等待，时间推移
