import cv2
import numpy as np 

resim=cv2.imread("goruntu_isleme/bolum2/zebrasmall.png")


h,w,c=resim.shape

aci=0
while True:
    merkez=(w//2,h//2)
    aci += 30
    olcek=1.0

    dondurme_matris=cv2.getRotationMatrix2D(merkez,aci,olcek)
    donmus_resim=cv2.warpAffine(resim,dondurme_matris,(w,h))

    cv2.imshow("donmus",donmus_resim)


    if cv2.waitKey(50)==27:# 27 escape tuşu ascii kodudur.
        break
    
cv2.destroyAllWindows()
