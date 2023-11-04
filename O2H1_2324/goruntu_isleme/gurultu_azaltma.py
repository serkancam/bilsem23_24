import cv2

img=cv2.imread("goruntu_isleme/images/bolum2/salt-pepper.jpg",cv2.IMREAD_UNCHANGED)

print(cv2.IMREAD_UNCHANGED)

ortalama=cv2.blur(img,(5,5))
gauss=cv2.GaussianBlur(img,(5,5),0.0)
ortanca = cv2.medianBlur(img,5)

gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gri_ortanca = cv2.medianBlur(gri,5)

cv2.imshow("orijinal",img)
cv2.imshow("ortalama",ortalama)
cv2.imshow("gauss",gauss)
cv2.imshow("ortanca",ortanca)
cv2.imshow("gri_ortanca",gri_ortanca)
cv2.waitKey(0)