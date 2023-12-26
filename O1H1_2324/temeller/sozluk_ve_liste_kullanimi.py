# sozluk_ve_liste_kullanimi.py

# sözlük verilerin anahtar:değer çiftleri ile saklandığı bir koleksiyon türüdür.
# her koleksion değer/eleman olarak herşeyi alabilir. Bu bir listenin elemanının bir liste veya sözlükte olabilaceğini gösterir.
boylar={"ali":1.65,"emek":1.65,"serkan":1.74}
kilolar=[70,72,83,None,80]
print("emek kilosu:",kilolar[1])
print("emek boyu:",boylar["emek"])

dersler=["türkçe","matematik","fen","sosyal","ingilizce"]
notlar={"elif ada":[95,98,95,100,100]}
notlar["bartu"]=[95,100,90,95,100]
print(notlar)
print(dersler)
import os
import pandas as pd

while True:
    os.system("clear")
    deger = input("(çıkmak için ç giriniz:)öğrenci ismi giriniz:")
    if deger.lower()=="ç":
        break
    nt=list()#boş liste
    for d in dersler:
        n=float(input(f"{deger} öğrencisinin {d} notunu giriniz:"))
        nt.append(n)
    # print(f"{deger}: {nt}")
    notlar[deger]=nt
# print(notlar)
df = pd.DataFrame(notlar)
df.to_csv("temeller/notlar.csv")