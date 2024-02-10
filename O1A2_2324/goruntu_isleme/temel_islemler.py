# goruntu_okuma.py
import cv2 # opencv /open computer vision/açık bilgisayarlı görü
import numpy as np


resim = cv2.imread("/home/serkan/Belgeler/bilsem23_24/O1A2_2324/goruntu_isleme/bolum1/marsrover.png")
# x--> 220:240 //sütunlar
# y--> 240:255 //satırlar
print(resim.shape) # opencv resimleri numpy ndarray(n dimension array/n boyutlu dizi)
satir,sutun,kanal=resim.shape
parca1=resim[240:255,220:240]

cv2.imshow("orjinal",resim)
cv2.imshow("parca1",parca1)
cv2.waitKey(0)
cv2.destroyAllWindows()