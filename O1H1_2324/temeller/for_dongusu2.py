import os
import time

os.system("clear")
while True:
    metin="Mustafa Kemal ATATÜRK"
    for i in range(50):
        metin=" "+metin
        print(metin)
        time.sleep(0.05)
        os.system("clear")
    for i in range(50):
        metin=metin[1:]
        print(metin)
        time.sleep(0.05)
        os.system("clear")
