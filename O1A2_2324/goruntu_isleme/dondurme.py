import cv2
import numpy as np 

"""
yazdığınız kodlar ile zebra.png resmini zebrasmall.png resmi boyutuna küçültünüz. Bu işlemi yaparken tüm bilgileri python kodu ile elde ediniz.,
küçük haldeki resmi imshow ile gösteriniz.
"""
zebra=cv2.imread("goruntu_isleme/bolum2/zebra.png")
zebra_kucuk=cv2.imread("goruntu_isleme/bolum2/zebrasmall.png")
h,w,c=zebra_kucuk.shape

zebra_son=cv2.resize(zebra,(w,h))
zebra_son_yatay=cv2.flip(zebra_son,1) # 0 dikey 1 yatay -1 yatay ve dikey

# resim döndürme(rotasyon)
dm=(w//2,h//2)
aci=30
olcek=1.0
dondurme_matrisi=cv2.getRotationMatrix2D(dm,aci,olcek)
donmus_resim=cv2.warpAffine(zebra_son,dondurme_matrisi,(w,h))
print(zebra_kucuk.shape,zebra_son.shape)
cv2.imshow("sonuc",zebra_son)
cv2.imshow("yatay",zebra_son_yatay)
cv2.imshow("donmus_resim",donmus_resim)
cv2.waitKey(0)