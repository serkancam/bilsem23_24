import cv2

img=cv2.imread("goruntu_isleme/images/bolum2/park.jpg")

print(cv2.__version__)
img_k33=cv2.blur(img,ksize=(7,7))
img_g33=cv2.GaussianBlur(img,ksize=(7,7),sigmaX=0)
cv2.imshow("orijinal",img)
cv2.imshow("img_k33",img_k33)
cv2.imshow("img_g33",img_g33)

cv2.waitKey(0)