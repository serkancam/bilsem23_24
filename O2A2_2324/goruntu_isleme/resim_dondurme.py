import cv2 
import numpy as np

img = cv2.imread("goruntu_isleme/images/bolum2/zebrasmall.png")

img_yatay =  cv2.flip(img,0)
img_dikey = cv2.flip(img,1)
img_yakey = cv2.flip(img,-1)
# görüntü döndürme



# cv2.imshow("orijinal",img)
# cv2.imshow("yatay",img_yatay)
# cv2.imshow("dikey",img_dikey)
# cv2.imshow("yakey",img_yakey)

h,w,c= img.shape
aci=0
olcek=1.0
merkez=(w//2,h//2)

while True:
    dondurme_matrisi=cv2.getRotationMatrix2D(merkez,aci,olcek)

    img_donmus = cv2.warpAffine(img,dondurme_matrisi,(w,h))

    cv2.imshow("donmus",img_donmus)
    aci-=15
    olcek*=0.9
    if olcek<0.1:
        olcek=1.0
    if cv2.waitKey(50)==27:
        break


cv2.destroyAllWindows()