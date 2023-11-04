# takdir_alma_durumu.py
# kullanıcı şu üç bilgiyi girecek
# Türkçe dersi ortalaması
# Genel ortalama
# devamsılık gün sayısı

# takdir alma şartı: Türkçe dersi ortalaması 70 veya üstü, genel ortalama 90 veya üstü, devamszlık ise 10 günden az olmalıdır.

tdo = float(input("Türkçe dersi ortalaması:"))
gdo = float(input("Genel ders ortalaması:"))
devms = float(input("Devamsızlık sayıs:"))

if tdo>=70 and gdo>=90 and devms<10:
    print("takdir aldınız:")
else:
    print("takdir alamadınız.")