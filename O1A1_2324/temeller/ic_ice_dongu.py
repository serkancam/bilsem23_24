# ic_ice_dongu.py

# print("1*1=1")
# print("1*2=2")
# print("1*3=3")
# print("2*1=2")
# print("2*2=4")
# print("2*3=6")

# print(30*"-")
# for dis in range(1,30,1): #1,2
#     for ic in range(1,40,1):#1,2,3
#         print(f"{dis}*{ic}={dis*ic}")


# print(30*"-")
# for saat in range(24):
#     for dakika in range(60):
#         print(f"{saat}:{dakika}")
"""
00:00
00:01
00:02
...
23:59
"""        
"""
0:0
0:1
0:2
...
23:59
"""

s=0
d=0
while s<24:
    d=0
    while d<60:
        print(f"{s}:{d}")
        d=d+1
    s=s+1
