#günlük faiz kazancı hesaplama

# ana para, faiz oranı ve vade  girilen bir program yaparak
# vade sonundaki günlük faiz kazancını bulan programı python ile kodlayınız.

ap = float(input("ana para:"))
fo = float(input("faiz orani:"))
vade = int(input("vade:"))

kazanc= ap*(fo/100)*(vade/365)
kazanc=round(kazanc,2)
print(f"{ap} TL {fo} faiz oranı ile {vade} günde {kazanc} TL kazandırır.")