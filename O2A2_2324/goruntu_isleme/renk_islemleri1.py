#renk_islemleri1.py

import cv2
import numpy as np

img = cv2.imread("goruntu_isleme/images/bolum2/nature.jpg")

h,w,c =img.shape
print(h,w,c)

gray_1channel =np.zeros((h,w),dtype=np.uint8) 
gray_3channel =np.zeros((h,w,c),dtype=np.uint8)

gray_cv2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
for x in range(w):
    for y in range(h):       
       b,g,r=img[y,x]     
       ort=(int(b)+int(g)+int(r))//3
       gray_1channel[y,x]=ort
       gray_3channel[y,x]=ort

cv2.imshow("orijinal",img)
cv2.imshow("gray1",gray_1channel)
cv2.imshow("gray3",gray_3channel)
cv2.imshow("cv2_gray",gray_cv2)
# # img[:,:,2]=0
no_red = img.copy()
no_red[:,:,2]=0

# cv2.imshow("no_red",no_red)
cv2.waitKey(0)