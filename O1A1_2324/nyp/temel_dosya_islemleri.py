# dosyadan kasıt,saf(pure) metin dosyaları

# dosya oluşturalım 
dosya=open(file="nyp/ilk_dosya.txt",mode="w",encoding="utf-8")
dosya.close()
# dosya üzerine w modunda yazı yazalım
dosya=open(file="nyp/ilk_dosya.txt",mode="w",encoding="utf-8")

isim="bilsem"
dosya.write(f"\nmerhaba {isim}\n")
dosya.close()

#kullanıcıdan aldığınız bir metni ilk_dosya.txt ye ekleyelim
d=open(file="nyp/ilk_dosya.txt",mode="w",encoding="utf-8")

metin=input("metin yazınız:")

d.write(metin+"\n")
d.close()
dosya_yolu="nyp/ilk_dosya.txt"
try:
    dosya=open(file=dosya_yolu,mode="w",encoding="utf-8")
    dosya.write("Merhaba Python")
    dosya.write("\n")
    dosya.write("Bu 2. satır")
    dosya.write("\n")
except FileNotFoundError:
    print("Dosya Bulunamadı")
else:
    dosya.close()
    print("Dosya Kapatıldı")
try:
    dosya=open(file=dosya_yolu,mode="r",encoding="utf-8")
    okunan = dosya.read()
    print(okunan)
except FileNotFoundError:
    print("Dosya Bulunamadı")
else:
    dosya.close()
    print("Dosya Kapatıldı")
