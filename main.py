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
		playsound.playsound('D:/guzzvm.mp3',True)
while True:
	(grabbed, frame) = video.read()
	if not grabbed:break
	frame = cv2.resize(frame, (960, 540))
