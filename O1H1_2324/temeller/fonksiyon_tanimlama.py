# fonksiyon_tanimlama.py

# fonksiyonlarla ilgili en önemli kelimeler tanımlama(definition) ve çağırma(call) kelimeleridir.
# bir sozcuk devamında () yaplıyorsa o sozcuk bir fonksiyondur.
# fonksiyonlar işlemek için değerler alabilirler bunlara argüman/parametre denir.

# tanımlanma durumuna göre fonskiyonlar
# a. built-in(dahili) fonksiyonlar
# b. 3. parti fonksiyonlar
# c. kullanıcı tanımlı fonksiyonlar.

#a. dahili fonksiyonlar

a=5
b=-12
c=-20

eb=max(a,c,b)
ek=min(c,b,a)
mutlak = abs(eb**2-ek**2-70)
toplam = sum([3,5,5,0.7,0.8,15])
print("mutlak:",mutlak)
print("toplam:",toplam)
# 0 ile 1000 arasındaki 5 e kalansız bölünen sayıların toplamı

#0 5 10 15 ... 1000
aralik=range(0,1001,5)
aralik_toplam=sum(aralik)
print("aralık toplam:",aralik_toplam)
print("aralık toplam2:",sum(range(0,1001,5)))


# b. 3. parti fonksiyonlar

import matplotlib.pyplot as plt
import numpy as np

