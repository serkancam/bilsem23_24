# sayi_araligi_giris.py

while True:
    sayi1=float(input("sayı1:"))
    if sayi1>=0 and sayi1<=100:
        break


while True:
    sayi2=float(input("sayı2:"))
    if sayi2>=0 and sayi2<=100:
        break

ortalama=(sayi1+sayi2)/2
print(f"ortlama:{ortalama}")


s=1
while s<=10:
    if s==7:
        s=s+1
        continue
        
    print(s)
    s=s+1
    # if s==7:
    #     s=s+1