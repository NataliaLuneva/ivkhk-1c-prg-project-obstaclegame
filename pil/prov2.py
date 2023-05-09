import pygame
pygame.init()

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))

        self.dx = 0; self.dy = 0
        self.onGround = False

        self.Go = False
        self.Frame = 0

        self.Left = False
        self.Right = True

        self.Jump = False

    def update(self, *args):
        self.rect.x += self.dx

        if not (self.onGround):
            self.dy += 1

        self.rect.y += self.dy

        self.onGround = False

        if self.rect.y > args[0]:
            self.rect.y = args[0]
            self.dy = 0

            self.onGround = True
            self.Jump = False

        if self.Right:
            file = 'right'
        elif self.Left:
            file = 'left'

        if not (self.Jump):
            if self.Go:
                self.Frame += 0.2
                if self.Frame > 7:
                    self.Frame -= 7

                Personnel = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png']
                self.image = pygame.image.load('image/' + file + '/' + Personnel[int(self.Frame)]).convert_alpha()
            else:
                self.image = pygame.image.load('image/' + file + '/main.png').convert_alpha()
        else:
            self.image = pygame.image.load('image/' + file + '/jump.png').convert_alpha()

        self.dx = 0

width, height = 1000, 500

sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

player = Object(100, 400, 'image/right/main.png')

while True:
    sc.fill(pygame.Color('white'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYUP:
            player.Go = False

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        player.dx = 5

        player.Go = True

        player.Left = False
        player.Right = True
    if key[pygame.K_LEFT]:
        player.dx = -5

        player.Go = True

        player.Left = True
        player.Right = False
    if key[pygame.K_UP]:
        if player.onGround:
            player.dy = -20

            player.onGround = False
            player.Jump = True

    player.update(height - player.rect.height)
    sc.blit(player.image, player.rect)

    pygame.display.update()
    clock.tick(60)