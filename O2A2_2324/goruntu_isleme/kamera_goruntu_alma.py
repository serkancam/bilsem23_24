import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    durum,cerceve = cap.read()
    gri=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    t,sb=cv2.threshold(gri,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow("kamera",sb)
    if cv2.waitKey(50)==27:
        break

cap.release()
cv2.destroyAllWindows()