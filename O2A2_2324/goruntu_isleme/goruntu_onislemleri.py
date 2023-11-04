import cv2
import numpy as np


img =  cv2.imread("goruntu_isleme/images/bolum2/zebrasmall.png")

print(img.shape)
h,w,c = img.shape

img_r1 =  cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA)
img_r2 =cv2.resize(img,None,fx=0.4,fy=0.4)

# orjinal resmin genişliği 100 piksel olsun ama 
# resim en/boy oranı(aspect ratio) değişmesin

r = h/w
w_yeni=100
h_yeni=int(w_yeni*r)
img_r3 = cv2.resize(img,(w_yeni,h_yeni))

img_parca = img[10:150,30:135].copy()

cv2.imshow("normal",img)
cv2.imshow("img_r1",img_r1)
cv2.imshow("img_r2",img_r2)
cv2.imshow("img_r3",img_r3)
cv2.imshow("parca",img_parca)


cv2.waitKey(0)
cv2.destroyAllWindows()