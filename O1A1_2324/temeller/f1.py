# yarıçap değerini parametre/argüman olarak alıp daire çevresi hesaplayan ve ekranaa yazdıran fonksiyonu tanımlayınız
def daire_cevre_bul(r:float):
    cevre = 2*3.14*r
    print(f"{cevre}")

# yarıçap değerini parametre/argüman olarak alıp daire alanı hesaplayan ve ekranaa yazdıran fonksiyonu tanımlayınız
def daire_alani_bul(r:float):
    alan=3.14*r**2
    print(f"{alan}")

# bir dikdörtgenin kısa ve uzun kenar bilgilerini alıp dikdörtgen çevresini hesaplayan ve ekranaa yazdıran fonksiyonu tanımlayınız
def dortgen_cevresi(kk:float,uzk:float):
    cevre = (kk+uzk)*2
    print(f"{cevre}")

# bir dikdörtgenin kısa ve uzun kenar bilgilerini alıp dikdörtgen alanını hesaplayan ve ekrana yazdıran fonksiyonu tanımlayınız

def dortgen_alani(kk:float,uzk:float):
    alan = kk*uzk
    print(f"alan:{alan}")
    

