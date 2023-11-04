# hareket_algilama.py

import cv2
import numpy as np

yakalama=cv2.VideoCapture("goruntu_isleme/images/hareket3.mp4")

d1,eski_resim=yakalama.read()
d2,yeni_resim=yakalama.read()

while True:
    fark_resmi=cv2.absdiff(yeni_resim,eski_resim)
    cv2.imshow("video",fark_resmi)
    
    eski_resim=yeni_resim
    durum,yeni_resim=yakalama.read()
    
    if cv2.waitKey(50)==27 or not(durum):
        break

yakalama.release()
cv2.destroyAllWindows()
    