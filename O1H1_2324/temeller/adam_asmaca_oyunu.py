"""
1: kullanıcı tarfından söylenen harflerin kaydedildiği "tahminler" adında bir boş liste tanımlanır.
2: kullanıcı tarfınfdan söylenen ve bilinmesi gereken metinde bulunan harflerin kaydedildiği "bilinenler" adında boş bir liste tanımlanır
3: "ulkeler.txt" isimli içinde sorulacak ülke adlarının satır satır yer aldığı bir dosyadan rastgele bir ülke ismi seçilir.
4: kullanıcıdan daha önce söylenmemiş bir harf girmesi istenir
5: "-1" girildi ise oyunu bitir.
6: eğer girilen karakter sayısı 1'den fazla ise veya girilen karakter daha önce söylenmişse veya boş ise 4.satıra geri dön
7: eğer girilen karakter harf değilse 4. satıra git
8: girlen hgarfi "tahminler" listesine ekle
9: eğer girilen harf bilinmesi gereken metinde varsa "bilinenler" listesine ekle
10: bilinen harfler listesine göre metni yazdır(f _ a n _ a)
11: yazdırmada _ yoksa tebirkler de ve oyunu bitir. varsa 4. satıra dön

"""
import adam_asmaca
import random
import os

tahminler=list()
bilinenler=[]
hak=0
dosya=open("temeller/ulkeler.txt",mode="r",encoding="utf-8")
ulke=random.choice(dosya.readlines()).lower()
dosya.close()
# print(ulke)
def yazdir(ulke_adi:str,bilinen_harfler:list,hak:int):
    os.system("clear")
    yazilacak=""
    for hr in ulke_adi:
        if hr==" ":
            yazilacak=yazilacak+" "
        elif hr in bilinen_harfler:
            yazilacak=yazilacak+hr+" "
        elif hr=="\n":
            continue
        else:
            yazilacak=yazilacak+"_ "
    adam_asmaca.cop_adam_ciz(hak)
    print(yazilacak)
    return yazilacak
    
    

while True:#4. satır,
    yazdir(ulke,bilinenler,hak)   
    harf = input(f"{7-hak} hakkınız kaldı-->söylenmemiş bir harf giriniz:").lower()
    if harf=="-1":
        break
    elif len(harf)!=1 or (harf in tahminler) or harf==" ":
        continue
    elif not harf.isalpha():
        continue
    
    tahminler.append(harf)
    if harf in ulke:
        bilinenler.append(harf)
    else:
        hak=hak+1
    
    kontrol = yazdir(ulke,bilinenler,hak)
    if hak==7:
        print("hakkınız bitti.")
        break
    if "_" not in kontrol:
        print("Tebrikler bildin")
        break
    
    
    
    
