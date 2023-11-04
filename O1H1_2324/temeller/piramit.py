ts = int(input("tuğla sayısı:"))
# ks=1

# while ks<=ts:
#     ts = ts-ks
#     ks=ks+1

# print(f"{ks-1} kat çıkılabilir.")

ks=0
kts=0

while kts<=ts:
    ks=ks+1
    kts=kts+ks
    
print(ks-1)

