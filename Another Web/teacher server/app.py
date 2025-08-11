import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

MQTT_BROKER = '192.168.3.13'
MQTT_PORT = 1883
MQTT_TOPIC = 'classroom/#'

# MQTT 回调
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(f"收到 MQTT 消息: {msg.topic} -> {data}")
    socketio.emit('mqtt_message', {'topic': msg.topic, 'data': data})

# 运行 MQTT 循环的后台任务
def mqtt_loop():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_forever()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test_emit():
    socketio.emit('mqtt_message', {'topic': 'test', 'data': {'msg': 'Hello from server'}})
    return '消息已发送'

if __name__ == '__main__':
    # 在 SocketIO 启动前开启 MQTT 循环线程（eventlet 协程）
    socketio.start_background_task(mqtt_loop)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)
