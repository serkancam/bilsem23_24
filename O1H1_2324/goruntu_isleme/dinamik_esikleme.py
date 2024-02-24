# dinamik_esikleme.py

import cv2
import numpy as np 

resim=cv2.imread("goruntu_isleme/bolum2/receipt.jpg")

resim=cv2.resize(resim,dsize=(None,None),fx=0.4,fy=0.4)

resim_gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

#adaptif eşikleme
resim_adaptif=cv2.adaptiveThreshold(resim_gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51,61)
resim_adaptif_inv=cv2.adaptiveThreshold(resim_gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,51,61)

cv2.imshow("resim_sb",resim_adaptif)
cv2.imshow("resim_sb_inv",resim_adaptif_inv)
cv2.waitKey(0)