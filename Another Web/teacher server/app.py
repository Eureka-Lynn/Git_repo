# $env:GEVENT_SUPPORT="True"
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

students = {}      # { client_id: {name, student_id, hand_raised, online} }
mqtt_client = mqtt.Client()

def debug_log(msg):
    print(msg)
    socketio.emit('debug_message', {'message': msg})

def on_connect(client, userdata, flags, rc):
    debug_log(f"Connected to MQTT broker, rc={rc}")
    client.subscribe(MQTT_TOPIC, qos=2)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
    except Exception as e:
        debug_log(f"JSON解析失败: {e}, raw={msg.payload}")
        return

    msg_type = data.get("type")
    print('msg_type==',msg_type)
    cid = data.get("client_id", "")


    # 教师/系统统一取消举手
    if msg_type == "cancel_all":
        print('recived cancel_all')
    # 将所有学生 hand_raised 设为 False（保持 online 不变）
        for s in students.values():
            s["hand_raised"] = False
        debug_log("收到 cancel_all: 教师端请求所有学生放下手")
        print(students.items())
        # 逐个发送 hand_raise 事件更新前端显示
        for sid_key, sdata in students.items():
            socketio.emit('mqtt_message', {'topic': 'hand_raise', 'data': sdata})
        return

    # 学生上线
    if msg_type == "join":
        print('recieved join')
        students[cid] = {
            "name": data.get("name", "未知"),
            "student_id": data.get("student_id", ""),
            "hand_raised": False,
            "online": True,
            "client_id": cid
        }
        debug_log(f"学生上线: {students[cid]}")
        socketio.emit('mqtt_message', {'topic': 'join', 'data': students[cid]})
        return


    # 学生举手/放下
    if msg_type == "hand_raise":
        print('recieved hand_raise')
        if cid not in students:
            students[cid] = {
                "name": data.get("name", "未知"),
                "student_id": data.get("student_id", ""),
                "client_id": cid,
                "online": True
            }
        students[cid]["hand_raised"] = bool(data["hand_raised"])

        socketio.emit('mqtt_message', {'topic': 'hand_raise', 'data': students[cid]})
        debug_log(f"学生状态更新: {students[cid]}")
        return



    # 学生异常掉线（LWT）
    if msg_type in ("lwt"):
        if cid not in students:
            students[cid] = {
                "name": data.get("name", "未知"),
                "student_id": data.get("student_id", ""),
                "client_id": cid
            }
        students[cid]["hand_raised"] = False
        students[cid]["online"] = False
        socketio.emit('mqtt_message', {'topic': 'lwt', 'data': students[cid]})
        debug_log(f"学生掉线: {students[cid]}")

# Flask 路由
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def get_students():
    return jsonify(list(students.values()))

# 单个学生放下手（基于 client_id）
@app.route('/cancel_hand_raise/<client_id>', methods=['POST'])
def cancel_hand_raise(client_id):
    cid = str(client_id)
    if cid in students:
        students[cid]["hand_raised"] = False
        socketio.emit('mqtt_message', {'topic': 'hand_raise', 'data': students[cid]})
        payload = json.dumps({
            "type": "hand_raise",
            "client_id": cid,
            "hand_raised": False
        })
        mqtt_client.publish(MQTT_TOPIC, payload.encode('utf-8'), qos=2)
        debug_log(f"教师端控制学生 {cid} 放下手 -> classroom (qos=2)")
        return jsonify({'status': 'ok'})
    return jsonify({'status': 'student_not_found'}), 404

# 教师端一键取消所有学生举手
@app.route('/cancel_all', methods=['POST'])
def cancel_all():
    payload = json.dumps({"type": "cancel_all",})
    mqtt_client.publish(MQTT_TOPIC, payload.encode('utf-8'), qos=2)
    debug_log("教师发起 cancel_all -> classroom (qos=2)")
    return jsonify({'status': 'ok'})

# MQTT 循环
def mqtt_loop():
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_forever()

if __name__ == '__main__':
    socketio.start_background_task(mqtt_loop)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)
