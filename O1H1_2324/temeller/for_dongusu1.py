# for_dongusu1.py

# for döngüsü bir koleksiyon içindeki elemanları sırayla bir döngü değişkeninen aktararak ilerleyen bir yapıdır. Koleksiyonda eleman kalmayınca döngü sonlanır.

# tekil değer tutan ilkel değişkenler
a=5 #int
b=1.2 #float
c=True #bool

d=""
e="merhaba"
# string: metin, yazı. Karakter dizisi
ad_soyad="edirne bilsem"
# for  değişken(ler)  in koleksiyon:
#   işlemler

for karakter in ad_soyad:
    print(karakter)

# tek parametreli range kullanımı
# range(p1): 0 dan p1 değerine kadar birer artan sayılar. p1 hariç
aralik1=range(6) # 0 1 2 3 4 5 

for i in range(8):# 0 1 2 3 4 5 6 7
    print(i)
    
# iki parametreli range kullanımı
# range(p1,p2): p1 değerinden p2 değerine kadar birer artan sayı koleksiyonu oluştur. p2 hariç
print(30*"*")
aralik2 = range(3,8) # 3 4 5 6 7 

for a in aralik2:
    print(a)

# üç parametreli kullanım
# range(p1,p2,p3): p1 değerinden p2 değerine kadar p3 değeri kadar değişerek oluşan sayıların koleksiyonu.p2 hariç

aralik3= range(8,20,3) # 8 11 14 17 
aralik4= range(10,5,-1)  # 10 9 8 7 6  

print(30*"?")
for g in range(30,45,2):
    print(g)

# 45 ten 1' kadar 3er azalan değerleri ekrana for ve range yardımı ile yazınız
# 72 den 105'e kadar 7 şer artan değerleri for ve range yardımı yazınız

print(30*"*")

for y in range(45,1,-3):
    print(y)
print(30*"*")
for q in range(72,105,7):
    print(q)

# 343 ten 1 kadar 7 şer bölünerek
print("7ye bölünereke")
a=343
while a>=1:
    print(a)
    a=a/7
# print(a)
# a=a/7
# print(a)
# a=a/7
# print(a)
# a=a/7
# print(a)