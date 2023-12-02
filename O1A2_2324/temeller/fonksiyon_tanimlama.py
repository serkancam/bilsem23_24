# tanımlama(definition) ve çağırma(call)

def selam_yaz(deger:str):
    print("merhaba",deger)

selam_yaz("serkan")
ad="bilsem"
selam_yaz(ad)

def ucgen_cevre_bul(a:float,b:float,c:float):
    cevre=a+b+c
    print(cevre)
    
def ucgen_cevre_bul2(a:float,b:float,c:float):
    cevre=a+b+c
    return cevre
ucgen_cevre_bul(4,2,3)

print(ucgen_cevre_bul2(3,2,5))

ucgen_cevre_bul(3,4,3)




