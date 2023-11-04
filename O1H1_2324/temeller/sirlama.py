#sirlama.py
sayilar=[]
while True:
    sayi = int(input("pozitif sayı gir:"))
    if sayi == -1:
        break
    sayilar.append(sayi)

siralanmis =[]
print(sayilar)
while len(sayilar)!=0:
    a = min(sayilar)
    i=sayilar.index(a)
    siralanmis.append(sayilar.pop(i))


print(siralanmis)