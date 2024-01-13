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
RENGIM=(15,150,78)

# pygame öğelerinin ilklenmesi ve perncere yaratılması
pygame.init()
pygame.mixer.init()
ekran = pygame.display.set_mode((GENISLIK,YUKSEKLIK))
pygame.display.set_caption(BASLIK)
saat = pygame.time.Clock()
#Sprite/karakter sınıflarının yazılması
class Oyuncu(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,35])
        self.image.fill(RENGIM)
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        self.x_hizi=0
    def update(self):
        self.x_hizi=0
        tus_durumu=pygame.key.get_pressed()
        if tus_durumu[pygame.K_LEFT]:
            self.x_hizi = -5
        if tus_durumu[pygame.K_RIGHT]:
            self.x_hizi = 5
        
        self.rect.x += self.x_hizi
        
        # if self.rect.left<0:
        #     self.rect.left=0
        # elif self.rect.right>GENISLIK:
        #     self.rect.right=GENISLIK
        if self.rect.left>GENISLIK:
            self.rect.right=0
        elif self.rect.right<0:
            self.rect.left=GENISLIK
    def ates_et(self):
        k=Kursun(self.rect.centerx,self.rect.top)
        hepsi.add(k)
        kursunlar.add(k)
    
class Kursun(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([10,30])
        self.image.fill(YESIL)
        self.rect=self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.y_hizi= -10
    def update(self):
        self.rect.y += self.y_hizi
        if self.rect.bottom<0:
            self.kill()
        
    
        
        
        
        
       
# sprite grupları tanımlama ve nesne ekleme
hepsi = pygame.sprite.Group() 
kursunlar = pygame.sprite.Group()
meteorlar = pygame.sprite.Group()

oyuncu1=Oyuncu(GENISLIK//2,YUKSEKLIK-30)   

hepsi.add(oyuncu1)   
        

# Oyun döngüsü
calisma = True
while calisma:
    # Oyun akış hızının belirlenmesi
    saat.tick(FPS)
    # Giriş işlemeleri (olaylar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisma = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RCTRL:
                oyuncu1.ates_et()
                

    # Güncelleme
    hepsi.update()
    # Çizme / Ekranı tazeleme
    ekran.fill(BEYAZ)
    hepsi.draw(ekran)

    # herşeyin çizimi işleminden sonra , ekranın tazelenmesi
    pygame.display.flip()


# Oyundan çıkılması
pygame.quit()
