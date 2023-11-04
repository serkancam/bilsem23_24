import cv2 
import numpy as np

resim= cv2.imread("goruntu_isleme/images/bolum1/marsrover.png")


# rgb olabilir ama opencv bgr olarka okur resmi
p1=(100,70)
p2=(330,360)
h,w,c = resim.shape
print(h,w,c)
cv2.circle(resim,p1,30,(0,0,255),-1)
cv2.rectangle(resim,p1,p2,(0,255,255),2)
cv2.line(resim,(0,400),(640,0),(255,0,0),2)

print(cv2.__version__)
resimc =  resim.copy()

cv2.flip(resimc,1,resimc) # -1 0 1

cv2.imshow("rover",resim)
cv2.imshow("rover_ters",resimc)

cv2.waitKey(0)
cv2.destroyAllWindows()