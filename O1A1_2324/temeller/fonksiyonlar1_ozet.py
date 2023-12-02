# 3 Tür fonksiyon vardır.(tanımlanmasına göre)
# a. yerleşik(built-in) fonksiyonlar
# b. 3. parti fonksiyonlar
# c. Kullanıcı tanımlı fonksiyonlar
# yerleşik fonksiyonlar
a=int(input("sayi:"))
b=int(input("sayi:"))
c=int(input("sayi:"))

ek=min(a,b,c) # fonksiyonda virgül ile ayrılan değerlere, argüman/parametre
eb=max(b,c,a)
fark=eb-ek

print(f"en büyük:{eb}, en küçük:{ek}, fark:{fark}")

# 3. parti fonksiyonlar: import komutu ile koda eklenir.
# sudo pip3 install numpy matplotlib
import numpy as np
import matplotlib.pyplot as plt

x=np.array([10,12,2,3,5,8,7,-1,9,11])
y=np.array([1,4,5,9,7,10,8,7,25,4])
plt.scatter(x,y)
plt.show()
