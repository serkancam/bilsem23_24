# kullanıcı türkçe dersinin ortalamasını, diğer derslerin ortalamasını ve devamsızlık yaptığı gün sayısını girerek takdir alıp almadığını belirlemek istiyor. 
# buna göre Türkçe dersi 70 veya üstü, genel ortlama 90 veya üstü devamsızlık sayısı 10 dan az olduğu durumda True sonuç diğer durumlarda False sonuç veren mantıksal ifadeyi yazınız.

tdo=float(input("Türkçe dersi ortalaması:"))
gdo=float(input("Genel ders ortalaması:"))
devamsizlik=float(input("Özürsüz devamsızlık sayısı:"))

takdir = (tdo>=70) and (gdo>= 90) and (devamsizlik<10)

print(f"durum:{takdir}")