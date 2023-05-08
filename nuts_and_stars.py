#код персонажа
import pygame
from random import randint
from pathlib import Path
from typing import Tuple
from pygame.locals import *

width = 800
height = 600

stars_countdown = 2500
stars_interval = 100

stars_count = 3

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        player_img = str(
            Path.cwd() / "pygame" / "images" / "nuts.png"
        )
class Stars(pygame.sprite.Sprite):
    def __init__(self):
        super(Stars, self).__init__()
        stars_img = str(Path.cwd() / "pygame" / "images" / "stars.png")
        self.surf = pygame.image.load(stars_img).convert_alpha()
        self.rect = self.surf.get_rect(
            center = (
            randint(10, width - 10),
            randint(10, height - 10),
            )
        )

pygame.init()

screen = pygame.display.set_mode(size = [width, height])
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
addstars = pygame.USEREVENT + 1
pygame.time.set_timer(addstars, stars_countdown)
stars_list = pygame.sprite.Group()
score = 0

player = Player()
player.update(pygame.mouse.get_pos())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == addstars:
            new_stars = Stars()
            stars_list.add(new_stars)
            if len(stars_list) < 1:
                stars_countdown -= stars_interval
            if stars_countdown < 100:
                stars_countdown = 100
            pygame.time.set_timer(addstars, 0)
            pygame.time.set_timer(addstars, stars_countdown)
    player.update(pygame.mouse.get_pos())
    stars_collected = pygame.sprite.spritecollide(
        sprite = player, group = stars_list, dokill = True
    )
    for stars in stars_collected:
        score += 1
    if len(stars_list) >= stars_count:
        running = False
        screen.fill(179, 208, 255)
    for stars in stars_list:
        screen.blit(stars.surf, stars.rect)
    
    screen.blit(player.surf, player.rect)

    score_font = pygame.font.SysFont('any_font', 36)
    score_block = score_font.render(f'Score: {score}', False, (0, 0, 0))
    screen.blit(score_block, (50, height - 50))

    pygame.display.flip()
    clock.tick(30)

print(f'Game Over! Final score: {score}')
pygame.mouse.set_visible(True)

pygame.quit()
