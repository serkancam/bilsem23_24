
import cv2

face_cascade = cv2.CascadeClassifier('goruntu_isleme/bolum2/haar/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('goruntu_isleme/bolum2/haar/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('goruntu_isleme/bolum2/haar/smile_cascade.xml')

def detect(gray_image, original_image):
    face = face_cascade.detectMultiScale(gray_image, 1.3, 5)
    for (x,y,w,h) in face:
        cv2.rectangle(original_image, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray_image[y:y+h,x:x+w]
        roi_color = original_image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (0,0,255), 2)
    return original_image
 
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video',canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows