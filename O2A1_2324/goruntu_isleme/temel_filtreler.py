#temel_filtreler.py

import cv2
import numpy as np


img = cv2.imread("goruntu_isleme/images/bolum2/nature.jpg")

ort_55 = cv2.blur(img,(5,5))
gaus_55=cv2.GaussianBlur(img,(5,5),0)
median_55=cv2.medianBlur(img,5)

cv2.imshow("orijinal",img)
cv2.imshow("gaus",gaus_55)
cv2.imshow("median",median_55)
cv2.imshow("ortalama",ort_55)

cv2.waitKey(0)