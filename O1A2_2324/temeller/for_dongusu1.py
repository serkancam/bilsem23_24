# 20 0 kadar ikişer
#ilk =20
#son=0
#değişim=-2
i=20
while i>=0:
    print(i)
    i-=2
print("döngü sonu i değeri:",i),

# for değişken(ler) in koleksiyon:
#     işlem1
#     işlem2
#     işlem3

adim="serkan çam" # karkater koleksiyon

for krk in adim:
    print("i:",krk)
    

print("döngü sonu.")

# tek parametreli kullanımı
# 0 dan parametre olarak girilen değere kadar 1 er artımlı sayılar. parametre değeri hariç
aralik1= range(5) # 0 1 2 3 4 

for sayi1 in range(10):
    if sayi1==7:
        continue
    print(sayi1)
    
# iki parametreli kullanımı
# birinci parametreden ikinci parametreye kadar 1 er artımlı sayılar. ikinci parametre hariç
print(30*"_")
aralik2=range(10,14) # 10 11 12 13 

for sayi2 in aralik2: 
    print(sayi2)

# üç parametreli kullanımı
# birinci parametreden ikinci parametreye kadar üçüncü parametre değeri kadar değişim ile . ikinci parametre hariç
print(30*"_")
aralik3=range(100,250,7)
aralik4=range(250,100,-7)

for sayi3 in range(55,88,5):#55 60 65 70 75 80 85 
    print(sayi3) 

print(30*"_")
for x in aralik4:
    print(x)