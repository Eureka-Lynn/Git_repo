import time
import network
import ubinascii
import machine
import json
from umqtt.robust import MQTTClient

# ---------- 配置 ----------
SSID = "王帅什么时候能上S"
PASSWORD = "wangshuaicaonima"
MQTT_BROKER = "192.168.3.111"  # ← 教师端电脑IP
STUDENT_NAME = "张三"
STUDENT_ID = "200511"

# ---------- 引脚定义 ----------
BUTTON_PIN = 14  # 按钮连接的GPIO引脚
LED_PIN = 15     # LED连接的GPIO引脚

button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(LED_PIN, machine.Pin.OUT)

# 学生状态
STUDENT_STATE = {
    "hand_raised": False
}

# ---------- Wi-Fi ----------
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(0.5)
    print("WiFi connected:", wlan.ifconfig())

# ---------- MQTT 消息处理 ----------
def on_message(topic, msg):
    try:
        data = json.loads(msg)
    except Exception as e:
        print("JSON解析失败:", e)
        return

    # 只处理发给自己的消息
    if data.get("student_id") != STUDENT_ID:
        return

    # 教师端控制取消举手
    hand_raised = data.get("hand_raised", False)
    STUDENT_STATE["hand_raised"] = hand_raised
    led.value(1 if hand_raised else 0)
    print(f"教师端控制: hand_raised={hand_raised}")

# ---------- MQTT 循环 ----------
def mqtt_loop(client):
    last_ping = time.time()
    last_button_state = button.value()

    while True:
        client.check_msg()  # 处理接收消息

        # 按钮检测（下降沿触发）
        current_button_state = button.value()
        if last_button_state == 1 and current_button_state == 0:
            # 按下按钮，切换举手状态
            STUDENT_STATE["hand_raised"] = not STUDENT_STATE["hand_raised"]

            led.value(1 if STUDENT_STATE["hand_raised"] else 0)

            # 发送状态到教师端
            payload = json.dumps({
                "student_id": STUDENT_ID,
                "hand_raised": STUDENT_STATE["hand_raised"]
            })
            client.publish("classroom", payload.encode('utf-8'))
            print(f"发布举手状态: {payload}")

            time.sleep(0.2)  # 防抖

        last_button_state = current_button_state

        # 定期发送心跳
        if time.time() - last_ping > 30:
            client.ping()
            last_ping = time.time()

        time.sleep(0.05)

# ---------- 主函数 ----------
def main():
    connect_wifi(SSID, PASSWORD)
    client_id = b"pico_" + ubinascii.hexlify(machine.unique_id())

    while True:
        try:
            client = MQTTClient(client_id, MQTT_BROKER, keepalive=60)
            client.set_callback(on_message)
            client.connect()

            # 发布上线消息
            join_msg = json.dumps({
                "type": "join",
                "name": STUDENT_NAME,
                "student_id": STUDENT_ID
            })
            client.publish("classroom", join_msg.encode('utf-8'))
            print("已发布上线消息")

            # 订阅教师端指令
            client.subscribe("classroom")
            print("已订阅 classroom 主题")

            mqtt_loop(client)

        except OSError as e:
            print("连接丢失，5秒后重试...", e)
            time.sleep(5)

main()
