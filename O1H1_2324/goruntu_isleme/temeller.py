import cv2
import numpy as np

rover_img = cv2.imread("/home/serkan/Belgeler/bilsem23_24/O1H1_2324/goruntu_isleme/bolum1/marsrover.png")
#x aralığı 195:225(x sütunlar)
#y aralığı 155:175(y satırlar)

# aralık belirtirken [satırlar,sütunlar]
parca1=rover_img[155:175,195:225]
parca2=rover_img[239:254,219:240]

# usa yazısı için dörtgen 1 p1(x:230,y:140),p2(x:250,y:150)
cv2.rectangle(rover_img,[230,140],[250,150],[0,255,0],1)
# AL yazısı için dörtgen  p1(x:,y:),p2(x:,y:)

cv2.imshow("p1",parca1)
cv2.imshow("p2",parca2)
cv2.imshow("orijinal",rover_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
