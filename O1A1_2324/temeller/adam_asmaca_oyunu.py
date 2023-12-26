# adam_asmaca_oyunu.py
"""
 1- Bir *.txt dosyasında yazılı olan ülke isimlerinden rastgele seçim yapılır.
 2- kullanıcıdan istenen  harflerin saklandığı bir  boş liste oluşturulu(tahminler).
 3- Bilinen harfler boş listesi oluşturulur(bilinenler).
 4- bir sonsuz döngüde sürekli kullanıcıdan harf istenir.
 5- bir harf giriniz:
 6- harf -1 değeri ise oyunu bitir
 7- harf daha önce söylenen bir harf ise veya bir harf girilmedi ise 5. satıra git
 8- girilen harfi tahminler listesine ekle
 9- soylenen harf cümlede varsa bilinenler listesine ekle
 10- metni bilinen harfler dışında _ olacak şekilde yazdır. (_ta__a)
 11- yazdırılan metinde _ yoksa ve tahmin hakkı bitmemiş ise kazandın tebrikeler yaz ve oyunu bitir
 12-? 
"""
import random
import adam_karakter

dosya=open("temeller/ulkeler.txt","r",encoding="utf-8")
cumle = random.choice(dosya.readlines()).lower()
dosya.close()
print(cumle)
hak=0
tahminler=[]
bilinenler=list()

def yazdir():
    tahmin=""
    for h in cumle:
        if h=="":
            tahmin=tahmin+" "
        elif h in bilinenler:
            tahmin=tahmin+h
        elif h=="\n":
            continue
        else:
            tahmin=tahmin+"_ "
    print(tahmin)
    return tahmin

while True:   
    harf=input(f"{7-hak} hakkınız kaldı\ndaha önce söylenmemiş bir harf giriniz:").lower() #5. satır
    if harf=="-1":
        break
    if len(harf)!=1 or (not harf.isalpha()) or (harf in tahminler):      
        continue
    tahminler.append(harf)
    if harf in cumle:
        bilinenler.append(harf)
    else:
        hak+=1
    adam_karakter.karakter_ciz(hak)
        
    kontrol=yazdir()
    if hak==7:
        break
    if "_" not in kontrol:
        print("Tebrikler kazandınız:")
    
    