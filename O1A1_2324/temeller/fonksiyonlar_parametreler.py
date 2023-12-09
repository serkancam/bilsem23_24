# fonksiyonlar_parametreler.py

#a. pozisyonal parametre 
#b. isimli parametre
#c. varsayılan değer alan parametre

# bir fonksiyon çağrısında iki şekilde parametre gönderilir:
# eğer bir fonksiyon çağırısında isimli parametre kullanılırsa sonrasıda isimli parametre kullanımı olmalıdır.

# print(sep="-","merhaba") # hatalı çağrı: çünkü sep parametresi isimli olarak çağrıldı
print("merhaba",sep="-") #

def bisey(a,b,c):
    print("a:",a,"b:",b,"c:",c)
    
bisey(3,5,6) # pozisyonel parametre
bisey(c=5,a=2,b=8)  #isimsel parametre
bisey(3,b=8,c=10)
# bisey(25,a=20,c=80)# X hatalı kullanım
# bisey(a=5,10,20)#X hatalı kullanımisimsel başlarsan isimsel gitmelisin


def bisey2(a=5,b=10,c=20.0):
    print("bişey2")
    print("a:",a,"b:",b,"c:",c)
    

bisey2(2)
bisey2(3,5)
bisey2(10,20,30)


