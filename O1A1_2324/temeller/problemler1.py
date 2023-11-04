# kullanıcının girdiği 3 sayının ortlamasını bulan programı yazınız.

s1= float(input("s1:"))
s2= float(input("s1:"))
s3= float(input("s1:"))

ortalama =(s1+s2+s3)/3

# b peynirinin kg fiyatı, a peynirinin kg fiyatından 10 tl fazla olduğu bilinmektedir.
# buna göre  a peynirinin fiyatı ile a ve b peynirinden kaçar kg alındığı bilgisi girildiğinde, yapılacak ödemeyi hesaplayan ve sonucu ekrana yazdıran programı python kodu ile yazınız.

a_fiyat=float(input("a fiyati:"))
b_fiyati=a_fiyat+10
a_kg=float(input("a kg:"))
b_kg=float(input("b kg:"))

odenecek= a_fiyat*a_kg+b_fiyati*b_kg

print(odenecek)