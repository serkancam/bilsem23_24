# siyah_beyaz_donusum.py

import cv2
import numpy as np

# bu yöntem ile resim her zaman 3 kanallı bgr olak okunur
resim =cv2.imread("goruntu_isleme/bolum2/scanned_doc.png")
#BU YÖNTEM İLE RESİM HER ZAMAN ORJİNAL HALİ İLE OKUNUR
resim_orijinal=cv2.imread("goruntu_isleme/bolum2/scanned_doc.png",cv2.IMREAD_UNCHANGED)
print(resim.shape)
print(resim_orijinal.shape)

resim_gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
print(resim_gri.shape)
#statik eşikleme
(esik,resim_sb)=cv2.threshold(resim_gri,20,255,cv2.THRESH_BINARY)
(esik,otsu)=cv2.threshold(resim_gri,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#gösterimler
cv2.imshow("orijinal",resim)
cv2.imshow("gri",resim_gri)
cv2.imshow("resim_sb",resim_sb)
cv2.imshow("otsu",otsu)
cv2.waitKey(0)
