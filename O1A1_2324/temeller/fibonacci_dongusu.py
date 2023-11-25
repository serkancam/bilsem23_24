# fibonacci_dongusu.py

adim = int(input("fibonacci adımı:"))

f1=1
f2=1

for a in range(3,adim+1,1):
    t=f2
    f2=f2+f1
    f1=t
print(f"{adim} daki fibonacci değeri:{f2}")   

    
# #####3. adım
# t=f2
# f2=f1+f2
# f1=t
# print("3. adım",f2)
# #####4. adım
# t=f2
# f2=f1+f2
# f1=t
# print("4. adım",f2)
# #####5. adım
# t=f2
# f2=f1+f2
# f1=t
# print("5. adım",f2)

