import socket
import io
import struct
import time
import cv2


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.10', 8000))
connection = client_socket.makefile('wb')

CAMERA_WIDTH = 600
CAMERA_HEIGHT = 300

try:
    with cv2.VideoCapture(0) as cam:
        cam.set(cv2.CV_CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
        cam.set(cv2.CV_CAP_PROP_FRAME_HIGHT, CAMERA_HEIGHT)
        time.sleep(2)
        start = time.time()
        stream = io.BytersIO()
        
        for foo in camera.capture_continuous(stream, 'jpeg', use_video_port = True):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            if time.time() - start > 600:
                break
            stream.seek(0)
            stream.truncate()
        connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()
    
        
        
        