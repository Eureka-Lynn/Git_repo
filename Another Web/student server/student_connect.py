import time
from umqtt.robust import MQTTClient
import network
import ubinascii
import machine
import json

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(0.5)
    print("WiFi connected:", wlan.ifconfig())

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
            print("Connection lost, reconnecting...", e)
            raise e

def main():
    ssid = "HUAWEI-B919WJ"
    password = "lpq200531"
    broker = "192.168.3.13"
    
    # 学生信息
    STUDENT_NAME = "张三"
    STUDENT_ID = "2025001"
    CLIENT_ID = b"pico_" + ubinascii.hexlify(machine.unique_id())

    connect_wifi(ssid, password)

    while True:
        try:
            client = MQTTClient(CLIENT_ID, broker, keepalive=60)
            client.set_callback(lambda topic, msg: print("Received:", topic, msg))
            client.connect()

            # 发布上线消息
            join_topic = "classroom/students/join"
            join_msg = json.dumps({
                "name": STUDENT_NAME,
                "student_id": STUDENT_ID
            })
            client.publish(join_topic, join_msg.encode('utf-8'))
            print("Published join message")

            # 订阅教师控制主题
            control_topic = f"classroom/control/{STUDENT_ID}"
            client.subscribe(control_topic)

            mqtt_loop(client)

        except OSError as e:
            print("Error, retrying in 5 seconds...", e)
            time.sleep(5)

main()
