#fibonacci

sira =int(input("sıra:"))

fib1=1
fib2=1

i=3
while i<=sira:
    # yedek=fib2
    # fib2=fib1+fib2
    # fib1=yedek
    fib2,fib1=fib2+fib1,fib2
    print(i)
    i=i+1

print(f"{sira}. adım fibonacci değeri:{fib2}")





