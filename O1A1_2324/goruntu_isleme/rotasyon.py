import cv2 
import numpy as np 

resim = cv2.imread("/home/serkan/Belgeler/bilsem23_24/O1A1_2324/goruntu_isleme/bolum2/zebrasmall.png")

# döndürme matrisi
dondurme_matrisi=cv2.getRotationMatrix2D((0,0),-45,1.0)

donmus_resim=cv2.warpAffine(resim,dondurme_matrisi,(resim.shape[1],resim.shape[0]))
cv2.imshow("orijinal",resim)
cv2.imshow("donmus_resim",donmus_resim)
cv2.waitKey(0)