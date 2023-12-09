# fonksiyonlar_parametre_gonderme.py

# çağırma anı
# a. pozisyonel(positional) paramtere gönderimi
# b. isimli(named) parametre gönderimi
# c. karışık parametre gönderimi
# tanımlama anı

def bisey(a,b,c):
    print(f"a:{a}-b:{b}-c:{c}")
    
bisey(4,3,8) # pozisyonel
bisey(c=8,a=10,b=20) # isimli
# fonksiyon çağırısında soldan sağa parametrelere değer gönderilirken eğer bir parametre isimli paramtre almışsa artık ondan sonra sağına gelecek her parametre isimli çağrılmalıdır.
bisey(3,b=8,c=10) # karışık
# bisey(20,b=20,35) # hatalı
# bisey(10,a=8,c=90) # hatalı

# varsayılan(default) değer

def bisey2(a=1,b=3,c=2):
    print("bisey2")
    print(f"a:{a}-b:{b}-c:{c}")
    
bisey2()
bisey2(85)

print("ali","yaman")
print("ali","yaman",sep="@")