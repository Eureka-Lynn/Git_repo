from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# 存储房间和用户信息的简单数据结构（模拟数据库）
rooms = []
users = {}
next_user_id = 1  # 用于生成用户ID的计数器

@app.route('/')
def index():
    return render_template('index.html', rooms=rooms)

@app.route('/create_room', methods=['GET', 'POST'])
def create_room():
    if request.method == 'POST':
        room_name = request.form['room_name']
        # 模拟创建房间
        room_id = len(rooms) + 1
        rooms.append({'id': room_id, 'name': room_name, 'num_users': 1, 'owner_id': None})
        # 创建房间后跳转到房主注册页面
        return redirect(url_for('register_owner', room_id=room_id))
    return render_template('create_room.html')

@app.route('/register_owner/<int:room_id>', methods=['GET', 'POST'])
def register_owner(room_id):
    global next_user_id
    if request.method == 'POST':
        user_name = request.form['user_name']
        # 获取房间
        room = next((r for r in rooms if r['id'] == room_id), None)
        if room:
            user_id = next_user_id
            next_user_id += 1
            users[user_id] = {'name': user_name, 'room_id': room_id, 'is_owner': True}
            room['owner_id'] = user_id
            emit_room_update(room_id)  # 通知房间内用户更新
            return redirect(url_for('room_page', room_id=room_id,user_id = user_id))
    return render_template('register_owner.html', room_id=room_id)

def emit_room_update(room_id):
    room_users = {uid: users[uid] for uid in users if users[uid]['room_id'] == room_id}
    socketio.emit('room_update', {'room_id': room_id, 'users': room_users})

@socketio.on('exit_room')
def on_exit_room(user_id):
    # 检查用户是否存在
    user = users.get(user_id)
    if user:
        room_id = user['room_id']
        room = next((r for r in rooms if r['id'] == room_id), None)
        if room:
            # 删除用户
            del users[user_id]
            # 更新房间的玩家人数
            room['num_users'] -= 1
            # 如果房间为空，则删除房间
            if room['num_users'] == 0:
                rooms.remove(room)
            else:
                # 如果房主退出，重新指定房主
                if user_id == room['owner_id']:
                    if users:
                        new_owner = next((u_id for u_id in users if users[u_id]['room_id'] == room_id), None)
                        while new_owner == None:
                            new_owner = next((u_id for u_id in users if users[u_id]['room_id'] == room_id), None)
                        if new_owner:
                            users[new_owner]['is_owner'] = True
                            room['owner_id'] = new_owner

            # 通知房间内用户更新
            emit_room_update(room_id)



@app.route('/register_user/<int:room_id>', methods=['GET', 'POST'])
def register_user(room_id):
    global next_user_id
    if request.method == 'POST':
        user_name = request.form['user_name']
        # 获取房间
        room = next((r for r in rooms if r['id'] == room_id), None)
        if room:
            user_id = next_user_id
            next_user_id += 1
            # 设置用户为普通用户
            users[user_id] = {'name': user_name, 'room_id': room_id, 'is_owner': False}
            # 更新房间的玩家人数
            room['num_users'] += 1
            emit_room_update(room_id)  # 通知房间内用户更新
            return redirect(url_for('room_page', room_id=room_id,user_id = user_id))
    return render_template('register_user.html', room_id=room_id)

@app.route('/room/<int:room_id>')
def room_page(room_id):
    room = next((r for r in rooms if r['id'] == room_id), None)
    if room:
        # 获取房间内所有用户的信息
        users_in_room = [users[user_id] for user_id in users if users[user_id]['room_id'] == room_id]
        return render_template('room_page.html', room_id=room_id, users=users_in_room, user_id=request.args.get('user_id'))
    else:
        return "Room not found", 404



if __name__ == '__main__':
    socketio.run(app, debug=True)
