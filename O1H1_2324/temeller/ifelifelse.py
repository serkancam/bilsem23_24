# ifelifelse.py

"""
if şart1:
    işlem1
    işlem2
    işlemn
elif şart2:
    işlem1
    işlem2
    işlemn
elif şartn:
    işlem1
    işlem2
    işlemn
else:
    işlem1
    işlem2
    işlemn
"""
# fiyatı girilen ürün 200 tl den fazla ise %10 indirim yapan ve bu yeni indirimli fiyatı ekrana yazdıran kodu yazınız.

fiyat =  float(input("fiyat:"))

if fiyat>200:
    fiyat=fiyat*0.9
    
print(f"fiyat:{fiyat}")

