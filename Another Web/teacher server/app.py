# 记得PATH # $env:GEVENT_SUPPORT="True"

from gevent import monkey
monkey.patch_all()

import json
import paho.mqtt.client as mqtt
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

MQTT_BROKER = '192.168.3.111'  # 请按实际环境修改
MQTT_PORT = 1883
MQTT_TOPIC = 'classroom'

students = {}      # { student_id: {name, student_id, hand_raised, online} }
mqtt_client = mqtt.Client()

def debug_log(msg):
    print(msg)
    socketio.emit('debug_message', {'message': msg})

def on_connect(client, userdata, flags, rc):
    debug_log(f"Connected to MQTT broker, rc={rc}")
    # 订阅 classroom（QoS=2）
    client.subscribe(MQTT_TOPIC, qos=2)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
    except Exception as e:
        debug_log(f"JSON解析失败: {e}, raw={msg.payload}")
        return

    msg_type = data.get("type")
    sid = str(data.get("student_id", ""))

    # 学生上线
    if msg_type == "join" and sid:
        students[sid] = {
            "name": data.get("name", "未知"),
            "student_id": sid,
            "hand_raised": False,
            "online": True
        }
        debug_log(f"学生上线: {students[sid]}")
        socketio.emit('mqtt_message', {'topic': 'join', 'data': students[sid]})
        return

    # 学生举手/放下（单个）
    if sid and "hand_raised" in data:
        if sid not in students:
            students[sid] = {"name": "未知", "student_id": sid, "online": True}
        students[sid]["hand_raised"] = bool(data["hand_raised"])
        students[sid]["online"] = True
        debug_log(f"学生状态更新: {students[sid]}")
        socketio.emit('mqtt_message', {'topic': 'hand_raise', 'data': students[sid]})
        return

    # 教师/系统统一取消举手
    if msg_type == "cancel_all":
        # 将所有学生的 hand_raised 设为 False（但保持在线状态不变）
        for s in students.values():
            s["hand_raised"] = False
        debug_log("收到 cancel_all: 教师端请求所有学生放下手")
        # 向前端广播每个学生更新：可以发送一次带数组的事件或多次发送单个事件。
        # 为兼容现有前端处理，逐个发 hand_raise 更新事件：
        for sid_key, sdata in students.items():
            socketio.emit('mqtt_message', {'topic': 'hand_raise', 'data': sdata})
        return

    # 学生异常掉线（LWT）
    if msg_type in ("lwt", "offline") and sid:
        if sid not in students:
            students[sid] = {"name": data.get("name", "未知"), "student_id": sid}
        students[sid]["hand_raised"] = False
        students[sid]["online"] = False
        debug_log(f"学生掉线: {students[sid]}")
        socketio.emit('mqtt_message', {'topic': 'lwt', 'data': students[sid]})
        return


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def get_students():
    return jsonify(list(students.values()))

@app.route('/cancel_hand_raise/<student_id>', methods=['POST'])
def cancel_hand_raise(student_id):
    sid = str(student_id)
    if sid in students:
        students[sid]["hand_raised"] = False
        students[sid]["online"] = True
        socketio.emit('mqtt_message', {'topic': 'hand_raise', 'data': students[sid]})

        # MQTT通知学生端（单个学生放下）
        payload = json.dumps({
            "type": "hand_raise",
            "student_id": sid,
            "hand_raised": False
        })
        mqtt_client.publish(MQTT_TOPIC, payload.encode('utf-8'), qos=2)
        debug_log(f"教师端控制学生 {sid} 放下手 -> classroom (qos=2)")
        return jsonify({'status': 'ok'})

    return jsonify({'status': 'student_not_found'}), 404

# 新增：教师端一键取消所有学生举手
@app.route('/cancel_all', methods=['POST'])
def cancel_all():
    # 发布 cancel_all 消息（所有学生收到并放下）
    payload = json.dumps({
        "type": "cancel_all"
    })
    mqtt_client.publish(MQTT_TOPIC, payload.encode('utf-8'), qos=2)
    debug_log("教师发起 cancel_all -> classroom (qos=2)")
    return jsonify({'status': 'ok'})

# MQTT 循环
def mqtt_loop():
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_forever()  # 持续循环处理接收消息

if __name__ == '__main__':
    socketio.start_background_task(mqtt_loop)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)
