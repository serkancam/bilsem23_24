import cv2
import numpy as np


resim=cv2.imread("goruntu_isleme/bolum2/rice_1.jpg")
resim_gri =cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
filtreli=cv2.GaussianBlur(resim_gri,(3,3),0.0)
kenarlar=cv2.Canny(filtreli,100,170)

#konturları bul
konturlar,h=cv2.findContours(kenarlar,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(konturlar))

#konturları çizdir
cv2.drawContours(resim,konturlar,-1,(0,255,0),1)

k2=cv2.cvtColor(kenarlar,cv2.COLOR_GRAY2BGR)
cv2.drawContours(k2,konturlar,-1,(0,255,0),1)


cv2.imshow("orijinal",resim_gri)
cv2.imshow("canny",kenarlar)
cv2.imshow("bitti",resim)
cv2.imshow("k2",k2)
cv2.waitKey(0)