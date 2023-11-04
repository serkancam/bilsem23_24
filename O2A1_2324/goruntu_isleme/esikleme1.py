# esikleme1.py

import cv2
import numpy as np

img=cv2.imread("goruntu_isleme/images/bolum2/scanned_doc.png")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

fgri = cv2.GaussianBlur(gri,(3,3),0)

esik,sb_resim = cv2.threshold(gri,60,255,cv2.THRESH_BINARY)
esik,sb_resim_i = cv2.threshold(gri,60,255,cv2.THRESH_BINARY_INV)
# otsu binarization 
esik,sb_otsu =cv2.threshold(gri,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("orijinal",img)
cv2.imshow("gri",gri)
cv2.imshow("sb",sb_resim)
cv2.imshow("sbi",sb_resim_i)
cv2.imshow("otsu",sb_otsu)
cv2.waitKey(0)