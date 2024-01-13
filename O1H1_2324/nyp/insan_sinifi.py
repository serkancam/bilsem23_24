#insan_sinifi.py

class Insan():
    def __init__(self, ad, cinsiyet, boy, kilo):
        self.ad = ad
        self.cinsiyet = cinsiyet
        self.boy = boy
        self.kilo = kilo
    def __str__(self):
        return self.ad+" "+self.cinsiyet

a = Insan("ali","erkek",1.78,80) 
b = Insan("ayşe","kadın",1.75,62)
c = Insan("serkan","erkek",1.74,82)

print(c.ad)
print(c)
print(a)
print(b)

