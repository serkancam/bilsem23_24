# for bir koleksiyon da dolaşmayı sağlar
# örneğin 2 4 6 8 10 12 sayı listesi olsun. Bu listedeki değerleri sırası ile alan bir i döngü değişkenimiz olsun

for i in range(2,13,2): # 
    print(i)

l1=[2,4,6,8,10,12]

for t in l1:
    print("t:",t)

aralik=range(2,13,2)    
l1[0]=30
print("l1:",l1)
# aralik[0]=5
print("aralik:",aralik)

# for y in 3:
#     print(y)

for karakter in "bilsem nasıl?":
    # print(karakter)
    if karakter in "euıoüiaö" and karakter.isalpha():
        print(f"{karakter} sesli harf")
    elif karakter.isalpha():
        print(f"{karakter} sessiz harf")
    else:
        print(f"{karakter } özel karakter")