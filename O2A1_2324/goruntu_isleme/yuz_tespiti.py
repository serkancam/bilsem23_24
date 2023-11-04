import cv2

cap=cv2.VideoCapture("goruntu_isleme/images/ornek_video.mp4")
# cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier("goruntu_isleme/images/bolum2/haarcascade_frontalface.xml")

while True:
    state,frame=cap.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        piece = frame[y:y+h,x:x+w]
        blur_piece=cv2.medianBlur(piece,67)
        frame[y:y+h,x:x+w]=blur_piece
        
        
    
    cv2.imshow("video",frame)
    if cv2.waitKey(50)==27 or not(state):
        break 

cap.release()
cv2.destroyAllWindows()