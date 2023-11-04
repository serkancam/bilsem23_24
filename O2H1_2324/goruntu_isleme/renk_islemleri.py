import cv2
import numpy as np

img=cv2.imread("goruntu_isleme/images/bolum2/nature.jpg")

yuk,gen,kanal =img.shape

gri_resim = np.zeros((yuk,gen),dtype=np.uint8)
gri3=np.zeros((yuk,gen,kanal),dtype=np.uint8)
for x in range(yuk):
    for y in range(gen):
        b=int(img[x,y,0])
        g=int(img[x,y,1])
        r=int(img[x,y,2])
        ort = int((b+g+r)//3)
        gri_resim[x,y]=ort
        gri3[x,y]=[ort,ort,ort]
#*************#
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#*************#
cv2.imshow("orijinal",img)
cv2.imshow("gri_resim",gri_resim)
cv2.imshow("gri3",gri3)
cv2.imshow("gri",gri)

cv2.waitKey(0)