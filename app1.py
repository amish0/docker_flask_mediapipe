from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import base64
import numpy as np
import cv2
from mediapipe_test import ObjectDetector

obj_det = ObjectDetector()
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('my_response', {'data': 'Connected'})

@socketio.on('video_frame')
def handle_video_frame(data):
    try:
        frame = data['frame']
        #decode frame
        image_data = base64.b64decode(frame.split(',')[1])
        nparr = np.frombuffer(image_data, np.uint8)
        # Decode array into image
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # Assuming you have OpenCV installed
        # Process the image as needed
        print("Received frame:", image.shape)
        image = obj_det.process(image)
        # image = cv2.rectangle(image, (10, 10), (100, 100), (0, 255, 0), 2)
        # Encode the image
        # if len(image.shape) > 2:
        _, buffer = cv2.imencode('.jpg', image)
        image = base64.b64encode(buffer)
        image = image.decode('utf-8')
        # Send the processed image back
        socketio.emit('request_frame', {'frame': 'data:image/jpeg;base64,' + image})
    except:
        print("Error processing frame")
    # _, buffer = cv2.imencode('.jpg', image)
    # image = base64.b64encode(buffer)
    # image = image.decode('utf-8')
    # # Send the processed image back
    # socketio.emit('request_frame', {'frame': 'data:image/jpeg;base64,' + image})

if __name__ == '__main__':
    # context = ('cert.pem', 'key.pem')
    socketio.run(app,  host="0.0.0.0", debug=True, allow_unsafe_werkzeug=True)
