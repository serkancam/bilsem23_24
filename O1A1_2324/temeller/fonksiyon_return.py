# fonksiyon_return.py

ad=input("ad:")
soyad=input("soyad:")

print("merhaba")

print("print ilk parametre",input("yaz:"))

print("toplam=",int(input("1. sayı:"))+int(input("2. sayı:")))

def ucgen_cevre(k1:float,k2:float,k3:float):
    cevre=k1+k2+k3
    return cevre

# ucgen_cevre(3,5,6,7)
# ucgen_cevre(3,4)

cevre = ucgen_cevre(10,12,11)
print("üçgen çevresi",cevre)
print("üçgen çevresi",ucgen_cevre(10,12,11))