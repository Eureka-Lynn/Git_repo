import time
from machine import UART, Pin

# 配置UART串口
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))  # 串口0，波特率9600，TX引脚0，RX引脚1
key = Pin(2,Pin.OUT)
key.value(0)
try:
    while True:
        # 发送AT命令
        uart.write('AT')
        print("Sent: AT")

        # 等待一段时间
        time.sleep(1)

        # 读取并打印接收到的响应
        if uart.any():  # 检查是否有数据可读
            data_received = uart.read()
            print("Received: {}".format(data_received))

except KeyboardInterrupt:
    # 在Ctrl+C中断时关闭串口
    uart.deinit()
