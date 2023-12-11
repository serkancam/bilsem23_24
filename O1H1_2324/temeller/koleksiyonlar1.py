# koleksiyonlar1.py

# 1. liste(list) --> []
# 2. demet(tuple) --> ()
# 3. küme(set) --> {}
# 4. sözlük(dictionary) --> {k:v}

a=5
boy=1.74
isim="hakan"
print(len(isim))

isimler=["yaman","emek","ülkü","çınar"]
isimler.append("bartu")
isimler.append("ali")
isimler.append("elif")
isimler.append("çağatay")

print(isimler[2])
print(isimler)
isimler[0]="mustafa yaman"
isimler[2]="ülkü kerem"
isimler[3]="yahya çınar"
isimler[6]="elif ada"
isimler[7]="çağatay ali"
isimler.append("serkan")
print(isimler)
#değer silme
# del isimler[8]
# isimler.remove("serkan")
silinen=isimler.pop(8)
print("silinen:",silinen)
print(isimler)

# şimdi isimlere ait kiloların ve boyların olduğu 2 farklı liste tanımlayalım.
# boş liste
boylar=[]
kilolar=list()

for isim in isimler:
    boy = float(input(f"{isim} boyu:"))
    boylar.append(boy)
print(boylar)    
print(30*"*")
for i in range(len(isimler)):
    kilo=float(input(f"{isimler[i]} kilosu:"))
    kilolar.append(kilo)
    
print(kilolar)

maaslar=(30,20,40)