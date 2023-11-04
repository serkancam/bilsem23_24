# break_continue2.py

# kullanıcıdan sürekli pozitif tam sayılar alıp aldığı sayılardan çift olanları toplayan ve negatif bir sayı girildiğinde o ana kadar girilmiş pozitif çift olan sayıların toplamını ekrana yazdıran kodu yazınız.

toplam=0
while True:
    sayi=int(input("sayı:"))
    if sayi<0:
        break
    elif sayi%2==0:
        toplam+=sayi
    