from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

players = {}      # {sid: name}
roles = {}        # {sid: role}
room_ready = False

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    global room_ready, roles
    name = data['name']
    sid = request.sid
    players[sid] = name
    print(f"{name} 加入游戏")

    # 通知所有人目前有多少人
    emit("player_list", {"players": list(players.values())}, broadcast=True)

    # 如果人数到 4 且还没分配身份
    if len(players) == 4 and not room_ready:
        imposter_sid = random.choice(list(players.keys()))
        for psid in players:
            roles[psid] = "内鬼" if psid == imposter_sid else "平民"
            # 私密发送给每个玩家
            socketio.emit("your_role", {"role": roles[psid]}, to=psid)
        room_ready = True
        print("身份分配完成！")

@socketio.on('disconnect')
def on_disconnect():
    sid = request.sid
    if sid in players:
        print(f"{players[sid]} 退出了")
        del players[sid]
        emit("player_list", {"players": list(players.values())}, broadcast=True)

@socketio.on('reset_room')
def reset_room():
    global players, roles, room_ready
    players = {}
    roles = {}
    room_ready = False
    emit("player_list", {"players": []}, broadcast=True)
    print("房间已被重置")

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000)
