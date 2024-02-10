import cv2
import numpy as np

resim=cv2.imread("/home/serkan/Belgeler/bilsem23_24/O1A1_2324/goruntu_isleme/bolum1/marsrover.png")
print(resim.shape)
# print(resim)
resim_gri=np.zeros((400,640),dtype=np.uint8)
for x in range(400):
    for y in range(640):
        r=int(resim[x,y,0])
        g=int(resim[x,y,1])
        b=int(resim[x,y,2])
        px=int((r+g+b)//3)
        resim_gri[x,y]=px
      
cv2.imshow("resim_penceresi",resim)
cv2.imshow("resim_gri",resim_gri)
cv2.waitKey(0)