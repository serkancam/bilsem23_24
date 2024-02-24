import cv2

resim=cv2.imread("goruntu_isleme/bolum2/nature.jpg")

resim_ort=cv2.blur(resim,(7,7))
resim_medyan=cv2.medianBlur(resim,7)


cv2.imshow("ortalama",resim_ort)
cv2.imshow("ortanca",resim_medyan)
cv2.imshow("orijinal",resim)
cv2.waitKey(0)