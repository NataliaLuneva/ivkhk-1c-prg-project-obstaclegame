import pygame
import sys
from pygame.locals import *

pygame.init()

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fps = 60

tile_sz = 30


class Level():
    def __init__(self, data):
        self.tileL = []
        
        dirt = pygame.image.load('images/dirt.png')

        grass = pygame.image.load('images/grass.png')

        half_grass = pygame.image.load('images/halfGrass.png')

        countRow = 0
        for row in data:
            countCol = 0
            for tile in row:
                if tile == 1:
                    dirt_img = pygame.transform.scale(dirt, (tile_sz, tile_sz))
                    img_rect = dirt_img.get_rect()
                    img_rect.x = countCol * tile_sz
                    img_rect.y = countRow * tile_sz
                    tile = (dirt_img, img_rect)
                    self.tileL.append(tile)
                if tile == 2:
                    grass_img = pygame.transform.scale(grass, (tile_sz, tile_sz))
                    img_rect_grass = grass_img.get_rect()
                    img_rect_grass.x = countCol * tile_sz
                    img_rect_grass.y = countRow * tile_sz
                    tile = (grass_img, img_rect_grass)
                    self.tileL.append(tile)
      
                if tile == 8:
                    half_grass_img = pygame.transform.scale(half_grass, (tile_sz, tile_sz // 1.5))
                    img_rect_half = half_grass_img.get_rect()
                    img_rect_half.x = countCol * tile_sz
                    img_rect_half.y = countRow * tile_sz + (tile_sz // 2)
                    tile = (half_grass_img, img_rect_half)
                    self.tileL.append(tile)
                
                if tile == 3:
                    spikes = Spikes(countCol * tile_sz, countRow * tile_sz + (tile_sz // 2))
                    spikes_group.add(spikes)

                countCol += 1
            countRow += 1

    def draw(self):
        for tile in self.tileL:
            screen.blit(tile[0], tile[1])
            hitbox = pygame.key.get_pressed()
            if hitbox[pygame.K_LEFTBRACKET]:
                pygame.draw.rect(screen, (0, 240, 120), tile[1], 1)


level_look = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,2,2,2,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,2,2,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,8,0,0,0,2,2,2,0,0,0,0,0,0,0,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,3,3,3,3,3,2,2,1,1,1,3,3,3,3,3,3,3,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,2,2,2,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,1,1,1,1,1,1],
[1,0,0,0,0,0,0,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

spikes_group = pygame.sprite.Group()

over = 1

class Player():
    def __init__(self, x, y):
        player_image = pygame.image.load('images/nuts.png')

        self.img = pygame.transform.scale(player_image, (25,50))

        self.rect = self.img.get_rect()

        self.width = self.img.get_width()
        self.height = self.img.get_height()

        self.vel = 0
        self.jump = False
        self.rect.x = x
        self.rect.y = y

    def move(self):
        moveX = 0
        moveY = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            moveX -= 4
        if keys[pygame.K_d]:
            moveX += 4

        if keys[pygame.K_w] and self.jump == False:
            self.vel = -13
            self.jump = True
        if keys[pygame.K_w] == False:
            self.jump = False

        self.vel += 1
        if self.vel > 10:
            self.vel = 10       
        moveY += self.vel

        for tile in level.tileL:
            if tile[1].colliderect(self.rect.x + moveX, self.rect.y, self.width, self.height):
                moveX = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + moveY, self.width, self.height):
                if self.vel < 0:
                    moveY = tile[1].bottom - self.rect.top
                    self.vel = 0
                elif self.vel >= 0:
                    moveY = tile[1].top - self.rect.bottom
                    self.vel = 0
                    

        over = 1
        if pygame.sprite.spritecollide(self, spikes_group, False):
            over = 0
            if over == 0:
                screen.fill((0, 0, 0))
                font = pygame.font.SysFont('arial', 40)
                title = font.render('Game Over', True, (255, 255, 255))
                restart_button = font.render('R - Restart', True, (255, 255, 255))
                quit_button = font.render('Q - Quit', True, (255, 255, 255))
                screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
                screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
                screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
                moveX = 1000
                moveY = 1000
            None

        self.rect.y += moveY
        self.rect.x += moveX
                
        screen.blit(self.img, self.rect)
        hitbox = pygame.key.get_pressed()
        if hitbox[pygame.K_RIGHTBRACKET]:
            pygame.draw.rect(screen, (255,255,0), self.rect, 1)

class Spikes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        spikes = pygame.image.load('images/spikes.png')
        self.image = pygame.transform.scale(spikes, (tile_sz, tile_sz // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
player = Player(130,200)
level = Level(level_look)

run = True
while run:

    screen.fill((0,255,255))
    level.draw()
    spikes_group.draw(screen)
    player.move()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    clock.tick(fps)
    pygame.display.update()
pygame.quit()
