import cv2
import numpy as np


# haarcascade dosyası
siniflandirici = cv2.CascadeClassifier("goruntu_isleme/bolum2/haarcascade_frontalface.xml")

cap = cv2.VideoCapture("goruntu_isleme/bolum2/ornek_video.mp4")

while True:
    state,cerceve = cap.read()
    gray = cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    yuzler = siniflandirici.detectMultiScale(gray,1.1,5)
       
    for (x,y,w,h) in yuzler: 
        yuz=cerceve[y:y+h,x:x+w]
        yuz_blur=cv2.medianBlur(yuz,91)
        cerceve[y:y+h,x:x+w]=yuz_blur      
        cv2.rectangle(cerceve,(x,y),(x+w,y+h),(0,255,0),1)
        
    
    cv2.imshow("cerceve",cerceve)
    if cv2.waitKey(100)==27 or not(state):
        break
cap.release()
cv2.destroyAllWindows()
    
    
        