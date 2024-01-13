# idareci,öğretmen,öğrenci,veli,memur,çalışan
# bunların ortak özellikleir vardır.
# adı,soyadı,cinsiyet,yaşı


class Kisi():
    def __init__(self) :
        self.ad=""
        self.soyad=""
        self.cinsiyet=""
        self.yas=0
    def yazdir(self):
        print(self.ad,self.soyad)
class Ogrenci(Kisi):#Ogrenci sınıfı  Kisi sınıfının miras alır.
    pass
class Ogretmen(Kisi): #Ogretmen sınıfı Kisi sınıfını miraz aldı.
    pass

ali=Kisi()
ali.ad="ali"
ali.soyad="can"
ali.yazdir()

can=Ogrenci()
can.ad="can"
can.soyad="gül"
can.yazdir()