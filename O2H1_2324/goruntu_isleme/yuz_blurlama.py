import cv2
import numpy as np


# haarcascade dosyası
face_cascade = cv2.CascadeClassifier("goruntu_isleme/images/bolum2/haarcascade_frontalface.xml")

cap = cv2.VideoCapture(0)

while True:
    state,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)
   
    for (x,y,w,h) in faces:        
        yuz = img[y:y+h,x:x+w]
        yuz = cv2.medianBlur(yuz,91)
        img[y:y+h,x:x+w]=yuz
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
        
    
    cv2.imshow("img",img)
    if cv2.waitKey(1)==27 or not(state):
        break
cap.release()
cv2.destroyAllWindows()
    
    
        