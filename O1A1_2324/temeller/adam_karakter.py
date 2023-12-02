def karakter():
    print("  0   ")
    print(" /|\  ")
    print("  |   ")
    print(" / \  ")
    
def karakter2():
    adam=""" 
  0
 /|\ 
  |
 / \ 
 """
    return adam
karakter()

print(karakter2())


def karakter_ciz(sayi:int):
    if sayi==1:
        print("  0   ")      
    elif sayi==2:
        print("  0   ")
        print("  |   ")        
    elif sayi==3:
        print("  0   ")
        print("  |   ")
        print("  |   ")        
    elif sayi==4:
        print("  0   ")
        print(" /|   ")
        print("  |   ")        
    elif sayi==5:
        print("  0   ")
        print(" /|\  ")
        print("  |   ")            
    elif sayi==6:
        print("  0   ")
        print(" /|\  ")
        print("  |   ")
        print(" /    ")
    elif sayi==7:
        print("  0   ")
        print(" /|\  ")
        print("  |   ")
        print(" / \  ")
        print("oyun bitti!! Kaybettin")

karakter_ciz(7)