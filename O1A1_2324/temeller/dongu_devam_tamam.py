# break
# continue

# kullanıcı 0-100 arası sayı girene kadar çalışan programı yazınız.
# sayi1=0
# while True:
#     sayi1=int(input("0-100 arası sayı giriniz:"))
#     if sayi1>=0 and sayi1<=100:
#         break

# print(f"girilen sayı:{sayi1}")

# Bu işlemler break olmadan yazılabilir mi?

sayi=-1
# while sayi<0 or sayi>100:
#     sayi=int(input("sayi:"))
while not(sayi>=0 and sayi<=100):
    sayi=int(input("sayi:"))
print(sayi)


