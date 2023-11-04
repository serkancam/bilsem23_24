vize = float(input("vize:"))
final = float(input("final:"))
odev = float(input("odev:"))

ortalama =  vize*0.3 + final*0.4 + odev*0.3

if ortalama>=0 and ortalama<40:
    print("ff")
elif ortalama>=40 and ortalama<50:
    print("dd")
elif ortalama>=50 and ortalama<70:
    print("cc")
elif ortalama>=70 and ortalama<90:
    print("bb")
elif ortalama>=90 and ortalama<=100:
    print("aa")