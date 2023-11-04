r1=range(5)  # tek parametreli kullanımda 0 dan yzılan tam sayı değerine kadar birer artan sayılar ifade edilir. sayının kendisi dahil değildir.
print(r1) # 0,1,2,3,4
print(*r1)# * bir koleksiyonun elemanlarını sıra ile yazıdırır
r2=range(70)
print(*r2)

######
print(30*"*")
r3=range(2,8) #virgülün solundaki yazılan tam sayı değerinden sağıundaki tam sayı değerine  kadar birer artan sayılar ifade edilir. sayının kendisi dahil değildir.
# 2,3,4,5,6,7
print(*r3)
print(30*"*")
####
r4=range(53,82,3) # 53 ten 82 ye kadar 3 er artan 53,56,59......80
print(*r4)
print(30*"*")
###
r5 = range(80,10,-10)
print(*r5)

for i in range(2,10,2):#2 4 6
    print(i)

# in anahtar kelşmesinden sonra olan değişken çok elemanlı(koleksiyon)


