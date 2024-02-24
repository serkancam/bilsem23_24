import cv2

cap=cv2.VideoCapture(0)

while True:
    durum,cerceve=cap.read()
    
    
    canny=cv2.Canny(cerceve,50,170)
    cv2.imshow("resim",canny)
    if not(durum) or cv2.waitKey(50)==27:
        break
    
    
cap.release()
cv2.destroyAllWindows()
    