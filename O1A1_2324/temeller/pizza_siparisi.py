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
zeytin_durum= input("zeytin e/h:")
biber_durum= input("biber e/h:")
mantar_durum= input("mantar e/h:")
sosis_durum= input("sosis e/h:")
sucuk_durum= input("sucuk e/h:")

if zeytin_durum=="e":
    fiyat+=zeytin# fiyat=fiyat+zeytin
if biber_durum=="e":
    fiyat+=biber
if mantar_durum=="e":
    fiyat+=mantar
if sosis_durum=="e":
    fiyat+=sosis
if sucuk_durum=="e":
    fiyat+=sucuk
    
print(f"fiyat:{fiyat}")