# parker_dolasma.py
kutup_r= 6357
ekvator_r=6378
parker_hizi=150
pi=3.14

print("test"+" exam")
print("abra "*3)

ekvator_cevresi = 2*pi*ekvator_r

zaman=ekvator_cevresi/parker_hizi

ekvator_dakika = zaman//60
ekvator_saniye=zaman%60
print(f"parker ekvator yarıçağını {ekvator_dakika} dakika {round(ekvator_saniye,2)} saniye")