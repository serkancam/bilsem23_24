# yuz_tespiti.py

import cv2
import numpy as np

cap = cv2.VideoCapture("goruntu_isleme/images/ornek_video.mp4")

face_cascade=cv2.CascadeClassifier("goruntu_isleme/images/bolum2/haarcascade_frontalface.xml")

while True:
    state,frame=cap.read()
    
    faces=face_cascade.detectMultiScale(frame,1.1,5)    
    for (x,y,w,h) in faces:
        # roi = frame[y:y+h,x:x+w]
        # blur_roi=cv2.medianBlur(roi,67)
        # frame[y:y+h,x:x+w]=blur_roi
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)        
    
    cv2.imshow("video",frame)
    
    if cv2.waitKey(50)==27 or not(state):
        break
    
cap.release()
cv2.destroyAllWindows()