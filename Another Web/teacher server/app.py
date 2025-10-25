# 记得PATH # $env:GEVENT_SUPPORT="True"

from gevent import monkey
monkey.patch_all()

import json
import paho.mqtt.client as mqtt
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

MQTT_BROKER = '192.168.3.111'
MQTT_PORT = 1883
MQTT_TOPIC = 'classroom'

students = {}      # { student_id: {name, student_id, hand_raised} }
mqtt_client = mqtt.Client()

def debug_log(msg):
    print(msg)
    socketio.emit('debug_message', {'message': msg})

def on_connect(client, userdata, flags, rc):
    debug_log(f"Connected to MQTT broker, rc={rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
    except Exception as e:
        debug_log(f"JSON解析失败: {e}")
        return

    msg_type = data.get("type")
    sid = str(data.get("student_id", ""))

    # 学生上线
    if msg_type == "join" and sid:
        students[sid] = {
            "name": data.get("name", "未知"),
            "student_id": sid,
            "hand_raised": False
        }
        debug_log(f"学生上线: {students[sid]}")
        socketio.emit('mqtt_message', {'topic': 'join', 'data': students[sid]})
        return

    # 学生举手/放下
    if sid and "hand_raised" in data:
        if sid not in students:
            students[sid] = {"name": "未知", "student_id": sid}
        students[sid]["hand_raised"] = bool(data["hand_raised"])
        debug_log(f"学生状态更新: {students[sid]}")
        socketio.emit('mqtt_message', {'topic': 'hand_raise', 'data': students[sid]})
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
        socketio.emit('mqtt_message', {'topic': 'hand_raise', 'data': students[sid]})

        #MQTT发布
        payload = json.dumps({
            "student_id": sid,
            "hand_raised": False
        })
        mqtt_client.publish(MQTT_TOPIC, payload)
        debug_log(f"教师端控制学生 {sid} 放下手 -> classroom")
        return jsonify({'status': 'ok'})

    return jsonify({'status': 'student_not_found'}), 404

#MQTT循环
def mqtt_loop():
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_forever()  # 持续循环处理接收消息

if __name__ == '__main__':
    socketio.start_background_task(mqtt_loop)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)
