def islem(a,b,c):
    print(f"a{a} - b:{b} - c:{c}")   

# fonksiyonlar çağırılıkern 2 şekilde parametre gönderilir
# a. pozisyonel/sıralı(positional) parametre
# b. isimli(named) parametre
# c. karışık
# bir fonksiyon çağrısında isimli parametre kullanımı başladı ise(soldan-sağa) diğer parametrelerde isimli kullanılır.
islem(3,5,8) # tamamen pozisyonal parametre gönderimi
islem(b=8,c=3,a=10) # tamamen isimsel parametre gönderimi
islem(3,c=5,b=8) # hata yok. Karışık kullanım
# islem(a=5,b=8,10) # hatalı
# islem(c=5,3,8) # hatalı kullanım 
# islem(3,a=5,b=8) # hatalı kullanım

def islem2(a=10,b=5,c=8):
    print("işlem2 ")
    print(f"a:{a} - b:{b} - c:{c}")
    
islem2()
islem2(20)
islem2(a=5,c=8,b=38)
islem2(b=100)

import math

def daire_alan(r,pi=math.pi):
    return pi*r**2

print(daire_alan(5,3))

