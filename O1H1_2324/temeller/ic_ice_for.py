
for dis in range(0,3,1): # 0 1 2 
    for ic in range(10,13,1): # 10 11 12
        print(f"{dis}:{ic}")
        
print(30*"*")

# 0:0
# 0:1
# 0:2
#....
# 0:59
# 1:00
# 1:01
# 1:02
# 1:59
# 2:00
# .....
# 23:59
import os
import time

for saat in range(0,23,1):
    for dakika in range(0,60,1):
        print(saat,":",dakika)
        # time.sleep(0.02)
        # os.system("clear")