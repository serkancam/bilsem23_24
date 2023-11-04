# pizza_siparisi.py
# temel malzeme
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

boyut = input("pizza boyutu(k/o/b):")
if boyut=="k":
    fiyat=fiyat*1
elif boyut=="o":
    fiyat=fiyat*2
elif boyut=="b":
    fiyat=fiyat*2.5

biberd = input("biber e/h:")
zeytind = input("zeytin e/h:")
mantard = input("mantar e/h:")
sosisd=input("sosis e/h")
sucukd=input("sucuk e/h")

if biberd=="e":
    fiyat=fiyat+biber
if zeytind=="e":
    fiyat=fiyat+zeytin
if mantard=="e":
    fiyat=fiyat+mantar


print(f"pizzanızın fiyatı:{fiyat}")