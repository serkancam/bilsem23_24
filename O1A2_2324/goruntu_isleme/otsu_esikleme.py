import cv2
import numpy as np

resim=cv2.imread("goruntu_isleme/bolum2/scanned_doc.png")

resim_gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

resim_gri_medyan=cv2.blur(resim_gri,(3,3))

#dinamik eşikleme(otsu)
(_,resim_sb1)=cv2.threshold(resim_gri,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
(_,resim_sb2)=cv2.threshold(resim_gri_medyan,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#adaptive eşikleme
adaptif=cv2.adaptiveThreshold(resim_gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,21)

cv2.imshow("gri",resim_gri)
cv2.imshow("medyanFilter",resim_gri_medyan)
cv2.imshow("sb1",resim_sb1)
cv2.imshow("sb2",resim_sb2)
cv2.imshow("adaptif",adaptif)

cv2.waitKey(0)