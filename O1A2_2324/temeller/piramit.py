#piramit.py

ts = int(input("Tuğla sayısı:"))
ks=1

while ts>=ks:
    ts=ts-ks
    

    ks=ks+1
else:
    ks=ks-1

i=1
while i<=ks:
    print((ks-1)*" ",end="")
    print(ks*"\U0001F9F1",end="")
    i=i+1
print()

print(f"{ks} kat oluştu.")