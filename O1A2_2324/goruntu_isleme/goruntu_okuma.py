# goruntu_okuma.py
import cv2 # opencv /open computer vision/açık bilgisayarlı görü
import numpy as np


resim = cv2.imread("/home/serkan/Belgeler/bilsem23_24/O1A2_2324/goruntu_isleme/bolum1/marsrover.png",cv2.IMREAD_UNCHANGED)

print(resim.shape) # opencv resimleri numpy ndarray(n dimension array/n boyutlu dizi)
satir,sutun,kanal=resim.shape

resim_gri=np.zeros((satir,sutun),dtype=np.uint8)
for x in range(satir):
    for y in range(sutun):
        r=int(resim[x,y,2])
        g=int(resim[x,y,1])
        b=int(resim[x,y,0])
        ort=(r+g+b)//3
        resim_gri[x,y]=ort


print(resim)
cv2.imshow("resim_penceresi",resim)
cv2.imshow("resim_gri",resim_gri)
cv2.waitKey(0)
