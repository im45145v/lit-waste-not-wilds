import cv2
import numpy as np
import smtplib
import playsound
import threading
#libs
Alarm_Status = False
Fire_Reported = 0
#constants
#playsound lib functions
def play_function():
	while True:
		playsound.playsound('D:/guzzvm.mp3',True) #alarm sound is played using playsound module
while True:
	(grabbed, frame) = video.read()
	if not grabbed:
		break
	frame = cv2.resize(frame, (960, 540)) #resizing the frame
	blur = cv2.GaussianBlur(frame, (21, 21), 0) #using Gaussian blur to blur the objects in background and focus on one specific object
   	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV) #converting bgr to hsv
	lower = [18, 50, 50]
	upper = [35, 255, 255] #setting the upper and lower boundaries in a array
	lower = np.array(lower, dtype="uint8")
    	upper = np.array(upper, dtype="uint8") #converting an array to an numpyarray since any operations can be done easily on a numpyarray
	
	mask = cv2.inRange(hsv, lower, upper)
	
    	output = cv2.bitwise_and(frame, hsv, mask=mask)
    	no_red = cv2.countNonZero(mask)
    	if int(no_red) > 25000:
        	Fire_Reported = Fire_Reported + 1

    	cv2.imshow("output", output)

