import cv2
import numpy as np

img = cv2.imread("goruntu_isleme/images/bolum2/zebrasmall.png")

img_parca1 = img[10:200,200:300].copy()
img_parca2=img[10:155,25:140]

img_dikey = cv2.flip(img_parca2,0)# 0 dikey, 1 yatay -1 hem yatay hem dikey
img_yatay=cv2.flip(img_parca2,1)
img_yakey=cv2.flip(img_parca2,-1)
cv2.imshow("orijinal",img)
cv2.imshow("parca1",img_parca1)
cv2.imshow("parca2",img_parca2)
cv2.imshow("dikey",img_dikey)
cv2.imshow("yatay",img_yatay)
cv2.imshow("yakey",img_yakey)
cv2.waitKey(0)