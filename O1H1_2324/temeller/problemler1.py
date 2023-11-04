# b peynirinin kg fiyatı, a peynirinin kg fiyatından 10 tl fazla olduğu bilinmektedir.
# buna göre  a peynirinin fiyatı ile a ve b peynirinden kaçar kg alındığı bilgisi girildiğinde, yapılacak ödemeyi hesaplayan ve sonucu ekrana yazdıran programı python kodu ile yazınız.

a_fiyati=float(input("a fiyati:"))
b_fiyati=a_fiyati+10
a_kg=float(input("a kaç kg:"))
b_kg=float(input("b kaç kg:"))

odenecek=a_fiyati*a_kg+b_fiyati*b_kg

print(f"ödenecek: {odenecek}")

##########delta##########
a=float(input("A:"))
b=float(input("B:"))
c=float(input("C:"))
delta=(b**2)-(4*a*c)
print(f"delta:{delta}")

####+ ve * operatörü str lerde kullanımı

print("2"+"2") #22
print(3*"re",3*"ra")