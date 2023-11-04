import cv2
import numpy as np


img =  cv2.imread("goruntu_isleme/images/bolum2/zebrasmall.png")

print(cv2.__version__)

dikey=cv2.flip(img,0) # 0 dikey, 1 yatay, -1 her iki yönde de
yatay =cv2.flip(img,1)

y,g,k = img.shape 
print(y,g,k)
ebo = g/y

yeni_g =200
yeni_y=int(yeni_g/ebo)

r1 = cv2.resize(img,(100,200),interpolation=cv2.INTER_AREA)
r2 = cv2.resize(img,(yeni_g,yeni_y))
r3=cv2.resize(img,None,fx=1.5,fy=1.8)
cv2.imshow("orijinal",img)
cv2.imshow("dikey",dikey)
cv2.imshow("yatay",yatay)
cv2.imshow("r1",r1)
cv2.imshow("r2",r2)
cv2.imshow("r3",r3)
cv2.waitKey(0)


