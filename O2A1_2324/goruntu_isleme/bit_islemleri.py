import cv2
import numpy as np

img1=cv2.imread("goruntu_isleme/images/bolum2/cat1.png")
img2=cv2.imread("goruntu_isleme/images/bolum2/cat2.png")

maske = np.full((500,470,3),fill_value=255,dtype=np.uint8)
cv2.imshow("maske",maske)
maske[:,:,2]=0
maske[:,:,1]=0
cv2.imshow("maske2",maske)

img_or = cv2.bitwise_or(img1,img2)
img_and =cv2.bitwise_and(img1,img2)
img_red_and = cv2.bitwise_and(img1,maske)

cv2.imshow("or",img_or)
cv2.imshow("and",img_and)
cv2.imshow("red_and",img_red_and)
cv2.waitKey(0)
