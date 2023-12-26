def cop_adam_ciz(deger:int):
    if deger==1:
        print("  0  ")
    elif deger==2:
        print("  0  ")
        print("  |  ")
    elif deger==3:
        print("  0  ")
        print("  |  ")
        print("  |  ")
    elif deger==4:
        print("  0  ")
        print(" /|  ")
        print("  |  ")
    elif deger==5:
        print("  0  ")
        print(" /|\ ")
        print("  |  ")
    elif deger==6:
        print("  0  ")
        print(" /|\ ")
        print("  |  ")
        print(" /   ")
    elif deger==7:
        print("  0  ")
        print(" /|\ ")
        print("  |  ")
        print(" / \ ")

if __name__=="__main__":
    deger = int(input("deger:"))
    cop_adam_ciz(deger)