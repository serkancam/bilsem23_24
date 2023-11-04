# karsilastirma_operatorleri.py

print(3==5)
print(3>5)
print(3<3)
print(3!=3)
print(3<=3)
print(3>=3)
a="ser"
b="kan"
print(a=="Ser")
print("kan "==b)

# işe alma: yaşı 25 ten büyük olup, boyu 1.70 ten büyük olanların işe başvuruları onaylanacak.
# onaylanma:True
# onaylanmam:False

yas = int(input("yaş:"))
boy = float(input("boy(metre):"))

durum = yas>25 and boy>1.70
print("durum:",durum)
