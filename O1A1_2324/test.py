#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
import pygame.font
from pygame.locals import *
from enum import Enum
import random
import time
import locale
# locale.setlocale(locale.LC_ALL,'tr_TR.utf8')


## Renk tanımları
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLUE1 = (15,69,75)
BLUE2 = (106,144,147)
BGCOLOR= BLACK

# Yönler

# UP = 'up'
# DOWN = 'down'
# LEFT = 'left'
# RIGHT = 'right'
## Ekran değerleri ayarla
WIDTH = 640
HEIGHT = 480
FPS = 8
CAPTION = "Yılan Oyunu"
CELLSIZE = 20
CELLWIDTH = int(WIDTH/CELLSIZE)
CELLHEIGHT = int(HEIGHT/CELLSIZE)
running = False
puan=int()
## Pygame başlangıç ayarları ve pencere oluşturma

pygame.font.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
font=pygame.font.Font(None, 18)

# oyunda kullanılacak sınıflar
class Yonler(Enum):
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
class Yilan():
    def __init__(self,renk=GREEN):
        self.yilan=[{"x":CELLWIDTH/2,"y":CELLHEIGHT/2},{"x":CELLWIDTH/2+1,"y":CELLHEIGHT/2},{"x":CELLWIDTH/2+2,"y":CELLHEIGHT/2}]
        self.yon=Yonler.LEFT
        self.__renk=renk
    def degerHesapla(self):
        don = False
        i=len(self.yilan)-1
        # print(self.yilan)
        while i >= 1:
            x,y=self.yilan[i-1]["x"],self.yilan[i-1]["y"],
            self.yilan[i] = {"x":x,"y":y}
            # print(self.yilan)
            i-=1
        if self.yon == Yonler.DOWN:
            self.yilan[0]["y"] = self.yilan[0]["y"] + 1
        if self.yon == Yonler.UP:
            self.yilan[0]["y"] = self.yilan[0]["y"] - 1
        if self.yon == Yonler.RIGHT:
            self.yilan[0]["x"] = self.yilan[0]["x"] + 1
        if self.yon == Yonler.LEFT:
            self.yilan[0]["x"] = self.yilan[0]["x"] - 1

        if self.yilan[0]["x"] > CELLWIDTH or self.yilan[0]["y"] > CELLHEIGHT or\
         self.yilan[0]["x"] < 0 or self.yilan[0]["y"] < 0 :
            return True
        i=1
        while i<len(self.yilan):
            if self.yilan[0]["x"] == self.yilan[i]["x"] and \
            self.yilan[0]["y"] == self.yilan[i]["y"]:
                return True  
            i += 1 

        return False
    def parcaEkle(self):
        x,y = self.yilan[len(self.yilan)-1]["x"],self.yilan[len(self.yilan)-1]["y"]
        if self.yon == Yonler.LEFT:
            parca = {"x":x+1,"y":y}
            self.yilan.append(parca)
        if self.yon == Yonler.RIGHT:
            parca = {"x":x-1,"y":y}
            self.yilan.append(parca)
        if self.yon == Yonler.UP:
            parca = {"x":x,"y":y+1}
            self.yilan.append(parca)
        if self.yon == Yonler.DOWN:
            parca = {"x":x,"y":y-1}
            self.yilan.append(parca)



    def yilanCiz(self):
        for parca in self.yilan:
            x=parca["x"]*CELLSIZE
            y=parca["y"]*CELLSIZE
            pygame.draw.rect(screen,self.__renk,[x,y,CELLSIZE,CELLSIZE])
class Yem():
    def __init__(self,renk=RED):
        self.x = 10
        self.y = 10
        self.__renk = renk

    def yemCiz(self,yln,drm):
        while drm:
            buldum = True
            self.x = random.randint(0,CELLWIDTH-1)
            self.y = random.randint(0, CELLHEIGHT-1)
            for parca in yln:
                if parca["x"] == self.x and parca["y"] == self.y:
                    buldum = False
                    break
            if buldum:
                break
        pygame.draw.rect(screen,self.__renk,[self.x*CELLSIZE,self.y*CELLSIZE,CELLSIZE,CELLSIZE])

#Oyunda kullanılcak Fonksiyonlar
def ekranaYaz(mesaj,x,y,pt=12,yaziRengi=WHITE,arkaPlanRengi=BGCOLOR):
    font=pygame.font.Font(None, pt)
    yazi=font.render(u''+mesaj,True,yaziRengi,arkaPlanRengi)
    yaziKaresi=yazi.get_rect()
    yaziKaresi.center=(x/2,y/2)
    screen.blit(yazi,yaziKaresi)
    #pygame.display.flip()
    pygame.display.update()

