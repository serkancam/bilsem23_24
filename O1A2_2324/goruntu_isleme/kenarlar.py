import cv2
import numpy as np

resim=cv2.imread("goruntu_isleme/bolum2/sudoku.jpg",cv2.IMREAD_GRAYSCALE)
print(resim.shape)

#sobelx
sobelx=cv2.Sobel(resim,cv2.CV_64F,1,0,ksize=3)
sobelx=np.uint8(np.absolute(sobelx))
#sobely
sobely=cv2.Sobel(resim,cv2.CV_64F,0,1,ksize=3)
sobely=np.uint8(np.absolute(sobely))

#laplace
laplas=cv2.Laplacian(resim,cv2.CV_64F)
laplas=np.uint8(np.absolute(laplas))
#canny
canny=cv2.Canny(resim,90,170)


#görseller
cv2.imshow("orijinal",resim)
cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobely)
cv2.imshow("sobelxy",sobelx+sobely)
cv2.imshow("laplas",laplas)
cv2.imshow("canny",canny)
cv2.waitKey(0)