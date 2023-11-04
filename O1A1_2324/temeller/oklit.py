a = int(input("bir sayı giriniz:"))
b = int(input("bir sayı giriniz:"))
adim = 0
#yöntem1 
sonuc = min(a,b)

while sonuc:
    if a%sonuc == 0 and b%sonuc==0:
        break
    sonuc-=1

print(f"yöntem 1:\n {a} ve {b} ebob={sonuc}")
#öklit algoritması
kucuk= min(a,b)
buyuk= max(a,b)
kalan = -1
while kalan!=0:
    kalan=buyuk%kucuk
    buyuk=kucuk
    kucuk=kalan
    adim += 1

print(f"öklit: \n {a} ve {b} ebob={buyuk} {adim} adımda")

