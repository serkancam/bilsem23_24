# karsilastirma_operatorleri.py

print(3<5)
print(3<3)
a=8
b=10
c="hami"
d="veli"
print(c==d)
print("VELİ"==d)

# işe başvurusu kabul edilecekler için şart
# kadınlar için yaş en düşük 22
# erkekler için en düşük 25 olarak belirlenmiştir.
# buna göre cinsiyet bilgisi ve yaş bilgisi alınan kişinin
# bşavuru kabul ise True değil ise False sonuç veren program kodunu yazınız.

cinsiyet = input("cinsiyet e/k:")
yas=int(input("yas:"))
# kadın ve yaşı 22 den büyük veya erkek ve yaşı 25ten büyük olanların
# başvurusu onaylanır
durum = (cinsiyet=="k" and yas>22) or (cinsiyet=="e" and yas>25)
print(f"durum:{durum}")
print("durum:",durum)

# 20 ekime pas:
# sınıf geçme ve takdir almayı yap