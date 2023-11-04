# basit_faiz_hesaplama.py
#günlük faiz kazancı hesaplama
# ana para, faiz oranı ve vadesi girilen bir program yaparak
# vade sonundaki günlük faiz kazancını bulan programı python ile kodlayınız.

ap = float(input("ana para:"))
fo = float(input("faiz oranı:"))
vade = int(input("vade:"))

kazanc = ap*(fo/100)*(vade/365)

print(f"{ap} TL paranın {vade} günlük kazancı:{round(kazanc,2)} ")
