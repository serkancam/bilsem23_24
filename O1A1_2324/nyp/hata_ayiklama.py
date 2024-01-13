try:
    # dosya=open(file="test.txt",mode="r",encoding="utf-8")
    not1=float(input("1. sınavı gir:"))
    not2=float(input("2. sınavı gir:"))
    # a=3/0
    ort=(not1+not2)/2
    print("ortalamanız:",ort)
except Exception as e:
    print("hata oldu:",e)
else:
    print("hiç hata yok.")
finally:
    print("finally her zaman çalışır.")
    