import socket
import threading
import json
import time
from queue import Queue

from flask import Flask, render_template, request
import serial
import paho.mqtt.client as mqtt

# 配置
SERIAL_PORT = 'COM3'
SERIAL_BAUD = 115200
MQTT_BROKER = '192.168.3.111'
MQTT_PORT = 1883
MQTT_TOPIC = 'classroom'
FLASK_PORT = 5001

app = Flask(__name__)

client_id = socket.gethostname()
student_info = {
    "client_id": client_id,
    "name": None,
    "student_id": None,
    "hand_raised": False,
    "logged_in": False
}

ser = None
ser_lock = threading.Lock()
mqtt_client = None
serial_event_q = Queue()

# 串口
def open_serial():
    global ser
    try:
        ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=0.1)
        print("打开串口:", SERIAL_PORT)
    except Exception as e:
        print("打开串口失败:", e)
        ser = None

def serial_reader_loop():
    global ser
    while True:
        if ser and ser.is_open:
            try:
                line = ser.readline()
                if line:
                    if isinstance(line, bytes):
                        s = line.decode('utf-8', errors='ignore').strip()
                    else:
                        s = line.strip()
                    print("[PICO RX]", s)
                    if s == "BTN":
                        serial_event_q.put("BTN")
                else:
                    time.sleep(0.02)
            except:
                time.sleep(0.2)
        else:
            time.sleep(1)

def serial_send_cmd(cmd_text):
    global ser
    if ser and ser.is_open:
        with ser_lock:
            try:
                ser.write((cmd_text + "\n").encode('utf-8'))
            except:
                pass

# MQTT
def mqtt_on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC, qos=2)

def mqtt_on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
    except:
        return

    typ = data.get("type")
    msg_client_id = data.get("client_id", "")

    # 只处理针对自己或广播
    if msg_client_id and msg_client_id != student_info["client_id"]:
        return

    if typ == "hand_raise":
        hr = bool(data.get("hand_raised", False))
        student_info["hand_raised"] = hr
        if hr:
            serial_send_cmd("LED_ON")
        else:
            serial_send_cmd("LED_OFF")
    elif typ == "cancel_all":
        student_info["hand_raised"] = False
        serial_send_cmd("LED_OFF")

# 串口事件处理
def serial_event_processor():
    global mqtt_client
    while True:
        ev = serial_event_q.get()
        if ev == "BTN" and student_info["logged_in"]:
            student_info["hand_raised"] = not student_info["hand_raised"]
            payload = {
                "type": "hand_raise",
                "client_id": student_info["client_id"],
                "student_id": str(student_info["student_id"]),
                "name": student_info["name"],
                "hand_raised": student_info["hand_raised"],
                "online": True
            }
            mqtt_client.publish(MQTT_TOPIC, json.dumps(payload), qos=2)
            if student_info["hand_raised"]:
                serial_send_cmd("LED_ON")
            else:
                serial_send_cmd("LED_OFF")

# Flask 登录
@app.route('/', methods=['GET','POST'])
def login():
    global mqtt_client
    if request.method == 'POST':
        name = request.form.get('name','').strip()
        sid = request.form.get('student_id','').strip()
        if not name or not sid:
            return "请填写姓名与学号", 400

        student_info["name"] = name
        student_info["student_id"] = sid
        student_info["logged_in"] = True

        # MQTT 初始化
        client_id = student_info["client_id"]
        mqtt_client = mqtt.Client(client_id=client_id)
        lwt_msg = {
            "type": "lwt",
            "client_id": client_id,
            "name": student_info["name"],
            "student_id": student_info["student_id"],
            "online": False
        }
        mqtt_client.will_set(MQTT_TOPIC, payload=json.dumps(lwt_msg), qos=2, retain=False)

        mqtt_client.on_connect = mqtt_on_connect
        mqtt_client.on_message = mqtt_on_message
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
        mqtt_client.loop_start()

        t1 = threading.Thread(target=serial_reader_loop, daemon=True)
        t1.start()
        t2 = threading.Thread(target=serial_event_processor, daemon=True)
        t2.start()

        # 发布 join 消息
        join_payload = {
            "type": "join",
            "client_id": client_id,
            "name": student_info["name"],
            "student_id": student_info["student_id"],
            "hand_raised": student_info["hand_raised"],
            "online": True
        }
        mqtt_client.publish(MQTT_TOPIC, json.dumps(join_payload), qos=2, retain=True)
        return render_template('student_logged_in.html', name=name, student_id=sid)
    else:
        return render_template('student_login.html')

if __name__ == '__main__':
    open_serial()
    app.run(host='0.0.0.0', port=FLASK_PORT)
