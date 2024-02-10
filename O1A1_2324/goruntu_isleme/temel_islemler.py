import numpy as np
import cv2

resim = cv2.imread("/home/serkan/Belgeler/bilsem23_24/O1A1_2324/goruntu_isleme/bolum1/marsrover.png")

yuk,gen,kanal=resim.shape
print(gen,yuk,kanal)

parca1=resim[0:50,0:50]
parca2=resim[240:255,220:240]

cv2.rectangle(resim,(232,316),(335,345),(0,255,0),1)

cv2.imshow("orijinal",resim)
cv2.imshow("p1",parca1)
cv2.imshow("p2",parca2)

cv2.waitKey(0)
cv2.destroyAllWindows()