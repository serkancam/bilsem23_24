import cv2
import numpy as np

resim = cv2.imread("goruntu_isleme/images/bolum2/sudoku.jpg")
#####################
filtreli_gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
filtreli=cv2.GaussianBlur(filtreli_gri,(3,3),0)

kenarlar_filtreli=cv2.Canny(filtreli,60,80)
##################
gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY) 
kenarlar=cv2.Canny(gri,50,170)
#############

cv2.imshow("orijinal",resim)
cv2.imshow("gri",gri)
cv2.imshow("kenarlar",kenarlar)
cv2.imshow("filtrel_gri",kenarlar_filtreli)
cv2.waitKey(0)