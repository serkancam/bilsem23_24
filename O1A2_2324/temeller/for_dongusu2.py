# 100 den 25 e 7 şer azalan değerleri for döngüsü ile ekrana yazdırın
# 20 den 102 ye 4 er artan değerleri for döngüsü ile ekrana yazdırın
# 3 ten 1003 e kadar olan çift sayıların toplamını for döngüsü ile bulunuz.
for s in range(100,25,-7):
    print(s)
print(30*"-")
for  s2 in range(20,102,4):
    print(s2)
print(30*"-")
####################################################

toplam=0
for sayi in range(3,1003):
    if sayi%2==0:
        toplam=toplam+sayi
        
print(f"toplam:{toplam}")
    
