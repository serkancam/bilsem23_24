#  soruları yazmayın

# soru1: kullanıcının girdiği 3 sayının ortlamasını bulan programı yazınız.
s1=float(input("s1:"))
s2=float(input("s2:"))
s3=float(input("s3:"))
ortalama=(s1+s2+s3)/3
print("ortalama",(s1+s2+s3)/3)

# soru2: b peynirinin kg fiyatı, a peynirinin kg fiyatından 10 tl fazla olduğu bilinmektedir.
# buna göre  a peynirinin fiyatı ile a ve b peynirinden kaçar kg alındığı bilgisi girildiğinde, yapılacak ödemeyi hesaplayan ve sonucu ekrana yazdıran programı python kodu ile yazınız.

a_fiyati=float(input("a fiyat:"))
b_fiyati=a_fiyati+10
a_kg=float(input("a kg:"))
b_kg=float(input("b kg:"))
odeme=(a_fiyati*a_kg)+(b_fiyati*b_kg)
print(f"odeme:{odeme}")