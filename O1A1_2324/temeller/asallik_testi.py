# asallik_testi.py
"""
sayi = int(input("sayı giriniz:"))
durum=""
for bolen in range(2,sayi):
    if sayi%bolen==0:
        durum="asal değil"
        break
    else:
        durum="asal"
        
print(f"{sayi} {durum}")
"""
#yukarıdaki örneğe bakarak parametre olarak aldığı tam sayı asal ise True, değil ise False değerinin geri döndüren fonksiyonu tanımlayınız.

def asalMi(s:int):
    durum=True
    for bolen in range(2,s):# s değeri 8 olursa 2-3-4-5-6-7
        if s%bolen==0:
            durum=False
            break
    return durum

sayi = int(input("sayı:"))

if asalMi(sayi):
    print(f"{sayi} asaldır.")
else:
    print(f"{sayi} asal değil?")