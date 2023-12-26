# ortalama
# en küçük
# en büyük
# karışık sıralı
# artan sıralı
# azalan 
l1=[17,1999,1658,-300]
l2=[1400,1993,1453,1881,1903,17,150]
l1.sort()
l2.sort()
l1e=len(l1)
l2e=len(l2)
print(l1)
print(l2)

if l1e%2==1:
    # tek elemanlı
    ort_yeri=l1e//2
    ortanca=l1[ort_yeri]
else:
    # çift elemanlı
    ort_yeri=l1e//2
    ortanca=(l1[ort_yeri]+l1[ort_yeri-1])/2
print(ortanca)