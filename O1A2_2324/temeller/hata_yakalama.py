# hata_yakalama.py
try:
    s1=float(input("s1:"))
    s2=float(input("s2:"))
    islem = s1/(s2-3)
    print(islem)
except ZeroDivisionError:
    print("sıfıra bölme hatası.")
except FileExistsError:
    print("bu hata burada hayatta olmaz.")
except Exception as ex:
    print("hata oldu:",ex)
else:
    print("hata olmadı")
finally:
    print("ben her zaman çalışırım.")
    


print("bundan sonraı hep çalışır.")