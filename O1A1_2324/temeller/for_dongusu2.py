for harf in "bilsem":
    print(harf)
    
    
print("a" in "ali")
print("a" in "meyve")
metin="ali ata bak."
print(metin.count("a"))
print(metin.replace("a","e"))

#  3 ten -101 kadar 7şer azalan ve her adımdaki değeri ekrana yazdıran for döngüsünü yazınız.
for sayi in range(3,-101,-7):
    print(sayi)

print("8 var mı?",8 in [8,2,3])# True
print("9 var mı?",9 in [8,2,3])# False