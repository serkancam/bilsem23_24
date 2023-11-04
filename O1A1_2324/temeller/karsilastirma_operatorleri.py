# karsilastirma_operatorleri.py

print(3<5)
print(3!=5)
a=8
b=10
print(a>=b)
sifre="1234"
print(sifre==1234)
print(sifre=="1234")
sonuc = a>b and 10<a
print("birleşik",sonuc)
# işe başvurusu kabul edilecekler için şart
# kadınlar için yaş en düşük 22
# erkekler için en düşük 25 olarak belirlenmiştir.
# buna göre cinsiye bilgisi ve yaş bilgisi alınan kişinin
# bşavuru kabul ise True değil ise False sonuç veren program kodunu yazınız.

# if yas>10:
#     print("bişey")

# kadın ve yaşı 22 den büyük olacak veya erkek ve yaşı 25ten büyük olacak.
cinsiyet=input("cinsiyet için e/k:")
yas=int(input("yas:"))

sonuc =  (cinsiyet=="k" and yas>22) or (cinsiyet=="e" and yas>25)
print(sonuc)

# bir öğrencinin not ortalaması, Türkçe dersi not ve devamsızlık sayısı girildiğinde aşağıdaki şartlara göre takdir alıp alamayacağını True False şeklinde cevaplayan kodu yazınız.
# not ortalaması 90 dan büyük veya eşit olmalı >=
#ve
# Türkçe dersi notu 70 ten büyük veya eşit olmaı
#ve
# Devamsızlık sayısı 15 ten az olmalı

"""
açıklama
"""

genel_ortalama =float(input("genel ortalama:"))
turkce_ortalama=float(input("Türkçe ortalaması:"))
devamsizlik=float(input("Devamsızlık:"))


durum = (genel_ortalama>=90)and(turkce_ortalama>=70)and(devamsizlik<15)