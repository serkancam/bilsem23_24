#günlük faiz kazancı hesaplama

# ana para, faiz oranı ve vade süresi girilen bir program yaparak
# vade sonundaki günlük faiz kazancını bulan programı python ile kodlayınız.
ap = float(input("Ana para:"))
fo = float(input("faiz orani:"))
vs = int(input("vade süresi:"))

kazanilan = ap*(fo/100)*(vs/365)

print(f"{ap} TL {vs} günde {fo} faiz oranı ile {kazanilan} TL kazandırır.")
