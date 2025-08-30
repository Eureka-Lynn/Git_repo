from gevent import monkey
monkey.patch_all()

import json
import paho.mqtt.client as mqtt
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

MQTT_BROKER = '192.168.3.13'
MQTT_PORT = 1883
MQTT_TOPIC = 'classroom/#'

# 后端保存学生信息，key为str(student_id)
students = {}

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(f"收到 MQTT 消息: {msg.topic} -> {data}")

    # 学生加入
    if msg.topic == 'classroom/students/join' and 'student_id' in data:
        students[str(data['student_id'])] = data
        # 默认手未举
        students[str(data['student_id'])]['hand_raised'] = False
        socketio.emit('mqtt_message', {'topic': msg.topic, 'data': students[str(data['student_id'])]})

    # 学生举手/取消举手
    if msg.topic == 'classroom/students/hand_raise' and 'student_id' in data:
        sid = str(data['student_id'])
        if sid in students:
            students[sid]['hand_raised'] = data.get('hand_raised', False)
            socketio.emit('mqtt_message', {'topic': msg.topic, 'data': students[sid]})

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
        students[sid]['hand_raised'] = False
        socketio.emit('mqtt_message', {'topic': 'classroom/students/hand_raise', 'data': students[sid]})
        # MQTT通知学生端
        mqtt_client = mqtt.Client()
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
        mqtt_client.publish('classroom/students/hand_raise', json.dumps({'student_id': sid, 'hand_raised': False}))
        mqtt_client.disconnect()
        return jsonify({'status': 'ok'})
    return jsonify({'status': 'student_not_found'}), 404

def mqtt_loop():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_forever()

if __name__ == '__main__':
    socketio.start_background_task(mqtt_loop)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)
