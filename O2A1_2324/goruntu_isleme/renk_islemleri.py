import cv2 
import numpy as np

img =cv2.imread("goruntu_isleme/images/bolum2/nature.jpg") 

yuk,gen,kanal=img.shape

gri_1c = np.zeros((yuk,gen),dtype=np.uint8)
for satir in range(yuk):
    for sutun in range(gen):
        k = int(img[satir,sutun,2])
        m = int(img[satir,sutun,0])
        y = int(img[satir,sutun,1])
        ort= int((k+m+y)/3)
        gri_1c[satir,sutun]=ort

gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("orijinal",img)
cv2.imshow("gri1",gri_1c)
cv2.imshow("gri",gri)

cv2.waitKey(0)