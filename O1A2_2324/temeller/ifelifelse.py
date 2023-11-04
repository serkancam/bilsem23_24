#ifelifelse.py
"""
kullanım1:
if şartlar:
    işlem1
    işlem2
    işlemn

kullanim2:
if şart1:
    işlem1
    işlem2
    işlemn
else:
    işlem1
    işlem2
    işlemn
    
kullanim3:
if şart1:
    işlem1
    işlem2
    işlemn
elif şart2
    işlem1
    işlem2
    işlemn
elif şartn
    işlem1
    işlem2
    işlemn
else:
    işlem1
    işlem2
    işlemn 
"""
# kullanıcı girdiği ürünün fiyatı 200 tl den pahalı ise ürünün fiyatında
# %10 indirim yapan ve ekrana yazdıran kodu yazınız:

fiyat = float(input("ürün fiyatını giriniz:"))

if fiyat>200:
    fiyat*=0.9#fiyat=fiyat*0.9
    a=5

print(f"fiyat:{fiyat}")
print(a)

