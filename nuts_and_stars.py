from pathlib import Path
from random import randint
from typing import Tuple
import pygame

WIDTH = 800
HEIGHT = 600

stars_countdown = 2500
stars_interval = 100

STARS_COUNT = 3

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        player_image = str(
            Path.cwd() /"images/nuts.png"
        )
        self.surf = pygame.image.load(player_image).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (80, 80))
        self.rect = self.surf.get_rect()

    def update(self, pos: Tuple):
        self.rect.center = pos


class Stars(pygame.sprite.Sprite):
    def __init__(self):
        super(Stars, self).__init__()

        stars_image = str(Path.cwd() /"images/stars.png")

        self.surf = pygame.image.load(stars_image).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (80, 80))
        self.rect = self.surf.get_rect(
            center=(
                randint(10, WIDTH - 10),
                randint(10, HEIGHT - 10),
            )
        )

pygame.init()

screen = pygame.display.set_mode(size=[WIDTH, HEIGHT])

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

ADDSTARS = pygame.USEREVENT + 1
pygame.time.set_timer(ADDSTARS, stars_countdown)

stars_list = pygame.sprite.Group()

score = 0


player = Player()
player.update(pygame.mouse.get_pos())

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == ADDSTARS:
            new_stars = Stars()
            stars_list.add(new_stars)

            if len(stars_list) < 3:
                stars_countdown -= stars_interval
            if stars_countdown < 100:
                stars_countdown = 100

            pygame.time.set_timer(ADDSTARS, 0)

            pygame.time.set_timer(ADDSTARS, stars_countdown)

    player.update(pygame.mouse.get_pos())

    stars_collected = pygame.sprite.spritecollide(
        sprite=player, group=stars_list, dokill=True
    )
    for stars in stars_collected:
        score += 10
       

    if len(stars_list) >= STARS_COUNT:
        running = False

    screen.fill((0, 255, 255))

    for stars in stars_list:
        screen.blit(stars.surf, stars.rect)

    screen.blit(player.surf, player.rect)

    score_font = pygame.font.SysFont("any_font", 36)
    score_block = score_font.render(f"Score: {score}", False, (0, 0, 0))
    screen.blit(score_block, (50, HEIGHT - 50))

    pygame.display.flip()

    clock.tick(30)

print(f"Game over! Final score: {score}")

pygame.mouse.set_visible(True)

pygame.quit()
