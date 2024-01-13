dosya=open(file="nyp/notlar.txt",mode="a",encoding="utf-8")

while True:
    islem = input("ekle-e,çık-ç:")
    if islem=="ç":
        break
    elif islem=="e":
        #sorma ve ekleme işlemleri
        ad=input("adınız:")
        soyad=input("soyadınız:")
        s1=input("1. sınav:")
        s2=input("2. sınav:")
        dip1=input("dip1:")
        dip2=input("dip2:")
        dosya.write(f"{ad},{soyad},{s1},{s2},{dip1},{dip2}\n")
dosya.close()