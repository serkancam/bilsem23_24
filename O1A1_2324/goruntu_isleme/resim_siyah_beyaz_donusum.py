# resim_siyah_beyaz_donusum.py
import cv2
import numpy as np

resim = cv2.imread("goruntu_isleme/bolum2/scanned_doc.png")
resim_orj = cv2.imread("goruntu_isleme/bolum2/scanned_doc.png",cv2.IMREAD_UNCHANGED)
print(resim_orj.shape)
print(resim.shape)
# bgr2gray
resim_gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

#gri resim eşikleme(binarization)
(T,resim_sb)=cv2.threshold(resim_gri,75,255,cv2.THRESH_BINARY)
(T,resim_bs)=cv2.threshold(resim_gri,75,255,cv2.THRESH_BINARY_INV)
#otsu binarization
(T,resim_otsu)=cv2.threshold(resim_gri,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#resimleri göster
cv2.imshow("orjinal",resim)
cv2.imshow("gri",resim_gri)
cv2.imshow("sb",resim_sb)
cv2.imshow("bs",resim_bs)
cv2.imshow("otsu",resim_otsu)
cv2.waitKey(0)