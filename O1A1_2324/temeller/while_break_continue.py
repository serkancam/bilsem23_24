# sürekli kullanıcıdan aldığı 0-100 arası sayıları toplayan negatif sayı girilince toplam sonucunu ekrana yazdıran, toplama çift sayıları dahil etmeyen kodu yazınız.
toplam=0

while True:
    sayi=int(input("sayı giriniz:"))
    if sayi<0:
        break
    if sayi%2==0:
        continue
    toplam=toplam+sayi
    

print(f"girilen tek pozitif sayıların toplamı:{toplam}")