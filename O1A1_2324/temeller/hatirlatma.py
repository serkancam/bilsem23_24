#1. işlem
# boş liste tanımlayıp 
# sınıftaki kişilerin adını listeye tek tek ekleyin

l=[]
l.append("gülce")
l.append("hasan")
l.append("ece")
l.append("ada")
l.append("rüzgar")
l.append("cem")
l.append("okyanus")
l.append("emin")
l.append("arke")
print(l)
# 1 ile 22 arasında sayıları ekrana yazdıran kodu while yardımı ile yapınız.
a=1
while a<=22:
    print(a)
    a+=1
# 20 den -2 ye kadar(20 ve -2 dahil) ikişer azalarak sayıları ekrana for döngüsü yardımı ile yazdırnız.
print(30*"*")
for b in range(20,-3,-2):
    print(b)
    

#1 den 10 a kadar sayıların toplamını for döngüsü ile bulunuz.

t=0
r=int(input("sayı giriniz:"))
for s in range(1,r+1):
    t+=s
    
print(f"1 den {r}'a kadar sayıların toplamı={t}")
