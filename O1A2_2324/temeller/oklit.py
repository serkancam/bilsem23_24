a = int(input("sayı gir:"))
b = int(input("sayı gir:"))

bs = max(a, b)
ks = min(a,b)
kalan=-1
adim=0
while kalan != 0:
    kalan = bs % ks
    bs=ks
    ks=kalan
    adim += 1 #adim=adim+1

print(f"{a} ile {b} sayısının en büyük ortak böleni={bs}")
print("bu işlem",adim,"adımda yapıldı.")