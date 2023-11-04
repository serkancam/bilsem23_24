import cv2
import numpy as np

img=cv2.imread("goruntu_isleme/images/bolum2/salt-pepper.jpg")

filtreli = cv2.medianBlur(img,5)
cv2.imshow("orjinal",img)
cv2.imshow("filtreli",filtreli)

cv2.waitKey(0)
