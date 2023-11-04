# pizza_siparisi.py
hamur=10
peynir=20
sos=15
fiyat=hamur+peynir+sos
###############
biber=10
zeytin=15
mantar=20
sosis=25
sucuk=30
############
biber_durum = input("biber e/h:")
zeytin_durum = input("zeytin e/h:")
mantar_durum = input("mantar e/h:")
sosis_durum = input("sosis e/h:")
sucuk_durum = input("sucuk e/h:")
if biber_durum=="e":
    fiyat=fiyat+biber#fiyat+=biber
if zeytin_durum=="e":
    fiyat=fiyat+zeytin
if mantar_durum=="e":
    fiyat=fiyat+mantar
if sosis_durum=="e":
    fiyat=fiyat+sosis
if sucuk_durum=="e":
    fiyat=fiyat+sucuk
print(fiyat)


