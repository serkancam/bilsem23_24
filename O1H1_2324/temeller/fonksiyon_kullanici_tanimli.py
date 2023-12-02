# fonksiyon_kullanici_tanimli.py

# bir fonksiyon tanımlanır(definition) ve çağrılır(call). Tanımlanmayan fonksiyonlar doğal olarak çağırılımaz.

# çağrılınca ekrana merhaba yazan selam_yaz() foknsiyonu tanımlayalım.
# tanımlamalar
def selam_yaz():
    print("merhaba")   
    
selam_yaz()
def selam_yaz_isme(a:str):
    print("merhaba",a)
    
    
# parametre olarak iki iç açı değerini aldığın üçgenin 3. iç açısını bulup ekrana yazdıran fonksiyonu tanımlayınız.

def ucuncu_aci_bul(a1:float,a2:float):
    a3 = 180-(a1+a2)
    print("3. açı:",a3)

def cop_adam():
    print("  0  ")
    print(" /|\ ")
    print("  |  ")
    print(" / \ ")

#çağırmalar
cop_adam()
cop_adam()
ucuncu_aci_bul(40,50)
ucuncu_aci_bul(70,30) 
ucuncu_aci_bul(40,30) 
ucuncu_aci_bul(100,30) 
ucuncu_aci_bul(70,90) 
selam_yaz()
selam_yaz()
selam_yaz_isme("serkan")
deger="bilsem"
selam_yaz_isme(deger)
selam_yaz_isme("edirne")


