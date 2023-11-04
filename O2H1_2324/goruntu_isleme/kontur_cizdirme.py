import cv2
import numpy as np

img = cv2.imread("goruntu_isleme/images/bolum2/rice_1.jpg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
filtreli=cv2.GaussianBlur(gri,(3,3),0)
canny=cv2.Canny(filtreli,100,170)

konturlar,hiyerarji = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,konturlar,-1,(0,0,255),1)
print(konturlar,len(konturlar))
cv2.imshow("orijinal",img)
cv2.imshow("gri",gri)
cv2.imshow("filtreli",filtreli)
cv2.imshow("canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()