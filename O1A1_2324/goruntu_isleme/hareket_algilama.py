import cv2
import numpy as np
from datetime import datetime as dt
cap = cv2.VideoCapture(0)
durum1,eski=cap.read()
durum2,yeni=cap.read()
fw=int(cap.get(3))
fh=int(cap.get(4))
kayit= cv2.VideoWriter(str(dt.now())+".avi",cv2.VideoWriter_fourcc(*"DIVX"),20,(fw,fh))
while True:
    fark=cv2.absdiff(eski,yeni)
    fark_gri=cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    t,sb=cv2.threshold(fark_gri,20,255,cv2.THRESH_BINARY)    
    konturlar,hiy=cv2.findContours(sb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
    for kontur in konturlar:
        (x,y,w,h)=cv2.boundingRect(kontur)
        kontur_alani=cv2.contourArea(kontur)
        if kontur_alani>4000:
            cv2.rectangle(eski,(x,y),(x+w,y+h),(0,255,0),1)
            kayit.write(eski)
    cv2.imshow("fark",fark)
    cv2.imshow("fark_gri",fark_gri)
    cv2.imshow("sb",sb)
    cv2.imshow("sonuc",eski)
    eski=yeni
    durum2,yeni=cap.read()
    if not(durum2) or cv2.waitKey(50)==27:
        break
cap.release()
kayit.release()
cv2.destroyAllWindows()
    