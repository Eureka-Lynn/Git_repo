import serial
import time
import threading

# 设置 COM 端口（按你的情况修改）
PORT = "COM3"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=0.1)

print("Connected to Pico on", PORT)

# ------------ 后台线程：持续读取 Pico 输出 ------------
def read_thread():
    while True:
        try:
            line = ser.readline()
            if line:
                try:
                    print("[PICO]", line.decode("utf-8").strip())
                except:
                    print("[PICO RAW]", line)
        except:
            pass
        time.sleep(0.01)

# 启动后台线程
t = threading.Thread(target=read_thread, daemon=True)
t.start()

# ------------ 主循环：从键盘输入命令发送到 Pico ------------
print("输入指令并回车发送给 Pico：")
print("LED_ON / LED_OFF / ALL_OFF")
print("按 Ctrl+C 退出\n")

while True:
    try:
        cmd = input("> ").strip()
        if cmd:
            ser.write((cmd + "\n").encode("utf-8"))
    except KeyboardInterrupt:
        print("\n退出程序")
        break

ser.close()
