import cv2
import numpy as np

resim = [[255,0,255,255,255,255,0,255],
         [255,0,255,255,255,255,0,255],
         [255,0,255,255,255,255,0,255],
         [255,0,0,0,0,0,0,255],
         [255,000,0,0,0,0,0,255],
         [255,0,255,255,255,255,0,255],
         [255,0,255,255,255,255,0,255],
         [255,0,255,255,255,255,0,255]
         ]
print(type(resim))

resim3 = [[[255,0,0],[0,255,0]],
          [[0,0,255],[255,255,0]]
            ]

# opencv resimleri numpy uint8 biçiminde ister

rsm = np.array(resim,dtype=np.uint8)
rsm3 =np.array(resim3,dtype=np.uint8)

resim_s = [
    [0,0,0,0,0,0,0,0],
    [0,255,255,255,255,255,255,0],
    [0,255,0,0,0,0,0,0],
    [0,255,0,0,0,0,0,0],
    [0,255,255,255,255,255,255,0],
    [0,0,0,0,0,0,255,0],
    [0,0,0,0,0,0,255,0],
    [0,255,255,255,255,255,255,0],
    [0,0,0,0,0,0,0,0]
    ]
resim_sn = np.array(resim_s,np.uint8)
cv2.imshow("harf",rsm)
cv2.imshow("isim",resim_sn)
cv2.imshow("renkli",rsm3)
cv2.waitKey(0)
