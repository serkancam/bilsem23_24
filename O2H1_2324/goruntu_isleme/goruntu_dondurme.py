import cv2
import numpy as np

img = cv2.imread("goruntu_isleme/images/bolum2/zebrasmall.png")
yuk,gen,kanal = img.shape

# döndürme matrisi(rotation matrix)
merkez = (20,200)
aci = 0
olcek=1.0
while True:
    dondurme_matrisi = cv2.getRotationMatrix2D(merkez,aci,olcek)
    # bu matrise göre resmin dönmüş halini elde edelim
    donmus=cv2.warpAffine(img,dondurme_matrisi,(gen,yuk))
    aci=aci+5
    cv2.imshow("orijinal",img)
    cv2.imshow("donmus",donmus)
    tus=cv2.waitKey(50)
    if tus==27:
        break