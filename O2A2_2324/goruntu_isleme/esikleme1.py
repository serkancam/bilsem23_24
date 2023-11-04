import cv2

img=cv2.imread("goruntu_isleme/images/bolum2/scanned_doc.png")
yuk,gen,kanal=img.shape

if kanal>1:
    pass
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

(thresh1,sb_img)=cv2.threshold(gri,60,255,cv2.THRESH_BINARY)
(thresh2,sb_otsu)=cv2.threshold(gri,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
dilate_img=cv2.dilate(sb_img,(3,3),iterations=2)
erode_img =cv2.erode(sb_img,(3,3),iterations=2)
cv2.imshow("orjinal",img)
cv2.imshow("gri",gri)
cv2.imshow("sb",sb_img)
cv2.imshow("sb_otsu",sb_otsu)
cv2.imshow("erode_img",erode_img)

cv2.waitKey(0)
