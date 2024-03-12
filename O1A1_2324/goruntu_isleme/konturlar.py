import cv2
import numpy as np

resim=cv2.imread("goruntu_isleme/bolum2/rice_1.jpg")

resim_gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
resim_filtre=cv2.GaussianBlur(resim_gri,(7,7),0)
kenarlar=cv2.Canny(resim_filtre,100,170)


# kontur koordinatalarını bul
konturlar,hiyerarsi=cv2.findContours(kenarlar,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(konturlar))
#bulunan koordinatlara çizgi çiz
cv2.drawContours(resim,konturlar,-1,(0,255,0),1)

cv2.imshow("orijinal",resim)
cv2.imshow("gri",resim_gri)
cv2.imshow("kenarlar",kenarlar)
cv2.imwrite("goruntu_isleme/bolum2/rice_1_sonuc.jpg",resim)
cv2.waitKey(0)