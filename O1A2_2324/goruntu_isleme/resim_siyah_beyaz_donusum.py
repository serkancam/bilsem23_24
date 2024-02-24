# resim_siyah_beyaz_donusum.py
import cv2
import numpy as np 

#bu yöntem,  her zaman resmi bgr olarak okur
resim=cv2.imread(r"goruntu_isleme/bolum2/scanned_doc.png")
# bu yöntem, resmi orijinal renk uzayında okur
resim_orijinal=cv2.imread(r"goruntu_isleme/bolum2/scanned_doc.png",cv2.IMREAD_UNCHANGED)
print(resim.shape)

print(resim_orijinal.shape)
resim_gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
print(resim_gri.shape)
#statik eşikleme(siyah beyaz dönüşüm)
(T,sb_resim)=cv2.threshold(resim_gri,50,255,cv2.THRESH_BINARY)
(T,sb_resim_ters)=cv2.threshold(resim_gri,80,255,cv2.THRESH_BINARY_INV)
#beyaz pikseller azaltılır.
erozyon=cv2.erode(sb_resim,np.ones((3,3),np.uint8),iterations=1)
#dinamik eşikleme(otsu binarization)
cv2.imshow("orijinal",resim)
cv2.imshow("orijinal4kanl",resim_orijinal)
cv2.imshow("gri",resim_gri)
cv2.imshow("sb",sb_resim)
cv2.imshow("sb_ters",sb_resim_ters)
cv2.imshow("erozyon",erozyon)
cv2.waitKey(0)