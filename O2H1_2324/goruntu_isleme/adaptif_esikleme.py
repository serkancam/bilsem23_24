#14 ekim 2023 buradan devam
import cv2 
import numpy as np

img= cv2.imread("goruntu_isleme/images/bolum2/boat.jpg")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

t,statik=cv2.threshold(gri,80,255,cv2.THRESH_BINARY)
dinamik=cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,3)
t,otsu = cv2.threshold(gri,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("orijinal",img)
cv2.imshow("gri",gri)
cv2.imshow("statik",statik)
cv2.imshow("dinamik",dinamik)
cv2.imshow("otsu",otsu)
cv2.waitKey(0)