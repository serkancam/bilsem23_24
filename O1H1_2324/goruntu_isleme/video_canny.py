import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    durum,cerceve=cap.read()
    cv2.imshow("orijinal",cerceve)
    canny=cv2.Canny(cerceve,50,150)
    cv2.imshow("canny",canny)
    
    if not(durum) or cv2.waitKey(50)==27:
        break

cap.release()
cv2.destroyAllWindows()