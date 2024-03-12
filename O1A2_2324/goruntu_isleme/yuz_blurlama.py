import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
yuz_bulucu=cv2.CascadeClassifier("goruntu_isleme/bolum2/haarcascade_frontalface.xml")
while True:
    durum,cerceve=cap.read()
    gri =cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    yuzler = yuz_bulucu.detectMultiScale(gri,1.1,5)
    for (x,y,w,h) in yuzler:
        yuz=cerceve[y:y+h,x:x+w]
        yuz_blurlu=cv2.medianBlur(yuz,77)
        cerceve[y:y+h,x:x+w]=yuz_blurlu
        cv2.rectangle(cerceve,(x,y),(x+w,y+h),(0,255,0),2) 
              
    cv2.imshow("goruntu",cerceve)
    if not(durum) or cv2.waitKey(50)==27:
        break
    
cap.release()
cv2.destroyAllWindows()
