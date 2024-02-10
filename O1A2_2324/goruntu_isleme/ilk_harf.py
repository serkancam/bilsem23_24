import numpy as np
import cv2

# tek kanallı/gri tonlamalı resim

h_harfi = [
    [255,0,255,255,255,255,0,255],
    [255,0,255,255,255,255,0,255],
    [255,0,255,255,255,255,0,255],
    [255,0,0,0,0,0,0,255],
    [255,0,0,0,0,0,0,255],
    [255,0,255,255,255,255,0,255],
    [255,0,255,255,255,255,0,255],
    [255,0,255,255,255,255,0,255]
    ]

h_resim = np.array(h_harfi,dtype=np.uint8)
cv2.imshow("h",h_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()