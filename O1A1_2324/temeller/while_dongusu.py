"""
while şart:
    işlem1
    işlem2
    işlemn

*belli bir örüntünün tekrarı
*belli bir kod bloğunun tekrarı
"""

i=1
while i<=100:
    print(i)
    i=i+1

t=10
while t>=1 and t<=10:
    print(t)
    t =t-1

s1=int(input("sayi1:"))
s2=int(input("sayi2:"))
degisim=int(input("değişim:"))

# if s1<s2:
#     while s1<s2:
#         print(s1)
#         s1=s1+degisim
# elif s2<s1:
#     while s2<s1:
#         print(s2)
#         s2=s2+degisim

# if s1<s2:
#     ks=s1
#     bs=s2
# else:
#     ks=s2
#     bs=s1

# while ks<bs:
#     print(ks)
#     ks=ks+degisim

ks=min(s1,s2)
bs=max(s1,s2)
while ks<bs:
    print(ks)
    ks=ks+degisim
    
######################################
metin= input("isminiz:")

uzunluk = len(metin)
print(uzunluk)
h=0
while h<uzunluk:
    print(metin[h])
    h=h+1