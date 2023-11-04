import cv2
import numpy as np

img = cv2.imread("goruntu_isleme/images/bolum2/nature.jpg")

img_kopya1 =img.copy()
img_kopya1[:,:,2]=0

img_kopya2=img.copy()
img_kopya2[:,:,0:2]=0

cv2.imshow("orijinal",img)
cv2.imshow("kopya1",img_kopya1)
cv2.imshow("kopya2",img_kopya2)
cv2.waitKey(0)