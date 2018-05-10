import cv2 as cv

THRESHOLD_LOW = (15, 210, 20);
THRESHOLD_HIGH = (35, 255, 255);

MIN_RADIUS = 10

CAMERA_WIDTH = 1366
CAMERA_HIGHT = 768

cam = cv.VideoCapture(0)
cam.set(cv.cv.CV_CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
cam.set(cv.cv.CV_CAP_PROP_FRAME_HIGHT, CAMERA_HIGHT)

print ("Camera Initialized:")

while True:
    ret_val, img = cam.read()
    
    img_filter = cv.GaussianBlur(img.copy(), (3, 3), 0)
    
    img_filter = cv.cvtColor(img_filter, cv.COLOR_BGR2HSV)
    
    img_binary = cv.inRange(img_filter.copy(), THRESHOLD_LOW, THRESHOLD_HIGH)
    
    img_binary = cv.dilate(img_binary, None, iterations = 1)
    
    img_contours = img_binary.copy()
    
    contours = cv.findContours(img_contours, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
    
    cv.drawContours(img_contours, contours, -1, (0, 255, 0), 5)
    
    center = None
    radius = 0
    if len(contours) > 0:
        c = max(contours, key=cv.contourArea)
        ((x ,y), radius) = cv.minEnclosingCircle(c)
        M = cv.moments(c)
        if M["m00"] > 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius < MIN_RADIUS:
                center = None
                
    if center != None:
        cv.circle(img, center, int(round(radius)), (0, 255, 0))
    
    cv.imshow("webcam", img)
    cv.imshow("binary", img_binary)
    cv.imshow("contours", img_contours)
    
    
    if cv.waitKey(1) == 27:
       break
    
cv.destroyAllWindows()
