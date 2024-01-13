#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import random
from os import path

WIDTH = 480
HEIGHT = 600
FPS = 30
CAPTION = "Shoot'em Up!"

# Kullanışlı renklerini tanimlanması
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# pygame öğelerinin ilklenmesi ve perncere yaratılması
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
# set up assets folder
img_folder = path.join(path.dirname(__file__), "img")
vec = pygame.math.Vector2


# Oyunda kullanılan sınıflar
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.pos = vec(self.rect.x, self.rect.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.acc.x = -0.5

        if keystate[pygame.K_RIGHT]:
            self.acc.x = 0.5

        self.acc += self.vel * (-0.06)  # fren etkisi, kayma
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

 

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = meteor_img
        # self.image_orig.set_colorkey(WHITE)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)

        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedY = random.randrange(1, 8)
        self.speedX = random.randrange(-3, 3)
        self.rot = 0    
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        # print(now - self.last_update)
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + (self.speedX) * 3) % 360
            self.image = pygame.transform.rotate(self.image_orig, self.rot)

    def update(self):
        self.rotate()
        self.rect.y += self.speedY
        self.rect.x += self.speedX

        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedY = random.randrange(1, 8)

        if self.rect.left > WIDTH + 1 or self.rect.right < -1:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedY = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedY = -10

    def update(self):
        self.rect.y += self.speedY
        if self.rect.bottom < 0:
            self.kill()


# Load all game graphics
background = pygame.image.load(path.join(img_folder, "starfield.png"))
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_folder, "playerShip1_orange.png"))
meteor_img = pygame.image.load(path.join(img_folder, "meteorBrown_med1.png"))
bullet_img = pygame.image.load(path.join(img_folder, "laserRed16.png"))


all_sprites = pygame.sprite.Group()  # Bütün parçlar için oluşturulan grup
mobs = pygame.sprite.Group()        # Göktaşları için oluşturulan grup
bullets = pygame.sprite.Group()  # kurşunlar için oluşturulan grup

player = Player()
all_sprites.add(player)

for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
# Oyun döngüsü
running = True
while running:
    # kepp loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)

    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # check to see if a mon hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        print("Vuruldun")
        # running = False

    # Draw / Render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

# Oyundan çıkılması
pygame.quit()
