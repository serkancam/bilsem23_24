# min_bul.py

import random

sayilar = [random.randint(100,10000) for _ in range(100)]
print(sayilar)

print("en küçük", min(sayilar))
print(sayilar[0])

ek=sayilar[ 0]

for i in range(len(sayilar)):
    if sayilar[i]<ek:
        ek=sayilar[i]

print("benim en küçüç",ek)