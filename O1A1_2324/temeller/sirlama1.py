import random

sayilar = [ random.randint(1,1000) for i in range(100)]

print(sayilar)


ek=sayilar[0]
sira=0
for i in range(len(sayilar)):
    if sayilar[i]<ek:
        ek=sayilar[i]
        sira=i

print("en küçük:",min(sayilar))
print("en küçük benim:",ek)

