import cv2
import numpy as np


zebra = cv2.imread("goruntu_isleme/images/bolum2/zebra.png")

zebra_k =  cv2.resize(zebra,(300,300),interpolation=cv2.INTER_AREA)

cv2.imshow("zebra",zebra)

cv2.imshow("zebra_kucuk",zebra_k)

cv2.waitKey(0)
cv2.destroyAllWindows()