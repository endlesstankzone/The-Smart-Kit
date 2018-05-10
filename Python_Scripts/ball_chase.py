import cv2
import serial
import time

THRESHOLD_LOW = (15, 210, 20);
THRESHOLD_HIGH = (35, 255, 255);

MIN_RADIUS = 10

MIN_SIZE = 20
MAX_SIZE = 40

CAMERA_WIDTH = 600
CAMERA_HEIGHT = 150

cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

camWidth = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
camHeight = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

x = 0

print ("Camera Initialized:")

ser = serial.Serial('/dev/ttyACM0',57600)

while True:
    ret_val, img = cam.read()
    
    img_filter = cv2.GaussianBlur(img.copy(), (3, 3), 0)
    
    img_filter = cv2.cvtColor(img_filter, cv2.COLOR_BGR2HSV)
    
    img_binary = cv2.inRange(img_filter.copy(), THRESHOLD_LOW, THRESHOLD_HIGH)
    
    img_binary = cv2.dilate(img_binary, None, iterations = 1)
    
    img_contours = img_binary.copy()
    
    contours = cv2.findContours(img_contours, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 5)
    
    center = None
    radius = 0
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x ,y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        if M["m00"] > 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius < MIN_RADIUS:
                center = None
                
    if center != None:
        cv2.circle(img, center, int(round(radius)), (0, 255, 0))
        #print(str(center) + " "+ str(radius))
    
    seg3 = camWidth / 3
    
    if 0 <= radius < MIN_SIZE:
        if 0 <= x < (seg3 * 1):
            print("im too far and i want to go left")
            ser.write("l".encode('utf-8'))
            time.sleep(1./120) 
        elif (seg3 * 1) <= x < (seg3 *2):
            print("im too far and i want to go foward")
            ser.write("f".encode('utf-8'))
            time.sleep(1./120) 
        elif (seg3 * 2) <= x <= (seg3 * 3):
            print("im too far and i want to go right")
            ser.write("r".encode('utf-8'))
            time.sleep(1./120) 
            
            
            
    elif MIN_SIZE <= radius <= MAX_SIZE:
        if 0 <= x < (seg3 * 1):
            print("im at the correct distance and i want to go left")
            ser.write("l".encode('utf-8'))
            time.sleep(1./120) 
        elif (seg3 * 1) <= x < (seg3 * 2):
            print("stop")
            ser.write("s".encode('utf-8'))
            time.sleep(1./120) 
        elif (seg3 * 2) <= x <= (seg3 * 3):
            print("im at the correct distance and i want to go right")
            ser.write("r".encode('utf-8'))
            time.sleep(1./120) 
            
            
    else:
        if 0 <= x < (seg3 *1):
            print("im too close and i want to go backwards to the right")
            ser.write("r".encode('utf-8'))
            time.sleep(1./120) 
        elif (seg3 * 1) <= x < (seg3 * 2):
            print("im too close and i want to go backwards")
            ser.write("b".encode('utf-8'))
            time.sleep(1./120) 
        elif (seg3 * 2) <= x <= (seg3 * 3):
            print("im too close and i want to go backwards to the left")
            ser.write("l".encode('utf-8'))
            time.sleep(1./120) 
                  
                  
                  

            
    #cv2.imshow("webcam", img)
    #cv2.imshow("binary", img_binary)
    #cv2.imshow("contours", img_contours)
    
    
    if cv2.waitKey(1) == 27:
       break
    
cv2.destroyAllWindows()
