import cv2
import numpy as np

yuz_bulucu = cv2.CascadeClassifier("goruntu_isleme/bolum2/haarcascade_frontalface.xml")

cap = cv2.VideoCapture(0)

while True:
    durum,cerceve=cap.read()
    gri=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    yuzler=yuz_bulucu.detectMultiScale(gri,1.1,27)
    for (x,y,w,h) in yuzler:
        yuz=cerceve[y:y+h,x:x+w]
        blurlu_yuz=cv2.GaussianBlur(yuz,(77,77),0.0)
        cerceve[y:y+h,x:x+w]=blurlu_yuz
        #cerceve[y:y+h,x:x+w]= cv2.GaussianBlur(cerceve[y:y+h,x:x+w],(37,37),0.0)
        cv2.rectangle(cerceve,(x,y),(x+w,y+h),(0,255,0),1)
    
    cv2.imshow("video",cerceve)
    
    if not(durum) or cv2.waitKey(50)==27:
        break

cap.release()
cv2.destroyAllWindows()
    


####### resim üzerinde #######################
# resim=cv2.imread("goruntu_isleme/bolum2/galatasaray.jpg")

# gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

# on_yuzler = yuz_bulucu.detectMultiScale(gri,1.1,5)

# for (x,y,w,h) in on_yuzler:
#     cv2.rectangle(resim,(x,y),(x+w,y+h),(0,255,0),1)
    




# cv2.imshow("yuz",resim)
# # cv2.imshow("gri",gri)
# cv2.waitKey(0)