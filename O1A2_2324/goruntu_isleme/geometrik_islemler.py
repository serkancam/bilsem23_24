import cv2
import numpy as np


"""
Geometrik işlemler:
Resmi; küçültme, büyütme, ayna görüntüsü alma ve döndürme işlemlerine denir.(belli bir parçasını alma)
"""

resim = cv2.imread("goruntu_isleme/bolum2/zebrasmall.png")

h,w,c=resim.shape
print(f"resim {h} yükseklik {w} genişliktedir ve {h*w} pikseldir.")

en_boy=w/h
h_yeni=200
w_yeni=int(h_yeni*en_boy)

resim_k1=cv2.resize(resim,(w_yeni,h_yeni))
resim_k2=cv2.resize(resim,(250,250))
resim_b1=cv2.resize(resim,(800,600))
resim_b2=cv2.resize(resim,dsize=(None,None),fx=1.2,fy=1.2)
cv2.imshow("orijinal",resim)
cv2.imshow("kucuk1",resim_k1)
cv2.imshow("kucuk2",resim_k2)
cv2.imshow("buyuk1",resim_b1)
cv2.imshow("buyuk2",resim_b2)

cv2.waitKey(0)