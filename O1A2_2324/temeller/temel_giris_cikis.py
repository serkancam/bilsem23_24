# temel_giris_cikis.py
# TemelGirisCikis.py
print("\\n")
print(" merhaba \"selam\" ")
print(' merhaba "selam" ')
print(" merhaba 'selam' ")
print(' merhaba \'selam\' ')
print(""" selam
      ben açıklama metni""")
print(''' ben ve diğer üçlü tırnak kullanımı
      fonksiyon ve sınıf tanımında kullanılırım. ''')

end="test"
print("birşey","iki şey","üç şey",sep=" ",end="\n")

ad=input("ad:")
soyad=input("soyad:")
print(f"merhaba {ad.capitalize()} {soyad.upper()} hoşgeldin.")#**
print("merhaba",ad,soyad,"hoşgeldin.")

liste=["ali","berk","kuzey","ege","ahmet","ömer","yusuf","aslan"]
print(*liste)
print(liste)
