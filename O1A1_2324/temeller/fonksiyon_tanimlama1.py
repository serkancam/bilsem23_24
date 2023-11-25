# bir fonksiyon tanımlanır(definition) ve çağırılır(call)
# örneğin print fonksiyonunu çağıralım
print("a","merhaba")
# print fonksiyonu işini yapar ve sonlanır

# input fonksiyonunu çağıralım

ad=input("isim:")
# input print ten farklı olarak çağırıldı yere bir sonuç döndürür

def selam_yaz(adet:int):
    for i in range(adet):
        print("selam")
    print("fonskiyon bitti.")

selam_yaz(2)
selam_yaz(3)

# iki sayının kerelerinin farkını bulup ekrana yazdıran fonksiyonu yazalım

def kare_farki_bul(s1:float,s2:float):
    fark = s1**2 - s2**2
    print(f"{s1} ve {s2} kare farkı:{fark}")
    

kare_farki_bul(10,20)