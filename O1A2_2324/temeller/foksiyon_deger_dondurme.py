# a=input("adınız:")
# b=input("soyadınız:")


# print("toplam:",int     (input("1. sayı:"))+int(input("2. sayı:")))
# print(      )

# fonsksiyonu çağırdığımda çöp adam çizen fonksiyonu tanımlayınız.

def cop_adam():
    print("  @  ")
    print(" /|\ ")
    print("  |  ")
    print(" / \ ")
    
cop_adam()
# sayı asal mı? değil mi?
sayi = int(input("sayı:"))


durum=True
for bolen in range(2,sayi):#2,......sayi-1
    if sayi%bolen==0:
        durum=False
        break

print(f"sayi:{durum}")

# yukarıdaki asalmı bulan işlemi fonksiyoına çeviriniz
# parametre olarak aldığı tam sayının asallık durumunu geri döndüren fonksiyonu tanımlyınız.

#############    
def asal_mi(sayi:int):
    durum=True
    for i in range(2,sayi):
        if sayi%i==0:
            durum=False
            break
    return durum


############

a=int(input("sayı gir:"))
if asal_mi(a):
    print(a,"asal")
else:
    print(a,"asal değil")



