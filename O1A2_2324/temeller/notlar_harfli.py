# notlar_harfli.py
# bir dersten vize, final ve ödev olmak üzere 3 not verilmketedir. 
# vizenin %30 u finalin %40'ı ödevin %30 u
# oalcak şekilde ders notu bulunacaktır
# buna göre:
# 0-40 arası: FF
# 40-60 arası: DD
# 60-70 arası : CC
# 70-85 arası:BB
# 85-100 arası:AA
vize = float(input("vize:"))
final=float(input("final:"))
odev=float(input("ödev:"))
ort = vize*0.3+final*0.4+odev*0.3
sonuc=""
if ort<40 and ort>=0:
    sonuc="FF"
elif ort<60 and ort>=40:
    sonuc="DD"
elif ort<70 and ort>=60:
    sonuc="CC"
elif ort<85 and ort>=70:
    sonuc="BB"
elif sonuc<=100 and sonuc>=85:
    sonuc="AA"
else:
    sonuc="hata"

print(f"{ort} ile {sonuc} aldın.")
