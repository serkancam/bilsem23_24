import cv2

img=cv2.imread("goruntu_isleme/images/bolum2/scanned_doc.png",-1)

print(img.max())

gri =  cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
esik,sb1 = cv2.threshold(gri,50,255,cv2.THRESH_BINARY)
sb1_d = cv2.erode(sb1,(3,3),iterations=2)
cv2.imshow("orijinal",img)
cv2.imshow("gri",gri)
cv2.imshow("sb1",sb1)
cv2.imshow("sb1_d",sb1_d)
cv2.waitKey(0)