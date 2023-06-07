import pygame
from pygame.locals import *

pygame.init()

screen_width = 1920
screen_height = 1080

# выставляется размер и ширина экрана от [screen_width] и [screen_height]
screen = pygame.display.set_mode((screen_width, screen_height))

# частота обновления, которая зависит от переменной [fps]
clock = pygame.time.Clock()
fps = 90

# размер хитбокса блока
tile_sz = 60

transition = 4
score = 0
pause = False
appear = False

class Level():
    countCol = 0
    countRow = 0

    def __init__(self, data):  
        # переменная в которую передаются блоки уровня    
        self.tileL = []
       
        # загрузка картинок уровня
        dirt = pygame.image.load('images/dirt.png').convert()
        grass = pygame.image.load('images/grass.png').convert()
        half_grass = pygame.image.load('images/halfGrass2.png')
        half_dirt = pygame.image.load('images/halfDirt.png')
       
        # cчет по вертикали
        Level.countRow = 0
        for row in data:

            # счет по горизонтали
            Level.countCol = 0
            for tile in row:

                # проверка если в [level_look] есть данная цифра, тогда в [self.tileL] добавляется хитбокс и картинка
                if tile == 1:
                    dirt_img = pygame.transform.scale(dirt, (tile_sz, tile_sz))
                    img_rect = dirt_img.get_rect()
                    img_rect.x = Level.countCol * tile_sz
                    img_rect.y = Level.countRow * tile_sz
                    tile = (dirt_img, img_rect)
                    self.tileL.append(tile)
                if tile == 2:
                    grass_img = pygame.transform.scale(grass, (tile_sz, tile_sz))
                    img_rect_grass = grass_img.get_rect()
                    img_rect_grass.x = Level.countCol * tile_sz
                    img_rect_grass.y = Level.countRow * tile_sz
                    tile = (grass_img, img_rect_grass)
                    self.tileL.append(tile)
                if tile == 3:
                    spikes = Spikes(Level.countCol * tile_sz, Level.countRow * tile_sz + (tile_sz // 2))
                    spikes_group.add(spikes)
                if tile == 4:
                    end = End(Level.countCol * tile_sz, Level.countRow * tile_sz)
                    end_group.add(end)
                if tile == 5:
                    stars = Stars(Level.countCol * tile_sz , Level.countRow * tile_sz)
                    star_group.add(stars)
                if tile == 6:
                    ladder = Ladder(Level.countCol * tile_sz, Level.countRow * tile_sz)
                    ladder_group.add(ladder)
                if tile == 7:
                    half_dirt_img = pygame.transform.scale(half_dirt, (tile_sz, tile_sz // 2))
                    img_rect_half_dirt = half_dirt_img.get_rect()
                    img_rect_half_dirt.x = Level.countCol * tile_sz
                    img_rect_half_dirt.y = Level.countRow * tile_sz
                    tile = (half_dirt_img, img_rect_half_dirt)
                    self.tileL.append(tile)
                if tile == 8:
                    half_grass_img = pygame.transform.scale(half_grass, (tile_sz, tile_sz // 2))
                    img_rect_half_grass = half_grass_img.get_rect()
                    img_rect_half_grass.x = Level.countCol * tile_sz
                    img_rect_half_grass.y = Level.countRow * tile_sz
                    tile = (half_grass_img, img_rect_half_grass)
                    self.tileL.append(tile)
                if tile == 9:
                    flip_spikes = FlippedSpikes(Level.countCol * tile_sz, Level.countRow * tile_sz)
                    flip_spikes_group.add(flip_spikes)
               
                # счет переходит на следующую вертикаль, если равна 0
                Level.countCol += 1

            # счет переходит на следующую горизонталь, если равна 0
            Level.countRow += 1

    def draw(self):
        # добавляется хитбокс и картинка, если в переменной [level_look] есть соответсвующая цифра
        for tile in self.tileL:
            screen.blit(tile[0], tile[1])

            # по нажатию на "[" показываются хитбоксы уровня
            hitbox = pygame.key.get_pressed()
            if hitbox[pygame.K_LEFTBRACKET]:
                pygame.draw.rect(screen, (255,255,255), tile[1], 1)
    
    
    def update_end_image(self, activity=False):
        for end in end_group:
            if activity:
                end.image = pygame.transform.scale(end.active_end_image, (tile_sz, tile_sz))
            else:
                end.image = pygame.transform.scale(end.end_image, (tile_sz, tile_sz))


# уровень
# easy
level_look = [
[1, 1, 1, 1, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 7, 1, 1, 1, 1, 1],
[1, 1, 7, 0, 0, 0, 0, 7, 1, 1, 1, 1, 1, 1, 7, 0, 0, 7, 1, 1, 1, 1, 7, 7, 0, 0, 0, 9, 7, 1, 1, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 7, 9, 0, 0, 0, 0, 9, 1, 1, 7, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
[1, 0, 0, 0, 5, 2, 2, 0, 0, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1, 1],
[1, 0, 6, 2, 2, 1, 7, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[1, 0, 6, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1],
[1, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 2, 2, 0, 0, 5, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 2, 2, 2, 3, 0, 0, 2, 1, 1, 7, 0, 9, 7, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 6, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 7, 0, 0, 0, 0, 0, 0, 7, 1, 1, 1, 1, 7, 0, 0, 1, 7, 6, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 3, 1],
[1, 1, 1, 7, 7, 7, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 2, 2, 1],
[1, 1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 2, 6, 0, 0, 1, 1, 7, 0, 0, 7, 1, 1],
[1, 0, 0, 0, 0, 0, 2, 1, 1, 1, 2, 0, 0, 0, 3, 1, 7, 0, 0, 7, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 3, 3, 3, 2, 1, 0, 5, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1],
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
]

# medium
level_look2 = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 7, 7, 0, 0, 0, 7, 1, 1, 7, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1, 1],
[1, 1, 1, 7, 0, 0, 0, 0, 0, 0, 9, 1, 0, 0, 0, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 2, 2, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 7, 1, 2, 2, 2, 1, 7, 0, 6, 2, 2, 0, 4, 0, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 0, 0, 6, 7, 1, 2, 2, 2, 1, 1],
[1, 0, 5, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 7, 1, 1, 1, 1],
[1, 2, 2, 2, 1, 1, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 9, 7, 1],
[1, 1, 1, 1, 1, 1, 7, 0, 0, 2, 1, 1, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 5, 6, 0, 0, 0, 0, 3, 0, 1],
[1, 1, 1, 1, 7, 7, 0, 0, 0, 7, 1, 7, 0, 0, 7, 1, 0, 0, 1, 7, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 1],
[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 7, 0, 6, 2, 1, 1, 1],
[1, 1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 1, 1, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 6, 3, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 7, 1, 1, 1, 1, 1, 1, 1, 7, 0, 0, 0, 7, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 1, 1, 7, 0, 0, 0, 0, 7, 1, 1, 1, 1, 7, 0, 0, 0, 0, 0, 7, 1, 1, 1],
[1, 0, 0, 2, 2, 1, 1, 1, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 1, 7, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
[1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
]

# hard
level_look3 = [
[1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 0, 8, 8, 8, 0, 8, 8, 8, 8, 0, 8, 8, 8, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 8, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 6, 1],
[1, 0, 0, 3, 8, 3, 3, 3, 0, 3, 5, 0, 0, 3, 0, 0, 4, 0, 3, 2, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 6 ,1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
]

levels = [level_look, level_look2, level_look3]

class Player():
    def __init__(self, x, y):
        self.restart(x, y)

    def move(self, transition):
        # переменные, которые отвечают за движение и прыжок
        moveX = 0
        moveY = 0

        # переменная, которая отвечает за скорость смены картинок для анимации
        walk_animation = 6

        # переменная для определения нажатия кнопки
        keys = pygame.key.get_pressed()

        # если переменная [transition] равна 0, то игрок может двигатся
        if transition == 0:
            # проверки на нажатие кнопкок
                # если нажата [A] или [<] то игрок двигается влево
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                moveX -= 6
                self.image_direction = -1
                self.image_counter += 1
               
                # если нажата [D] или [>] то игрок двигается вправо
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                moveX += 6
                self.image_direction = 1
                self.image_counter += 1

                # если нажата [SPACE] то игрок поднимается вверх
            if keys[pygame.K_UP] and self.jump == False and self.jump_detect == False or keys[pygame.K_w] and self.jump == False and self.jump_detect == False:
                self.vel = -15
                self.jump = True

                # проверка, чтобы при зажатии клавиши игрок только прыгал, а не поднимался
            if keys[pygame.K_UP] == False or keys[pygame.K_w] == False:
                self.jump = False

            if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False and keys[pygame.K_a] == False and keys[pygame.K_d] == False:
                self.image_index = 0
                self.image_counter = 0
                if self.image_direction == 1:
                    self.image = self.image_right_direction[self.image_index]
                if self.image_direction == -1:
                    self.image = self.image_left_direction[self.image_index]

            # если [self.image_counter] больше [walk_animation] то [self.image_counter] равняется 0
            # к индексу картинки [self.image_index] прибавляется 1, и берется картинка, которая идет по счету
            if self.image_counter > walk_animation:
                self.image_counter = 0
                self.image_index += 1

                # если индекс картинки больше количества картинок, то индекс сбрасывается до 0
                if self.image_index >= len(self.image_right_direction):
                    self.image_index = 0
               
                # если игрок идет вправо, то загружаются картинки, которые направлены в правую сторону
                if self.image_direction == 1:
                    self.image = self.image_right_direction[self.image_index]

                # если игрок идет влево, то загружаются картинки, которые направлены в левую сторону
                if self.image_direction == -1:
                    self.image = self.image_left_direction[self.image_index]

            # если игрок прыгает, то скорость падения увеличивается на 1 пока не достигнет 10
            # если скорость падения больше 10, то скорость падения равна 10
            self.vel += 1
            if self.vel > 10:
                self.vel = 10
            moveY += self.vel

            self.jump_detect = True
            # проверка, если игрок задевает боковые стороны блока то останавливается
            for tile in level.tileL:
                if tile[1].colliderect(self.rect.x + moveX, self.rect.y, self.width, self.height):
                    moveX = 0
                    self.image_counter = 0
                       
                # проверка если игрок задевает верхнюю или нижнюю часть блока
                if tile[1].colliderect(self.rect.x, self.rect.y + moveY, self.width, self.height):

                    # если нижняя часть игрока меньше верхней части блока, то скорость равна 0
                    if self.vel < 0:
                        moveY = tile[1].bottom - self.rect.top
                        self.vel = 0

                    # если верхняя часть игрока больше или равна нижней части блока, то скорость равна 0
                    elif self.vel >= 0:
                        moveY = tile[1].top - self.rect.bottom
                        self.vel = 0
                        self.jump_detect = False

            # присвоение скорости движения и прыжка
            self.rect.y += moveY
            self.rect.x += moveX

            # если переменная [transition] равна -1, то появляется экран проигрыша с кнопкой [Restart]
            if pygame.sprite.spritecollide(self, spikes_group, False):
                transition = -1

            if pygame.sprite.spritecollide(self, flip_spikes_group, False):
                transition = -1

            # если игрок соприкосается с лестницой, то ожидается зажатая [SPACE]
            # если [SPACE] зажата, то игрок поднимается по лестнице
            if pygame.sprite.spritecollide(self, ladder_group, False):
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.vel = -5

        # добавление игрока на экран
        screen.blit(self.image, self.rect)

        # по нажатию на "]" показываются хитбоксы игрока
        hitbox = pygame.key.get_pressed()
        if hitbox[pygame.K_RIGHTBRACKET]:
            pygame.draw.rect(screen, (0,0,250), self.rect, 1)
   
        return transition
   
    def restart(self, x, y):
        self.image_right_direction = []
        self.image_left_direction = []
        self.image_counter = 0
        self.image_index = 0
        for num in range(1, 6):
            player_image_R = pygame.image.load(f'images/nut{num}.png')
            player_image_R = pygame.transform.scale(player_image_R, (50, 75))
            player_image_L = pygame.transform.flip(player_image_R, True, False) # x = True; y = False
            self.image_right_direction.append(player_image_R)
            self.image_left_direction.append(player_image_L)
        self.image = self.image_right_direction[self.image_index]
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel = 0
        self.jump = False
        self.rect.x = x
        self.rect.y = y
        self.add_point = 1
        self.image_direction = 0
        self.jump_detect = True

# картинки для кнопок
play_image = pygame.image.load('images/play.png')
quit_image = pygame.image.load('images/quit.png')
restart_image = pygame.image.load('images/restart.png')
restart_2_image = pygame.image.load('images/restart2.png')
difficulty_image = pygame.image.load('images/select difficulty.png')
win_image = pygame.image.load('images/levelCompleted.png')
easy_btn_image = pygame.image.load('images/easy.png')
medium_btn_image = pygame.image.load('images/medium.png')
hard_btn_image = pygame.image.load('images/hard.png')
level_select_image = pygame.image.load('images/select lvl.png')
resume_button = pygame.image.load('images/resume.png')
game_over_image = pygame.image.load('images/gameOver.png')
go_back_image = pygame.image.load('images/back.png')
settings_image = pygame.image.load('images/settings2.png')

# класс для кнопок
class Button():
    def __init__(self, image, x, y, w, h):
        self.image = image
        self.button_image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.button_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click = False

    def update(self):
        # переменная, которая при нажатии, будет равнятся [True] и будет означать, что кнопка нажата
        # в конце эта переменная возвращается
        action = False

        # переменная для получения позиции курсора
        pos = pygame.mouse.get_pos()
        # проверка если позиция курсора равняется с позицией картинки
        if self.rect.collidepoint(pos):
            # если позиция курсора равняется с позицией картинки, то ожидается нажатие мыши
            # если нажатие мыши происходит, то переменные равняются [True]
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                action = True
                self.click = True
            # проверка для того, чтобы кнопку нельзя было зажать, а только лишь нажать один раз
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False
       
        # появление кнопки и ее хитбокса на экране
        screen.blit(self.button_image, self.rect)

        # возвращаем переменную
        return action
   
# картинки в игре
class ScreenImage():
    def __init__(self, image, x, y, w, h):
        self.image = image
        self.screen_image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.screen_image.get_rect()
        self.rect.x = x
        self.rect.y = y
   
    def draw(self):
        screen.blit(self.screen_image, self.rect)

spikes_group = pygame.sprite.Group()
flip_spikes_group = pygame.sprite.Group()
star_group = pygame.sprite.Group()
end_group = pygame.sprite.Group()
ladder_group = pygame.sprite.Group()
   
# классы для объектов, которые не имеют хитбокса
class Spikes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        spikes = pygame.image.load('images/spikes2.png')
        self.image = pygame.transform.scale(spikes, (tile_sz, tile_sz // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FlippedSpikes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        spikes = pygame.image.load('images/spikes2.png')
        self.flip_image = pygame.transform.flip(spikes, False, True)
        self.image = pygame.transform.scale(self.flip_image, (tile_sz, tile_sz // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Stars(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        star = pygame.image.load('images/stars.png')
        self.image = pygame.transform.scale(star, (tile_sz, tile_sz))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class End(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.end_image = pygame.image.load('images/end.png')
        self.active_end_image = pygame.image.load('images/activeEnd.png')
        self.image = pygame.transform.scale(self.end_image, (tile_sz, tile_sz))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        end = pygame.image.load('images/ladder.png')
        self.image = pygame.transform.scale(end, (tile_sz, tile_sz))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

font = pygame.font.Font(None, 35)

class TextAppear():
    def __init__(self, text, pos, w, h):
        
        self.rect = pygame.Rect(pos, (w, h))
        self.rect_color = ((0,0,0))

        self.text = font.render(text, True, (35, 205, 5))
        self.text_rect = self.text.get_rect(center = self.rect.center)

    def update(self):
        pygame.draw.rect(screen, self.rect_color, self.rect)
        screen.blit(self.text, self.text_rect)

text_position = [(screen_width // 2 + 400, screen_height // 2 - 138),
                 (screen_width // 2 + 400, screen_height // 2 + 62),
                 (screen_width // 2 + 400, screen_height // 2 + 265)]
text_completed = 'COMPLETED'
texts = []

# передаем аргументы в классы игрока и уровня    
player = Player(130,970)

# передаем аргументы в классы кнопок
play_button = Button(play_image, screen_width // 2 - 160, screen_height // 2 - 75, 300,100)
quit_button = Button(quit_image, screen_width // 2 - 160, screen_height // 2 + 75, 300,100)
restart_button = Button(restart_image, screen_width // 2 - 160, screen_height // 2 - 62, 300,100)
restart_2_button = Button(restart_2_image, screen_width // 2 - 160, screen_height // 2 - 62, 300,100)

easy_button = Button(easy_btn_image, screen_width // 2 + 250, screen_height // 2 - 250, 300,100)
medium_button = Button(medium_btn_image, screen_width // 2 + 250, screen_height // 2 - 50, 300,100)
hard_button = Button(hard_btn_image, screen_width // 2 + 250, screen_height // 2 + 150, 300,100)

level_select = Button(level_select_image, screen_width // 2 - 188, screen_height // 2 - 85, 350,120)
resume_button = Button(resume_button, screen_width // 2 - 160, screen_height // 2 - 200, 300,100)
go_back_button = Button(go_back_image, 40, 40, 200,50)
settings_button = Button(settings_image, screen_width // 2 - 45, screen_height // 2 + 225, 75, 75)

# передаем аргументы в классы меню
difficulty_draw = ScreenImage(difficulty_image, screen_width // 3, screen_height // 2 - 100, 500,240)
win_draw = ScreenImage(win_image, screen_width // 3 + 35, screen_height // 2 - 350, 550,300)
game_over_draw = ScreenImage(game_over_image, screen_width // 3 + 20, screen_height // 2 - 350, 600,300)

currrent_level = -1

level_completed = [False, False, False]
game_complete = False

run = True
while run:
   
    keys = pygame.key.get_pressed()
    
    # Экран после проигрыша
    if transition == -1:
        screen.fill((0,0,0))
        game_over_draw.draw()

        levels.clear()
        level = Level(levels)
        spikes_group.empty()
        flip_spikes_group.empty()
        star_group.empty()
        end_group.empty()
        ladder_group.empty()
        score = 0

        if restart_2_button.update():    
            player.restart(130,970)
            transition = 0
            levels = [level_look, level_look2, level_look3]
            level = Level(levels[currrent_level])

    # Активная игра
    if transition == 0:
       
        screen.fill((90,143,220))

        level.draw() # уровень
        spikes_group.draw(screen) # иголки
        flip_spikes_group.draw(screen) # перевернутые иголки
        ladder_group.draw(screen) # лестница
        star_group.draw(screen) # звезды
        end_group.draw(screen) # дверь

        if pygame.sprite.spritecollide(player, star_group, True):
            score += 1


        if score == 3:
            level.update_end_image(activity = True)
            if pygame.sprite.spritecollide(player, end_group, False) and score == 3:
                if keys[pygame.K_e] or keys[pygame.K_RSHIFT]:
                    transition = 3
                    level_completed[currrent_level] = True

        transition = player.move(transition)

        if keys[pygame.K_ESCAPE]:
            transition = 1

    # Пауза
    if transition == 1:
        screen.fill((0,0,0))
        if resume_button.update():
            transition = 0

        if quit_button.update():
            transition = 2
            levels.clear()
            level = Level(levels)
            spikes_group.empty()
            flip_spikes_group.empty()
            star_group.empty()
            end_group.empty()
            ladder_group.empty()
            score = 0
            levels = [level_look, level_look2, level_look3]

        if restart_button.update():    
            player.restart(130,970)
            transition = 0
            level = Level(levels[currrent_level])
            score = 0

    # Выбор уровней
    if transition == 2:
        screen.fill((0,0,0))
        difficulty_draw.draw()
        # Легкий
        if easy_button.update():
            player.restart(130, 970)
            transition = 0
            currrent_level = 0
            level = Level(levels[0])

        # Средний
        if medium_button.update():
            player.restart(130, 970)
            transition = 0
            currrent_level = 1
            level = Level(levels[1])

        # Сложный
        if hard_button.update():
            player.restart(130, 970)
            transition = 0
            currrent_level = 2
            level = Level(levels[2])

        # проверка, какой уровень был пройден
        # если этот  уровень пройден, то под его кнопкой появляется надпись [COMPLETED]
        if level_completed[currrent_level] == True:
                completed = TextAppear(text_completed, text_position[currrent_level], 5, 5)
                texts.append(completed)

        for text in texts:
            text.update()

        # проверка, если все 3 уровня были пройдены
        if level_completed == [True, True, True]:
            game_complete = True

        if go_back_button.update():
            transition = 4
        if keys[pygame.K_ESCAPE]:
            transition = 4

    # Уровень пройден
    if transition == 3:
        screen.fill((0,0,0))
        win_draw.draw()
        if level_select.update():
            transition = 2

            levels.clear()
            level = Level(levels)
            spikes_group.empty()
            flip_spikes_group.empty()
            star_group.empty()
            end_group.empty()
            ladder_group.empty()
            score = 0

            levels = [level_look, level_look2, level_look3]

        if quit_button.update():
            transition = 2

            levels.clear()
            level = Level(levels)
            spikes_group.empty()
            flip_spikes_group.empty()
            star_group.empty()
            end_group.empty()
            ladder_group.empty()
            score = 0

            levels = [level_look, level_look2, level_look3]
    
    # Главное меню
    if transition == 4:
        screen.fill((0,0,0))
        if play_button.update():
            transition = 2
        if quit_button.update():
            pygame.quit()
        if settings_button.update():
            transition = 5

    # Настройки
    if transition == 5:
        screen.fill((0,0,0))
        if go_back_button.update():
            transition = 4

        if keys[pygame.K_ESCAPE]:
            transition = 4
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(fps)
    #обновление экрана
    pygame.display.update()
pygame.quit()
