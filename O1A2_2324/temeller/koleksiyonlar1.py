# 4 temel koleksiyon türünden bahsedebiliriz:
# a. *liste (list) --> []
# b. demet (tuple) --> ()
# c. küme (set) --> {}
# d. sözlük (dictionary) --> {k:v}
# listeler:
# çok sayıda ve çok boyutta eleman barındırır.

# elemanları silinebilir,değiştirilebilir ve yeni eleman eklenebilir.

isimler=["aslan","kuzey","ömer","ege","berk","ali","süleyman"]
"""
print(type(isimler))
print(isimler)
print(isimler[0])
isimler[0]="aslan efe"
print(isimler)
isimler.append("ahmet")
isimler.append("yusuf")
print(isimler)
print(len(isimler))
print(len("ali"))
print("ahmet nerde?:",isimler.index("ahmet"))
# isimler.clear()
isimler.reverse()
print(isimler)
print("serkan"[::-2])
"""


kilolar=[] # boş liste
boylar=list() #boş liste

for isim in isimler:
    # print(isim)
    kilo=float(input(f"{isim} kilosu giriniz:"))
    kilolar.append(kilo)
print(kilolar)

for i in range(len(isimler)):
    boy= float(input(f"{isimler[i]} boyunu giriniz:"))
    boylar.append(boy)


print(boylar)

#bkiler boş listesine, isimler listesindeki kişinin boylar ve kilolar listelerini kullanrarak bki değerini hesaplayıp ekleyniz. bki=kilo/(boy*boy)

bkiler=[]

for 3 in range(len(isimler)):
    bki=kilolar[i]/(boylar[i]**2)
    bkiler.append(bki)
    


for i in range(len(isimler)):
    print(f"{isimler[i]} bki: {bkiler[i]}")














# import random

# rl = [ random.randint(1,100) for i in range(random.randint(1,100))]
# print(rl)