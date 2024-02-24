import cv2

resim = cv2.imread("goruntu_isleme/bolum2/nature.jpg")

ortalama=cv2.blur(resim,(7,7))
ortanca=cv2.medianBlur(resim,7)
gauss=cv2.GaussianBlur(resim,(7,7),sigmaX=1.0)

cv2.imshow("orijinal",resim)
cv2.imshow("ortalama",ortalama)
cv2.imshow("ortanca",ortanca)
cv2.imshow("gauss",gauss)
cv2.waitKey(0)