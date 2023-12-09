# demet(tuple)

notlar = (100,85,85)

# demet yapılakrı sonradan eleman eklenmesine,çıkarılmasına, elemenların değiştirilmesine izin vermez. Onun için değiştirilmez veriler için kullanılır.
# oyun karakter renkleri, başlangıç koortdinatları.

print(notlar[0])
# notlar[0]=80 #hata

# küme(set)

ayakkabi_numaralari ={42,41,40,40,38,43,41,36,40.5,39}
print(ayakkabi_numaralari)
# sıralaı değildir. elemanlara ulaşım olamaz
# print(ayakkabi_numaralari[0])

ayakkabi_numaralari.add(44)
print(ayakkabi_numaralari)
print(len(ayakkabi_numaralari))

a=[1,1,2,3,4,4,5]
print("a listesi eleman sayısı:",len(a))
b=set(a)
print("b listesi eleman sayısı:",len(b))

# sözlük(dictionary)

# anahtar(key):değer(value) 

boylar={"gülce":1.55,"okyanus":1.60,"ada":1.62}

print(boylar["ada"])
boylar["ada"]=1.65
print(boylar)

notlar={"gülce":[85,100,100],"okyanus":[100,90,85],"ada":[90,90,100]}

print(notlar)
notlar["gülce"][0]=100
print(notlar)