metin=input("metin giriniz:")
hece_sayisi=0

# harf değişkeni sıra ile metin içindeki her harfi temsil edecek
for harf in metin:
    if harf in "uieaıüöo":
        hece_sayisi=hece_sayisi+1


print(f" metindeki hece sayısı:{hece_sayisi}")




