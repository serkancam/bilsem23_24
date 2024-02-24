import cv2
import numpy as np 


zebra_kucuk=cv2.imread("goruntu_isleme/bolum2/zebrasmall.png")
h,w,c=zebra_kucuk.shape
aci=0
while True:
    dm=(w//2,h//2)
    aci+=30
    olcek=1.0
    dondurme_matrisi=cv2.getRotationMatrix2D(dm,aci,olcek)
    donmus_resim=cv2.warpAffine(zebra_kucuk,dondurme_matrisi,(w,h))
    cv2.imshow("animasyon",donmus_resim)
    if cv2.waitKey(50)==27:#27 escape tuş kodu
        break

cv2.destroyAllWindows()