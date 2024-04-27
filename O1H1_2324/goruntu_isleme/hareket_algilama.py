#23 mart buradan devam

import cv2
import numpy as np
from datetime import datetime as dt
# cap = cv2.VideoCapture("goruntu_isleme/bolum2/hareket3.mp4")
cap = cv2.VideoCapture(0)
state1,f_eski=cap.read()
state2,f_yeni=cap.read()
while True:    
    fark=cv2.absdiff(f_eski,f_yeni)
    fark_gri=cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(fark_gri,(3,3),0)
    t,sb=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    konturlar,hiy=cv2.findContours(sb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for kontur in konturlar:
        kontur_alani=cv2.contourArea(kontur)
        if kontur_alani>2000:
            (x,y,w,h)=cv2.boundingRect(kontur)
            cv2.rectangle(f_eski,(x,y),(x+w,y+h),(0,255,0),1)           
                   
    cv2.imshow("video",f_eski)
    # hareketi tespit kısmını yaz 28 ekime pas
    f_eski=f_yeni
    state2,f_yeni=cap.read()
    if cv2.waitKey(50)==27 or not(state2):
        break
cap.release()
cv2.destroyAllWindows()   