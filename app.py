# simple python file for render hellow word in browser
from flask import Flask
from flask import render_template
from cam_loader import CamLoader
from flask_cors import CORS
import flask_socketio as socketio
import threading
import random
app = Flask(__name__)

CORS(app)
socketio = socketio.SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def hello_world():
    # return 'Hello, World!'
    message = "Hello, World!"
    return render_template('index.html', message=message)

def send_random_data():
    while True:
        x = random.randint(1, 100)
        print("x: ", x)
        socketio.emit('frame', x)
        socketio.sleep(1)

@socketio.on('connect')
def handle_connect(data):
    # print("data: ", data)
    print('Client connected')
    socketio.emit('frame', 'Hello, World!')

@socketio.on('video_frame')
def handle_frame(data):
    print(data)
    # cam_loader.stop()
    # print('Client disconnected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    print('received message: ', data)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=8000, debug=True)
    # app.run(debug=True)
    t = threading.Thread(target=send_random_data)
    t.daemon = True
    t.start()
    socketio.run(app,  host="0.0.0.0", port=8000, allow_unsafe_werkzeug=True, debug=True)
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=8000, debug=True)
    