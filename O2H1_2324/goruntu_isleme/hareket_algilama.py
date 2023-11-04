import cv2
import numpy as np
from datetime import datetime as dt
cap = cv2.VideoCapture(0)
state1,f_eski=cap.read()
state2,f_yeni=cap.read()
fw=int(cap.get(3))
fh=int(cap.get(4))
kayit=cv2.VideoWriter(str(dt.now())+".avi",cv2.VideoWriter_fourcc(*"DIVX"),20,(fw,fh))
while True:    
    fark=cv2.absdiff(f_eski,f_yeni)
    gri_fark= cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    yumusak=cv2.GaussianBlur(gri_fark,(3,3),0)   
    t,sb=cv2.threshold(yumusak,20,255,cv2.THRESH_BINARY)   
    yayilmis=cv2.dilate(sb,None,iterations=3)
    konturlar,hiyerarsi=cv2.findContours(yayilmis,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for kontur in konturlar:
        (x,y,w,h)=cv2.boundingRect(kontur)
        kontur_alani = cv2.contourArea(kontur)        
        if kontur_alani>4000:        
            cv2.rectangle(f_eski,(x,y),(x+w,y+h),(0,255,0),1)
            kayit.write(f_eski)           
    cv2.imshow("video",f_eski)
    # hareketi tespit kısmını yaz 28 ekime pas
    f_eski=f_yeni
    state2,f_yeni=cap.read()
    if cv2.waitKey(50)==27 or not(state2):
        break
cap.release()
kayit.release()
cv2.destroyAllWindows()    