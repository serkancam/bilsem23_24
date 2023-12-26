# ogrenci_not_ortlamalari.py

#liste ve sözlük yapısını kullancağız

notlar=[]
dersler=["matematik","fen","türkçe"]

for ders_adi in dersler:
    # print(ders_adi)
    n=float(input(f"{ders_adi} notu:")) 
    notlar.append(n)
print(notlar)

# ortalama=(notlar[0]+notlar[1]+notlar[2]+notlar[3])/4
toplam=0
for eleman in notlar:
    toplam+=eleman
    
print(toplam)
print(toplam/len(notlar))

"""not aralığı çözümü"""
"""
indis=0
while indis<len(dersler):
    n=float(input(f"{dersler[indis]} notu:"))
    if not(n>=0 and n<=100):
        continue
    notlar.append(n)
    indis+=1
"""