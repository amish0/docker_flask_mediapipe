# Write the class file to load camera images and return them to the app.py file

# Import the necessary packages
from threading import Thread
import cv2

class CamLoader:
    def __init__(self, src=0):
        self.cam_id = src
        self.frame = None
        self.keep_running = False
        self.thread = None
    
    def start(self):
        self.keep_running = True
        self.thread = Thread(target=self._capture, args=())
        self.thread.start()
        return self
    
    def _capture(self):
        cam = cv2.VideoCapture(self.cam_id)
        while self.keep_running:
            ret, frame = cam.read()
            if ret:
                self.frame = frame
        self.frame = None
        cam.release()
    
    def read(self):
        return self.frame
    
    def stop(self):
        self.keep_running = False
        self.thread.join()