import cv2
import numpy as np 


resim = cv2.imread("/home/serkan/Belgeler/bilsem23_24/O1A1_2324/goruntu_isleme/bolum2/nature.jpg")

filtre_ortalama = cv2.blur(resim,(5,5))
filtre_ortanca =cv2.medianBlur(resim,5)
filtre_gauss=cv2.GaussianBlur(resim,(5,5),0.0)
kucuk=resim[::2,::2]



cv2.imshow("orijinal",resim)
cv2.imshow("ortalama",filtre_ortalama)
cv2.imshow("ortanca",filtre_ortanca)
cv2.imshow("gauss",filtre_gauss)
cv2.imshow("kucuk",kucuk)
cv2.waitKey(0)