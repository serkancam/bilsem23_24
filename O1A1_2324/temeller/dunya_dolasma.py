yari_cap=6378
parker_hizi=150
e_cevre = 2*3.14*yari_cap
e_sure = e_cevre/150
e_dakika = e_sure//60
e_saniye=e_sure%60
print(f"ekvatoru {e_dakika} dakika {e_saniye} saniyede dolaşır.")

k_yaricap=6357
k_cevre = 2*3.14*k_yaricap
k_sure = k_cevre/150
k_dakika = k_sure//60
k_saniye=k_sure%60