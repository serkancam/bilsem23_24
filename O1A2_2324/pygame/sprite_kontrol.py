#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any
import pygame
import random



GENISLIK = 360
YUKSEKLIK = 480
FPS = 60
BASLIK = "iskelet Kod"

# Kullanışlı renklerini tanimlanması
BEYAZ = (255, 255, 255)
SIYAH = (0, 0, 0)
KIRMIZI = (255, 0, 0)
YESIL = (0, 255, 0)
MAVI = (0, 0, 255)

# pygame öğelerinin ilklenmesi ve perncere yaratılması
pygame.init()
pygame.mixer.init()
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption(BASLIK)
saat = pygame.time.Clock()
# oyunda kullanılacak sınıflar
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,38))
        self.image.fill(YESIL)
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        self.x_speed=0
        self.y_speed=0
    def update(self):
        self.x_speed=0
        self.y_speed=0
        tuslar=pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT]:
            self.x_speed=-5
        elif tuslar[pygame.K_RIGHT]:
            self.x_speed=5
        if self.rect.right==0:
            self.rect.left=GENISLIK
        elif self.rect.left==GENISLIK:
            self.rect.right=0
        self.rect.x+=self.x_speed
    def shoot(self):
        kursun=Bullet(self.rect.centerx,self.rect.top)
        hepsi.add(kursun)
        kursunlar.add(kursun)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,30))
        self.image.fill(KIRMIZI)
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.y_speed=-10
    def update(self):
        self.rect.y+=self.y_speed
        if self.rect.bottom<0:
            self.kill()
              
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 30])
        self.image.fill(KIRMIZI)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(5, GENISLIK-self.rect.width)
        self.rect.bottom = 0
        self.y_speed = random.randint(3, 8)
    def update(self):
        self.rect.y += self.y_speed
        if self.rect.top >= YUKSEKLIK:
            self.rect.x = random.randint(5, GENISLIK-self.rect.width)
            self.rect.bottom = 0
            self.y_speed = random.randint(3, 8)       
#grup tanımlamaları
hepsi=pygame.sprite.Group()
kursunlar=pygame.sprite.Group()
meteorlar=pygame.sprite.Group()

#nesnelerin tanımlanması ve gruba eklenmesi
oyuncu=Player(GENISLIK//2,YUKSEKLIK-40)
for i in range(5):
    m=Meteor()
    hepsi.add(m)
    meteorlar.add(m)

hepsi.add(oyuncu)
    
    
# Oyun döngüsü
calisma = True
def oyun():
    global calisma
    while calisma:
        # Oyun akış hızının belirlenmesi
        saat.tick(FPS)
        # Giriş işlemeleri (olaylar)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                calisma = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    oyuncu.shoot()

        # Güncelleme
        
        #hesaplamalara göre güncelle
        hepsi.update()
        # kurşun meteor vurdu ise:
        durumlar = pygame.sprite.groupcollide(meteorlar,kursunlar,True,True)
        for durum in durumlar:
            m=Meteor()
            hepsi.add(m)
            meteorlar.add(m)
        
        # Çizme / Ekranı tazeleme
        ekran.fill(BEYAZ)
        hepsi.draw(ekran)

        # herşeyin çizimi işleminden sonra , ekranın tazelenmesi
        pygame.display.flip()


# Oyundan çıkılması
if __name__=="__main__":
    oyun()
    pygame.quit()
