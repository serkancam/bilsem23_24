import cv2
import numpy as np 


resim = cv2.imread("/home/serkan/Belgeler/bilsem23_24/O1A1_2324/goruntu_isleme/bolum2/salt-pepper.jpg")

resim2=cv2.imread("/home/serkan/Belgeler/bilsem23_24/O1A1_2324/goruntu_isleme/bolum2/scanned_doc.png")

filtre1 = cv2.medianBlur(resim,3)#kernel/çkeirdek tek sayı seçilir
filtre2=cv2.medianBlur(resim2,5)
print(resim.shape)
print(resim)

cv2.imshow("orjinal",resim)
cv2.imshow("filteli_resim_1",filtre1)
cv2.imshow("orjinal2",resim2)
cv2.imshow("filteli_resim_2",filtre2)
cv2.waitKey(0)