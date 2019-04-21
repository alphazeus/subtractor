import cv2
import numpy as np

cap= cv2.VideoCapture('cameravideo2.mp4')
ret,prev=cap.read()
prev = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
prev= cv2.GaussianBlur(prev,(5,5),0)
while(1):
	ret,frame=cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame= cv2.GaussianBlur(frame,(5,5),0)
	cv2.imshow('Live',frame)
	diff=cv2.absdiff(prev,frame)
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
	ret,diff = cv2.threshold(diff,10,255,cv2.THRESH_BINARY)
	diff = cv2.dilate(diff,kernel,iterations = 1)
	cv2.imshow('Difference',diff)
	prev=frame
	if (cv2.waitKey(5) & 0xFF) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
