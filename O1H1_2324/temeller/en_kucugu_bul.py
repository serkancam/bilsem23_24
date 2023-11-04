#en_kucugu_bul.py
sayilar=[]
while True:
    sayi = int(input("pozitif sayı gir:"))
    if sayi == -1:
        break
    sayilar.append(sayi)

print("sayılar girişi bitti...")
print(sayilar)
# print(sayilar[3])

ek = sayilar[0]

for indis in range(len(sayilar)):
    if sayilar[indis]<ek:
        ek=sayilar[indis]

eks = min(sayilar)
print("en küçük sayı_min:",eks)
print("en küçük sayı benim:",ek)