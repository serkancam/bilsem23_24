import cv2
import numpy as np 

resim=cv2.imread("goruntu_isleme/bolum2/sudoku.jpg")

resim_gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
sobelx= cv2.Sobel(resim_gri,cv2.CV_64F,1,0,ksize=3)
sobely= cv2.Sobel(resim_gri,cv2.CV_64F,0,1,ksize=3)

sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))

canny=cv2.Canny(resim,50,170)
cv2.imshow("orijinal",resim)
cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobely)
cv2.imshow("canny",canny)
cv2.waitKey(0)
