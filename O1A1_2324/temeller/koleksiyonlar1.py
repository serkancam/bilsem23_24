# koleksiyonlar1.py

# 1. Liste (list) --> []
# 2. Demet (Tuple) --> ()
# 3. küme (set) --> {}
# 4. sözlük (dictionary) --> {k:v}

# indis(index) erişşimi için köşeli poarantez her koleksiyonda kullanılır.

isimler=["rüzgar","hasan","okyanus","muhammed","gülce","ada"]

# elemanlara erişim
print(isimler)
print(isimler[2])
isimler[0]="kerem rüzgar"
isimler[1]="hasan emir"
isimler[3]="muhammed emin"
print(isimler)
# isimler.append("ece evren")
# isimler.append("cem")
# isimler.append("arke doruk")
print(isimler)
boylar=[] #boylar=list()
print(f"isimler listesi eleman sayısı:{len(isimler)}")
print(f"boylar listesi eleman sayısı:{len(boylar)}")

agirliklar=list() # bu değerleri isimlere kullanıcı giricek
# agirlık girişi için çözüm:

for isim in isimler:
    # print(isim)
    boylar.append(float(input(f"{isim} boyu:")))
    agirliklar.append(float(input(f"{isim} ağrılığı:")))
    # deger = input(f"{isim} agırlığı:")
    # deger=float(deger)
    # agirliklar.append(deger)
    
print(isimler)
print(boylar)
print(agirliklar)



bkiler=[]# boylar,kilolar ve isimler listelerinden yararlanılarak oluşturulacak.bki=ağırlık/(boy*boy)
#bki lerin hesaplanması için çözüm:

for i in range(len(isimler)):#0 1 2 3 4 5 6 7 8 
    print(isimler[i])
    bki= agirliklar[i]/(boylar[i]**2)
    bkiler.append(bki)

print(bkiler)



