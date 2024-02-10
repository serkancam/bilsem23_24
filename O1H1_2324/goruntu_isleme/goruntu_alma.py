import cv2 #opencv(open computer vision - açık bilgisayarlı görü)

resim = cv2.imread("/home/serkan/Belgeler/bilsem23_24/O1H1_2324/goruntu_isleme/bolum1/marsrover.png")

cv2.imshow("pencere",resim)

cv2.waitKey(0)