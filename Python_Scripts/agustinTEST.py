import cv2 as cv #imports computer vision library as cv2

THRESHOLD_LOW = (15, 210, 20);# sets the minimum threshold for yellow in b/w
THRESHOLD_HIGH = (35, 255, 255);# sets the maximum threshold for yellow in b/w

MIN_RADIUS = 10 #creates a int value later to be used in creating a circle

cam = cv.VideoCapture(0)# assigns the first cam(0) to the variable cam
print ("Camera Initialized:")# prints to commanWin when camera initialzes 4 debugin


cam_width = 120 #stores cam_width/height with the interger value corresponding to
cam_height = 720#pixel dim of video input feed from cam(0)


#while cam recieves a feed from camera(0); stores still images in memory, converts
#to binary, then passes binary still through filters checking for pixels within
#our predetermined threshold values (yello in this case), selescts pixels within
#threshold and converts those pixels to white, and all others to black.
#Then dialates white/black img for better processing, then this image is sent
#through cv.contour detection which finds our yello obj. and circles in green
while True:
    ret_val, img = cam.read()#stores cam(0) still image to variable img,
                             #and something about a ret_val...
    
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

