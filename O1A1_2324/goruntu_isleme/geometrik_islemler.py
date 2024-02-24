import cv2

resim=cv2.imread("/home/serkan/Belgeler/bilsem23_24/O1A1_2324/goruntu_isleme/bolum2/zebra.png")

kucuk_r1 = cv2.resize(resim,(100,100))
buyuk_r1=cv2.resize(resim,(1200,1200))
kucuk_r1_yatay=cv2.flip(kucuk_r1,0)
kucuk_r1_dikey=cv2.flip(kucuk_r1,1)
cv2.imshow("orijinal",resim)
cv2.imshow("kucuk_r1",kucuk_r1)
cv2.imshow("resim_buyuk",buyuk_r1)
cv2.imshow("kucuk_flip_yatay",kucuk_r1_yatay)
cv2.imshow("kucuk_flip_dikey",kucuk_r1_dikey)
cv2.waitKey(0)