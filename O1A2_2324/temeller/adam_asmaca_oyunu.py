import random
import os
import cop_adam
tahminler=[]
bilinenler=list()
hak=0
dosya=open("temeller/ulkeler.txt",mode="r",encoding="utf-8")
secilen=random.choice(dosya.readlines()).lower()
print(secilen)
dosya.close()
os.system("clear")
def yazdir(secilen:str,bilinenler:list,hak:int):
    os.system("clear")
    cop_adam.karakter_ciz(hak)
    yazilacak=""
    for h in secilen:
        if h==" ":
            yazilacak=yazilacak+" "
        elif h in bilinenler:
            yazilacak=yazilacak+h
        elif h=="\n":
            continue
        else:
            yazilacak=yazilacak+"_ "            
    print(yazilacak)
    return yazilacak   
yazdir(secilen,bilinenler,hak)
while True:#4. satır
    harf = input(f"{7-hak} hakkınız kaldı-->söylenmemiş bir harf giriniz:").lower()
    if harf=="-1":
        break
    elif len(harf)!=1 or (harf in tahminler) or (harf==""):
        yazdir(secilen,bilinenler,hak)
        continue
    elif not harf.isalpha():
        yazdir(secilen,bilinenler,hak)
        continue
    tahminler.append(harf)
    if harf in secilen:
        bilinenler.append(harf)
    else:
        hak+=1
      
    if "_" not in yazdir(secilen,bilinenler,hak):
        print("Tebrikler oyunu kazandın.")
        break
    elif hak==7:
        print("hakkınız bitti.")
        break