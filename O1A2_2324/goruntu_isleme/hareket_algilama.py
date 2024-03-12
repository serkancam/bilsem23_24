import cv2
import numpy as np
from datetime import datetime as dt

cap=cv2.VideoCapture(0)

durum1,eski=cap.read()
durum2,yeni=cap.read()

fw=int(cap.get(3))
fh=int(cap.get(4))
kayitci=cv2.VideoWriter("kayitlar/"+str(dt.now())+".avi",cv2.VideoWriter_fourcc(*"DIVX"),20,(fw,fh))
while True:
    fark=cv2.absdiff(yeni,eski)
    fark_gri=cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    gri_blur=cv2.GaussianBlur(fark_gri,(3,3),0)
    t,sb=cv2.threshold(gri_blur,20,255,cv2.THRESH_BINARY)
    
    konturlar,hiy=cv2.findContours(sb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    
    for kontur in konturlar:
        (x,y,w,h)=cv2.boundingRect(kontur)
        kontur_alani=cv2.contourArea(kontur)
        if kontur_alani>2000:
            
            cv2.rectangle(eski,(x,y),(x+w,y+h),(0,255,0),1)
            cv2.putText(eski,str(dt.now()),(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)
            kayitci.write(eski)
            
            
    cv2.imshow("fark",fark)
    cv2.imshow("sb",sb)
    cv2.imshow("sonuc",eski)
    if not(durum2) or cv2.waitKey(50)==27:
        break
    
    eski=yeni
    durum2,yeni=cap.read()

cap.release()
kayitci.release()
cv2.destroyAllWindows()
    