import cv2

resim=cv2.imread("goruntu_isleme/bolum2/zebrasmall.png")
resim_yatay=cv2.flip(resim,1)#1 kodu yatay, 0 kodu dikey, -1 kodu yatay ve dikey 
resim_dikey=cv2.flip(resim,0)
resim_yakey=cv2.flip(resim,-1)
cv2.imshow("orijinal",resim)
cv2.imshow("yatay",resim_yatay)
cv2.imshow("dikey",resim_dikey)
cv2.imshow("yakey",resim_yakey)
cv2.waitKey(0)