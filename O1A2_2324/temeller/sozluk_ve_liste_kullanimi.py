# sozluk_ve_liste_kullanimi.py

ogrenci_boylari=dict() # boş sözlük {k:v}-{anahtar:değer}

# sözlüklerde koleksiyon elemanlarına key değerleri ile ulaşılır.
print(ogrenci_boylari)
ogrenci_boylari["yusuf"]=1.72
print(ogrenci_boylari)
ogrenci_boylari["ali"]=1.7
ogrenci_boylari["ege"]=1.40
ogrenci_boylari["ömer"]=1.68
ogrenci_boylari[78]=1.74
serkan=42
ogrenci_boylari[serkan]=1.74
# bir koleksiyon elemanı olarak herşey atanabili.
print(ogrenci_boylari)
# koleksiyonlarda indis veya elemanlara ulaşmak için [] operatörü kullanılır

print(ogrenci_boylari.keys())
print(list(ogrenci_boylari.keys())[2])
print(ogrenci_boylari.items())
print("ali'nin boyu:",ogrenci_boylari["ali"])
for anahtar in ogrenci_boylari.keys():
    print(anahtar,ogrenci_boylari[anahtar])
    
# türkçe,matematik,fen, ingilizce,sosyal
import os
import pandas as pd
notlar={"süleyman":[95,95,90,95,100]}
dersler=["türkçe","matematik","fen","ingilizce","sosyal"]

while True:
    os.system("clear")
    girilen=input("öğrenci adı giriniz(çıkmak için ç):")
    if girilen.lower()=="ç":
        break
    nt=list()
    for ders in dersler:
        n=float(input(f"{girilen} öğrencisinin {ders} ortlamasını giriniz:"))
        nt.append(n)
    notlar[girilen]=nt

dosya=pd.DataFrame(notlar)
dosya.to_csv("notlar.csv")

os.system("clear")
print(notlar)