def izgaraCiz():
    for x in range(0,WIDTH,CELLSIZE):
        pygame.draw.line(screen,DARKGRAY,(x,0),(x,HEIGHT))
    for y in range(0,HEIGHT,CELLSIZE):
        pygame.draw.line(screen,DARKGRAY,(0,y),(WIDTH,y))


def main():
    global running,FPS,screen
    # running =True
    girisEkrani()
    while running:
        oyun()
        oyunSonu()


def girisEkrani():
    global running,FPS
    fontG= pygame.font.Font(None,200)
    render1=fontG.render("Snake",True,WHITE,DARKGREEN)
    render2=fontG.render("Snake",True,GREEN)
    aci1=0
    aci2=0
    screen.fill(BGCOLOR)
    clock.tick(FPS)
    running=True
    while running:
        for event in pygame.event.get():
    #check for closing window
            if event.type == pygame.QUIT:
                # print("Giriş Ekranı")
                running=False
                return
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running = False
                else:
                    return

        screen.fill(BGCOLOR)

        rotate1=pygame.transform.rotate(render1,aci1)
        rect1=rotate1.get_rect()
        rect1.center=(WIDTH/2,HEIGHT/2)
        screen.blit(rotate1,rect1)

        rotate2=pygame.transform.rotate(render2,aci2)
        rect2=rotate2.get_rect()
        rect2.center=(WIDTH/2,HEIGHT/2)
        screen.blit(rotate2,rect2)
        ekranaYaz(u"Başlamak için enter Tuşuna basınız",WIDTH,40,30)
        aci1+=0.8
        aci2+=2
        pygame.display.update()

def oyun():

    #oyunda kullanılacak nesnelerin ilk başlatılması oyunda kullanışacak değişkenler
    global running,FPS,puan
    puan = 0
    FPS = 8
    yilan=Yilan(GREEN)
    yem=Yem(RED)
    yilan.yilanCiz()
    running = True
    while running:
        drm = False
        ## keep loop running at the right speed
        #oyun hızının ayarlanması
        clock.tick(FPS)
        ## Process inputs(events)
        for event in pygame.event.get():
            #check for closing window
            if event.type == pygame.QUIT:
                # print("Oyun")
                running=False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    print("escape")
                if event.key == pygame.K_LEFT:
                    if yilan.yon != Yonler.RIGHT:
                        yilan.yon=Yonler.LEFT
                if event.key == pygame.K_UP:
                    if yilan.yon != Yonler.DOWN:
                        yilan.yon = Yonler.UP
                if event.key == pygame.K_DOWN:
                    if yilan.yon != Yonler.UP:
                        yilan.yon = Yonler.DOWN
                if event.key==pygame.K_RIGHT:
                    if yilan.yon != Yonler.LEFT:
                        yilan.yon = Yonler.RIGHT
            if event.type==pygame.KEYUP:
                pass

        ## update
        #Oyunda kullanılan nesnelerin değerlerinin değiştirilmesi x,y ses, renk vb


        if yilan.degerHesapla():
            running = False
            return
        if yilan.yilan[0]["x"] == yem.x and yilan.yilan[0]["y"] == yem.y:
            drm = True
            puan += 1
            FPS += int(puan/5)
            yilan.parcaEkle()


        ## draw/render
        #oyunda kullanılacak nesnelerin güncellenmiş değelere göre çizilmesi

        screen.fill(BGCOLOR)
        izgaraCiz()
        yilan.yilanCiz()
        yem.yemCiz(yilan.yilan,drm)
        ekranaYaz(u"Skor:"+str(puan),(WIDTH*2)-(CELLSIZE*8),40,26)

        #ekranın tekrar yeni çizimler ile güncellenmesi
        pygame.display.update()#pygame.display.flip()
    # pygame.quit()

def oyunSonu():
     global running,FPS
     running = True
     while  running:
        clock.tick(FPS)
        ## Process inputs(events)
        for event in pygame.event.get():
            #check for closing window
            if event.type == pygame.QUIT:
                # print("Oyun")
                running=False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    print("escape")
                if event.key == pygame.K_SPACE:
                    return
        screen.fill(BGCOLOR)
        ekranaYaz(u"Oyun Bitti",WIDTH,40,30)
        ekranaYaz(u"Tekrar başlamak için 'Space' tuşuna basınız", WIDTH, 100,30,GREEN)
        pygame.display.update()#pygame.display.flip()




## oyun döngüsü
if __name__ == "__main__":
    main()
    screen.fill(BGCOLOR)
    pygame.display.flip()
    pygame.quit()