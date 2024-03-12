import cv2
import numpy as np

yuz_bulucu = cv2.CascadeClassifier("goruntu_isleme/bolum2/haarcascade_frontalface.xml")

resim=cv2.imread("goruntu_isleme/bolum2/icardi.jpg")


cv2.imshow("yuz",resim)
cv2.waitKey(0)