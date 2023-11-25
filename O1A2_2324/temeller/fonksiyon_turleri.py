#fonksiyon_turleri.py

# tanımlama şekline göre fonksiyonlar
# a. dahili(built-in) fonksiyonlar
# b. 3. parti fonksiyonlar
# c. kullanıcı tanımlı fonksiyonlar. 

# a. dahili fonksiyonlar

a=5
b=10
c=20
kare_farki= abs(a**2-b**2)

eb=max(a,b,c)
ek=min(a,b,c)
eb_ek_fark=eb-ek
print(kare_farki,eb_ek_fark)
# bir fonksiyonun işlemek için aldığı(parantez içinbe virgüller ayrılarak yazılan) değerlere parametre/argüman denir.

#b. 3. parti fonksiyonlar

import matplotlib.pyplot as plt
import numpy as np

x=np.array([3,4,10,8,20])
y=np.array([20,7,8,9,2])

plt.scatter(x,y)
plt.show()


# değer döndürme durumuna göre fonksiyonlar.
# çağrıldığı noktaya fonksiyon değer döndürüyor mu? Döndürmüyor mu?
print("merhaba") #geriye değer döndürmez
ad=input("adını yaz:") # geriye değer döndürür

# a. geriye değer döndürenler
# b. geriye değer döndürmeyenler

