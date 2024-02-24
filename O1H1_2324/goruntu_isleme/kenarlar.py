import cv2
import numpy as np

resim=cv2.imread("goruntu_isleme/bolum2/sudoku.jpg")

resim_gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

#ekler
resim_gri=cv2.medianBlur(resim_gri,3)
(t,resim_gri)=cv2.threshold(resim_gri,230,255,cv2.THRESH_BINARY)
resim_gri=resim_gri[30:-30,30:-30]
#sobelx
sobelx=cv2.Sobel(resim_gri,cv2.CV_64F,1,0,ksize=3)
sobelx=np.uint8(np.absolute(sobelx))

#sobely
sobely=cv2.Sobel(resim_gri,cv2.CV_64F,0,1,ksize=3)
sobely=np.uint8(np.absolute(sobely))
#sobelx+sobely

#canny
canny=cv2.Canny(resim_gri,50,150)

print(resim_gri)
cv2.imshow("orijinal",resim_gri)
cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobely)
cv2.imshow("sobelxy",sobelx+sobely)
cv2.imshow("canny",canny)
cv2.waitKey(0)