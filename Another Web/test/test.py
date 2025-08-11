from flask import Flask
from flask_socketio import SocketIO,emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return 'Hello World'

@app.route('/test')
def test():
    socketio.emit('mqtt_message', {'topic': 'test', 'data': {'msg': 'Hello from server'}})
    return 'Test message emitted!'

if __name__ == '__main__':
    import eventlet
    import eventlet.wsgi
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)

