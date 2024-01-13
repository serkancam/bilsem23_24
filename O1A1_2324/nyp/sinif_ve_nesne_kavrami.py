# sinif_ve_nesne_kavrami.py

# nesne yönelimli programlama(object orinted programing-OOP)
# Bu programlama yaklaşımında amaç, varlıkların *davranış ve *özelliklerini temsil edecek şablon oluşturacak tasarımlar yaparak; bunlardan nesne türetme yoluyla yararlanmaktır.
# En büyük avantajı tekrar kullanılabilirlik ve bakım kolaylığıdır.
# sınıf(class): sınıflar varlık şablonları.
# nesne (object): nesneler varlıkların kendileridir.

#oyuncu sınıf tanımalaması

class oyuncu():
    def __init__(self,ad1,can1=100,saldiri1=10) :#yapıcı method
        print("ben yapıcı method.",ad1,"için çalıştım")
        self.ad=ad1
        self.can=can1
        self.saldiri=saldiri1
        self.tur=None
    def saldiri_yap(self,dusman):
        print(f"{self.ad} saldırıyor... {dusman.ad}")
        dusman.hasar_al(self.saldiri)
    def hasar_al(self,kayip):
        self.can=self.can-kayip
# a isminde bir sınıf türetelim
# a sınıfının yapıcı methodu(fonksiyonu) çalışarak bir nesne türetir ve a değişkenine aktarır.
# a artık oyuncu sınıfına ait bir nesnedir.
a = oyuncu("a oyuncusu",can1=150)
a.tur="cancı"
# b isminde bir nesne türeteli
b = oyuncu("b oyuncusu")
b.tur="saldırıcı"
c=oyuncu("c oyuncusu")
c.tur="buyucu"
print(c.ad,c.can)
a.saldiri_yap(c)
print(c.ad,c.can)

print(a.ad,a.can)
c.saldiri_yap(a)
c.saldiri_yap(a)
print(a.ad,a.can)
# print(a.ad,a.can)

# print(a.ad,a.can)
# print(b.ad,b.can)

# print(type(a),type(b),type(c))


# öğrenci varlığının *adını, *soyadını, *okul numarasını, *devamsızlık sayısı tutan ve aynı zamanda devamsılık yap tığığında, adlığı parametre değeri kadar devamsızlık sayısını artıran sınıfı tanımlayınız.

class ogrenci():
    def __init__(self) :
        self.ad=str()#""
        self.soyad=""
        self.okul_no=int()
        self.devamsizlik=0
    def devamsizlik_yap(self,gun):
        self.devamsizlik+=gun

# sınıf içinde tanımlanmış fonskiyona method deniz
ogrenci1=ogrenci()

ogrenci1.ad="ali"
ogrenci1.soyad="can"
ogrenci1.okul_no=158
print(ogrenci1.ad,ogrenci1.soyad,ogrenci1.devamsizlik)
ogrenci1.devamsizlik_yap(3)
print(ogrenci1.ad,ogrenci1.soyad,ogrenci1.devamsizlik)