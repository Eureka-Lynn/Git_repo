import time
import network
import ubinascii
import machine
import json
from umqtt.robust import MQTTClient

# ---------- 配置 ----------
SSID = "HUAWEI-B919WJ"
PASSWORD = "lpq200531"
MQTT_BROKER = "192.168.3.13"
STUDENT_NAME = "张三"
STUDENT_ID = "200511"

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

    # 处理教师端取消举手
    if data.get("student_id") == STUDENT_ID:
        hand_raised = data.get("hand_raised", False)
        STUDENT_STATE["hand_raised"] = hand_raised
        print(f"收到取消举手消息，hand_raised={hand_raised}")

# ---------- MQTT 循环 ----------
def mqtt_loop(client):
    last_ping = time.time()
    while True:
        try:
            client.check_msg()
            if time.time() - last_ping > 30:
                client.ping()
                last_ping = time.time()
            time.sleep(0.1)
        except OSError as e:
            print("连接丢失，重连中...", e)
            raise e

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
            join_topic = "classroom/students/join"
            join_msg = json.dumps({
                "name": STUDENT_NAME,
                "student_id": STUDENT_ID
            })
            client.publish(join_topic, join_msg.encode('utf-8'))
            print("已发布上线消息")

            # 订阅教师端取消举手消息
            hand_raise_topic = "classroom/students/hand_raise"
            client.subscribe(hand_raise_topic)
            print("已订阅取消举手主题")

            # ---------- 虚拟举手示例 ----------
            # 可以用按键替代下面的虚拟触发
            time.sleep(5)  # 等待 5 秒后虚拟举手
            STUDENT_STATE["hand_raised"] = True
            client.publish(hand_raise_topic, json.dumps({
                "student_id": STUDENT_ID,
                "hand_raised": True
            }))
            print("已虚拟举手")

            mqtt_loop(client)

        except OSError as e:
            print("错误，5秒后重试...", e)
            time.sleep(5)

main()


"""
测试用例
classroom/students/join
{
  "name": "张三",
  "student_id": "200511"
}

classroom/students/hand_raise
{
  "student_id": "200511",
  "hand_raised": true
}

"""