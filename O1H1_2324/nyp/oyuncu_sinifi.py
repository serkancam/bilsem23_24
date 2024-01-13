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
        

a=oyuncu("oyuncu1",100,10,"elf")
b=oyuncu("oyuncu2",110,15,"buyucu")
c=oyuncu("oyuncu3",105,10,"insan")

a.yazdir()
b.saldir(a)