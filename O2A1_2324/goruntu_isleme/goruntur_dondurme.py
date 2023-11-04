# goruntu_dondurme.py
import cv2

img = cv2.imread("goruntu_isleme/images/bolum2/cat2.png")

h,w,c = img.shape

#degerler
center = (w//2,h//2)
angle = 0 # + saat yönü tersi, - saat yönü
scale=1.0
while True:
    # döndürme matrisi(rotation matrix)
    rotation_matrix = cv2.getRotationMatrix2D(center,angle,scale)
    print(rotation_matrix)
    # döndürme matrisine göre görüntüyü döndür

    rotated_img = cv2.warpAffine(img,rotation_matrix,(w,h))
    cv2.imshow("donmus_resim",rotated_img)
    angle=angle+5
    if scale<0.1:
        scale=1.0
    scale=scale*0.95
    if cv2.waitKey(50)==27:# 27 escape tuşunun ascii kodu
        break