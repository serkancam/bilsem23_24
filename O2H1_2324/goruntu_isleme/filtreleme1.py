import cv2

img = cv2.imread("goruntu_isleme/images/bolum2/park.jpg")
img2= cv2.imread("goruntu_isleme/images/bolum2/nature.jpg")

img_ort33=cv2.blur(img,(7,7))

img_gauss33=cv2.GaussianBlur(img,(7,7),0.0)

img_ortanca33 = cv2.medianBlur(img,7)
img2_ortanca77=cv2.medianBlur(img2,7)

cv2.imshow("orijinal",img)
cv2.imshow("ortalama",img_ort33)
cv2.imshow("gaussian",img_gauss33)
cv2.imshow("ortanca",img_ortanca33)
cv2.imshow("img2ortanca",img2_ortanca77)
cv2.waitKey(0)