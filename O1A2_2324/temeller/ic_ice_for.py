for s1 in range(0,20,2):# 0 2 4 6 8 10 12 14 16 18 
    for s2 in range(1,5,1): # 1 2 3 4
        print(f"{s1}:{s2}")
        

#saat:dakika
#0.0
#0.1
#0.2
#...
#0.59
#1.0
#1.1
#...
#1.59
#2.0
#2.1
#...
#23.59
import os
import time
for saat in range(0,24,1):
    for dakika in range(0,60,1): 
        for saniye in range(60):               
            os.system("clear")
            print(saat,":",dakika,":",saniye)
            time.sleep(1)
            

