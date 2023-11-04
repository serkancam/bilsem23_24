#oklit.py
#euclid.py

a = int(input("sayı gir:"))
b = int(input("sayı gir:"))

bs=max(a,b)
ks=min(a,b)
adim = 0
kalan = -1

while kalan!=0:
    kalan =  bs % ks
    bs = ks
    ks = kalan
    adim=adim+1 # adim+=1

print(f"{a} ve {b} sayılarının ebob'u {bs} sayısıdır.")
print(f"bu işlem {adim} adımda yapılmıştır.")
