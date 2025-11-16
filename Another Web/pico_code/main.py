# main.py（Pico, MicroPython）
import machine
import time
import sys
import select

BUTTON_PIN = 14
LED_PIN = 15

button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(LED_PIN, machine.Pin.OUT)

last = button.value()

# 使用 select 避免阻塞
poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

def read_serial_nonblocking():
    ready = poll.poll(0)
    if ready:
        try:
            line = sys.stdin.readline()
            if line:
                # line 已经是 str（MicroPython 在很多固件上返回 str）
                s = line.strip()
                return s
        except Exception as e:
            # 容忍任何串口读取错误
            try:
                print("SERIAL_READ_ERR", e)
            except:
                pass
    return None

print("[PICO] READY")

while True:
    cmd = read_serial_nonblocking()
    if cmd:
        print('receive:',cmd)
        # 兼容 bytes/str
        try:
            if isinstance(cmd, bytes):
                print('cmd为bytes')
                text = cmd.decode('utf-8', 'ignore')
            else:
                print('cmd为str')
                text = str(cmd)
        except:
            text = str(cmd)

        if text == "LED_ON":
            led.value(1)
        elif text == "LED_OFF":
            led.value(0)
        elif text == "ALL_OFF":
            led.value(0)
        # 返回 ACK 以便 PC 确认
        print("[ACK]", text)

    # 按键下降沿检测：1 -> 0
    cur = button.value()
    if last == 1 and cur == 0:
        print("BTN")
        # 消抖
        time.sleep(0.18)
    last = cur

    time.sleep(0.02)
