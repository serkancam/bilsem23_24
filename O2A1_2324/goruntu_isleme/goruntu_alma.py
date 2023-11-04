import cv2
import numpy as np

goruntu = cv2.imread("goruntu_isleme/images/bolum1/marsrover.png")

print(goruntu.shape)
parca = goruntu[70:360,100:330].copy()
cv2.rectangle(goruntu,(100,70),(330,360),(0,255,255),2)
cv2.circle(goruntu,(100,70),30,(0,0,255),2)
cv2.circle(goruntu,(330,70),30,(0,255,0),-1)
cv2.circle(goruntu,(330,360),30,(255,0,0),2)
cv2.line(goruntu,(100,70),(330,360),(200,78,222),5)

cv2.imshow("g",goruntu)
cv2.imshow("p",parca)

cv2.waitKey(0)
