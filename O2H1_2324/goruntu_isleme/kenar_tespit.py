import cv2 
import numpy as np

img = cv2.imread("goruntu_isleme/images/bolum2/sudoku.jpg")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gri,50,170)

cv2.imshow("orijinal",img)
cv2.imshow("canny",canny)

###kamera ve videodan görüntü okuma###

cap=cv2.VideoCapture(1) 
while True:
    durum,cerceve=cap.read()
    gri2=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    kenaralar=cv2.Canny(gri2,50,170)
    cv2.imshow("kamera",kenaralar)
    if cv2.waitKey(50)==27:
        break

cap.release()
cv2.destroyAllWindows()