# sayi = float(input("sayi:"))

# if sayi>=0 and sayi<=100:
#     print("kabul")
# else:
#     print("red")
 

vize=float(input("vize:"))
final=float(input("final:"))
odev=float(input("odev:"))
ort=vize*0.3+final*0.4+odev*0.3

if ort>=0 and ort<40:
    print("FF")
elif ort>=40 and ort<60:
    print("DD")
elif ort>=60 and ort<70:
    print("CC")
elif ort>=70 and ort<90:
    print("BB")
elif ort>=90 and ort<=100:
    print("AA")
else:
    print("hata")

print("ortalama:",ort)
