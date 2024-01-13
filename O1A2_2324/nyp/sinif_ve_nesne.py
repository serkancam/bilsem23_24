# sinif_ve_nesne.py
class oyuncu():# eğer miras alınmayacaksa parantezler olmayabilir.
    def __init__(self,ad,can=0,guc=0,tur="") :#nesnelere aktarılacak özellikleri burada tanımlarız.
        self._ad=ad
        self._can=can
        self._guc=guc
        self._tur=tur
        #self anahtar kelimesi sınıf içinde, sınıftan türetilen nesneleri işaret eder        
    def saldir(self,kime):# eğer sınıf içinde nesne için bir method tanımlanacaksa parantez içinde self olmalıdır
        kime.hasar_al(self._guc) 
        kime.yazdir()       
    def hasar_al(self,kayip):
        if self._can-kayip>=0:
            self._can-=kayip
    def yazdir(self):
        print(self._ad,self._can,self._guc,self._tur)
      
a=oyuncu("a oyuncusu",100,10,"ork")
# a._ad="a oyuncusu"
# a._can=100
# a._guc=20
# a._tur="ork"
# listem=list()
# b oyuncusu
c=oyuncu("c oyuncusu",150,5,"elf")
b=oyuncu("b oyuncusu",120,20,"buyucu")
# a.yazdir()
# b.yazdir()
a.saldir(b)
# b.yazdir()
karakterler=list()
import random
turler={"insan":10,"ork":5,"elf":20,"buyucu":15}


for i in range(100):
    sec=random.choice(list(turler))
    kr=oyuncu(f"{i}. oyuncu",random.randint(90,110),turler[sec],sec)
    karakterler.append(kr)
    
for k in karakterler:
    k.yazdir()
    