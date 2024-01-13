#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import random
import os
pygame.sprite.Sprite()

WIDTH = 800
HEIGHT = 600
FPS = 30
CAPTION = "iskelet Kod"

# Kullanışlı renklerini tanimlanması
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")


# Oyunda kullanılan sınıflar
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder,"p1_jump.png")).convert()
		self.image.set_colorkey(BLACK)#oluşan arka plan rengini transparan yapar
		# self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.ySpeed = 5
	def update(self):
		self.rect.x += 5
		self.rect.y += self.ySpeed
		if self.rect.bottom > HEIGHT - 200:
			self.ySpeed = -5
		if self.rect.top < 200:
			self.ySpeed = 5
		if self.rect.left > WIDTH:
			self.rect.right = 0
		

# pygame öğelerinin ilklenmesi ve perncere yaratılması
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(CAPTION)
saat = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
# Oyun döngüsü
running = True
while running:
	# Oyun akış hızının belirlenmesi
	saat.tick(FPS)
	# Giriş işlemeleri (olaylar)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Update
	all_sprites.update()

	# Çizme / Escreen tazeleme
	screen.fill(BLACK)
	all_sprites.draw(screen)

	# herşeyin çizimi işleminden sonra , ekranın tazelenmesi
	pygame.display.flip()

# Oyundan çıkılması
pygame.quit()



