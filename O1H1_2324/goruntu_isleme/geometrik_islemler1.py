# resim boyutlandırma
import cv2

resim = cv2.imread("goruntu_isleme/bolum2/zebrasmall.png")
h,w,c=resim.shape

# en boy oranı(ratio)
ebo=w/h
h_yeni=200
w_yeni=int(ebo*h_yeni)
resim_k1=cv2.resize(resim,(100,150))
resim_k2=cv2.resize(resim,(w_yeni,h_yeni))
resim_b1=cv2.resize(resim,(1920,1080))


print(resim.shape)
cv2.imshow("orijinal",resim)
cv2.imshow("kucuk1",resim_k1)
cv2.imshow("kucuk2",resim_k2)
cv2.imshow("resim_buyuk",resim_b1)

cv2.waitKey(0)