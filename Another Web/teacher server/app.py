from gevent import monkey
monkey.patch_all()

import json
import paho.mqtt.client as mqtt
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

MQTT_BROKER = '192.168.3.13'
MQTT_PORT = 1883
MQTT_TOPIC = 'classroom/#'

# 后端保存学生信息，key为student_id，value为学生信息dict
students = {}

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(f"收到 MQTT 消息: {msg.topic} -> {data}")

    # 假设学生加入的topic是 'classroom/students/join'，并且payload里有 student_id
    if msg.topic == 'classroom/students/join' and 'student_id' in data:
        students[data['student_id']] = data
        # 推送更新给所有连接前端
        socketio.emit('mqtt_message', {'topic': msg.topic, 'data': data})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test_emit():
    socketio.emit('mqtt_message', {'topic': 'test', 'data': {'msg': 'Hello from server'}})
    return '消息已发送'

# 新增接口：返回所有学生信息给前端
@app.route('/students')
def get_students():
    return jsonify(list(students.values()))

def mqtt_loop():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_forever()

if __name__ == '__main__':
    socketio.start_background_task(mqtt_loop)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)
