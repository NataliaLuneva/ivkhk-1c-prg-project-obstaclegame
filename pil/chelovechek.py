import pygame
pygame.init()

win = pygame.display.set_mode((618,600))
walkRight = [
    pygame.image.load('2.png'),
    pygame.image.load('3.png'),
    pygame.image.load('2.png')
]

walkLeft = [
    pygame.image.load('5.png'),
    pygame.image.load('4.png')
]

playerStand = pygame.image.load('1.png')
bg = pygame.image.load('picture3.png')
clock = pygame.time.Clock()


x = 50
y = 425
width = 46
height = 56
speed = 4

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

def draw_window():
    global animCount
    win.blit(bg,(0, 0))
    
    if animCount + 1 >= 15:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 4],(x,y))
    elif right :
        win.blit(walkRight[animCount // 4],(x,y))
    else:
        win.blit(playerStand,(x,y))

    pygame.display.update()


run = True

while run:
    win.fill((0,0,0))
    clock.tick (15)
    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 618 - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:  
            if jumpCount < 0:
                y += (jumpCount**2)/2
            else:
                y -= (jumpCount**2)/2
                jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    draw_window()
    
