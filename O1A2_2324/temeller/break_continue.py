# break_continue.py
# kullanıcının 0-100 arası sayı girmesini, bunun dışında sayı girilir ise tekrar sayı girmesini sağlayan python kodunu yazınız.

while True:
    sayi1=int(input("sayı1:"))
    if sayi1>=0  and sayi1<=100:
        break

print(sayi1)

sayi2=-1
while not(sayi2>=0  and sayi2<=100):
    sayi2=int(input("sayı2:"))
    
print(sayi2)