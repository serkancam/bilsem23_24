# pirincler.py
import cv2
import numpy as np
img = cv2.imread("goruntu_isleme/images/bolum2/rice_1.jpg")

gri =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kenarlar=cv2.Canny(gri,170,250)

konturlar,hiyerarji=cv2.findContours(kenarlar,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(konturlar,len(konturlar))

cv2.drawContours(img,konturlar,-1,(0,0,255),1)
# cv2.imshow("sonuc",kenarlar),
cv2.imshow("img",img)
cv2.waitKey(0)
