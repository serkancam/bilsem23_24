import cv2
import numpy as np

siniflandirici=cv2.CascadeClassifier("goruntu_isleme/bolum2/haarcascade_eye_tree_eyeglasses.xml")


cerceve=cv2.imread("goruntu_isleme/bolum2/yuz.jpg")
gri=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
yuzler = siniflandirici.detectMultiScale(gri,1.1,5)
# yuzler değişkeninin verisi yüz tespit edilen bölgenin sol üst köşe noktasının
# x ve y koordinatını ve yüzün kapladğı genişlik(w) ve yükseklik(h) bilgisini içerir   
for (x,y,w,h) in yuzler:
    cv2.rectangle(cerceve,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("tespit",cerceve)
cv2.waitKey(0)
cv2.destroyAllWindows()