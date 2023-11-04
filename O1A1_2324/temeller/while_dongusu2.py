ilk=int(input("ilk sayı:"))
son=int(input("son sayı:"))
bolen=int(input("bölen sayı:"))

# ilk ve sons ayı arasındaki bolen sayısına kalansız bölünebilen sayıların  toplamı.

t=ilk
toplam=0
while t<=son:
    if t%bolen==0:
        toplam=toplam+t #toplam+=t
    t=t+1
    
print(f"{ilk} ve {son} değerleri arasında {bolen} değerine kalansız bölünen sayıların toplamı:{toplam}")