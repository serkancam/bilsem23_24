import cv2
import keras
import matplotlib.pyplot as plt
import numpy as np

# model=keras.models.load_model("/home/serkan/Belgeler/bilsem23_24/O2H1_2324/ML/mnist_duz.h5")

img = cv2.imread("/home/serkan/Belgeler/bilsem23_24/O2H1_2324/ML/rakam6.png",cv2.IMREAD_UNCHANGED)
print(img.shape)
img=cv2.GaussianBlur(img,(11,11),cv2.BORDER_DEFAULT)
img=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
img=cv2.resize(img,(28,28),interpolation=cv2.INTER_LINEAR)
# 
img[img<25]=0
# plt.imshow(img,cmap="gray")
# plt.show()
tahmin2=model.predict(img.reshape(1,28,28))
print(np.argmax(tahmin2))
np.set_printoptions(linewidth=300)
print(img)
# for i in range(10):
#     print(f"{i} olma ihtimali tahmin:{tahmin2[0,i]}")