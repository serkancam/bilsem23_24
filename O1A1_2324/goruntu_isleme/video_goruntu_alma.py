import cv2 
import numpy 

cap = cv2.VideoCapture(0)

while True:
    durum,cerceve= cap.read()
    canny=cv2.Canny(cerceve,50,170)
    
    cv2.imshow("orjinal",cerceve)
    cv2.imshow("kenar",canny)
    if not(durum) or cv2.waitKey(50)==27:
        break

cv2.destroyAllWindows()
