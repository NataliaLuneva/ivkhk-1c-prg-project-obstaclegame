import pygame
from pygame.locals import *

pygame.init()

screen_width = 1560
screen_height = 780

# выставляется размер и ширина экрана от [screen_width] и [screen_height]
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Nut platformer game')

# частота обновления, которая зависит от переменной [fps]
clock = pygame.time.Clock()
fps = 90

# размер хитбокса блока
tile_sz = 78

transition = 4
score = 0
pause = False
appear = False

class Level():
    '''
    data - получение данных от [level_look]
    '''
    def __init__(self, data):  
        # переменная в которую передаются блоки уровня     
        self.tileL = []
        
        # загрузка картинок уровня
        dirt = pygame.image.load('images/dirt.png')
        grass = pygame.image.load('images/grass.png')
        half_grass = pygame.image.load('images/halfGrass2.png')
        
        # cчет по вертикали
        countRow = 0
        for row in data:

            # счет по горизонтали
            countCol = 0
            for tile in row:

                # проверка если в [level_look] есть данная цифра, тогда в [self.tileL] добавляется хитбокс и картинка
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
                    half_grass_img = pygame.transform.scale(half_grass, (tile_sz, tile_sz // 2))
                    img_rect_half = half_grass_img.get_rect()
                    img_rect_half.x = countCol * tile_sz
                    img_rect_half.y = countRow * tile_sz
                    tile = (half_grass_img, img_rect_half)
                    self.tileL.append(tile)

                if tile == 3:
                    spikes = Spikes(countCol * tile_sz, countRow * tile_sz + (tile_sz // 2))
                    spikes_group.add(spikes)
                if tile == 4:
                    end = End(countCol * tile_sz, countRow * tile_sz)
                    end_group.add(end)
                if tile == 5:
                    stars = Stars(countCol * tile_sz , countRow * tile_sz)
                    star_group.add(stars)
                if tile == 6:
                    ladder = Ladder(countCol * tile_sz, countRow * tile_sz)
                    ladder_group.add(ladder)

                # счет переходит на следующую вертикаль, если равна 0
                countCol += 1

            # счет переходит на следующую горизонталь, если равна 0
            countRow += 1

    def draw(self):
        # добавляется хитбокс и картинка, если в переменной [level_look] есть соответсвующая цифра
        for tile in self.tileL:
            screen.blit(tile[0], tile[1])

            # по нажатию на "[" показываются хитбоксы уровня
            hitbox = pygame.key.get_pressed()
            if hitbox[pygame.K_LEFTBRACKET]:
                pygame.draw.rect(screen, (255,255,255), tile[1], 1)

# уровень
# easy
level_look = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 6, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 6, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 5, 0, 0, 2, 2, 0, 0, 0, 0, 6, 2, 1, 1],
[1, 0, 0, 4, 0, 0, 2, 2, 2, 2, 1, 1, 2, 8, 8, 0, 6, 1, 1, 1],
[1, 0, 0, 2, 2, 2, 1, 1, 1, 1, 1, 1, 5, 0, 0, 0, 2, 1, 1, 1],
[1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1],
]

# medium
level_look2 = [
[1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 1],
[1, 0, 8, 5, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 1],
[1, 0, 0, 8, 3, 3, 3, 8, 0, 0, 0, 0, 0, 0, 0, 5, 8, 0, 0, 1],
[1, 0, 0, 0, 8, 8, 8, 0, 8, 8, 0, 0, 0, 0, 0, 8, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 2, 2, 0, 5, 0, 1],
[1, 2, 2, 3, 3, 2, 2, 2, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 2, 1]
]

# hard
level_look3 = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 4, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
]

spikes_group = pygame.sprite.Group()
star_group = pygame.sprite.Group()
end_group = pygame.sprite.Group()
ladder_group = pygame.sprite.Group()

class Player():
    def __init__(self, x, y):
        self.restart(x, y)

    def move(self, transition):
        # переменные, которые отвечают за движение и прыжок
        moveX = 0
        moveY = 0

        # переменная, которая отвечает за скорость смены картинок для анимации
        walk_animation = 7

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
restart = pygame.image.load('images/restart.png')
difficulty_image = pygame.image.load('images/difficulty.jpg')
win_image = pygame.image.load('images/levelCompleted.png')
easy_btn_image = pygame.image.load('images/easy.jpg')
medium_btn_image = pygame.image.load('images/medium.jpg')
hard_btn_image = pygame.image.load('images/hard.jpg')
level_select_image = pygame.image.load('images/select lvl.png')
resume_button = pygame.image.load('images/resume.png')
game_over_image = pygame.image.load('images/gameOver.png')
go_back_image = pygame.image.load('images/back.png')
star_appear = pygame.image.load('images/star.png')

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
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self):
        screen.blit(self.screen_image, self.rect)
    
# классы для объектов, которые не имеют хитбокса
class Spikes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        spikes = pygame.image.load('images/spikes2.png')
        self.image = pygame.transform.scale(spikes, (tile_sz, tile_sz // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Stars(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        star = pygame.image.load('images/star.png')
        self.image = pygame.transform.scale(star, (tile_sz, tile_sz))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class End(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        end = pygame.image.load('images/end.png')
        self.image = pygame.transform.scale(end, (tile_sz, tile_sz))
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

# появление звезды под кнопкой уровня
class StarAppear():
    def __init__(self, image, pos, width, height):
        self.image = image
        self.image_rect = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image_rect.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        screen.blit(self.image_rect, self.rect)

position = [(screen_width // 2 + 300, screen_height // 2 - 150),
            (screen_width // 2 + 375, screen_height // 2 - 150),
            (screen_width // 2 + 450, screen_height // 2 - 150)]
easy_star_1 = StarAppear(star_appear, position[0], 50, 50)
easy_star_2 = StarAppear(star_appear, position[1], 50, 50)
easy_star_3 = StarAppear(star_appear, position[2], 50, 50)


# передаем аргументы в классы игрока и уровня    
player = Player(130,600)

# передаем аргументы в классы кнопок
play_button = Button(play_image, screen_width // 2 - 160, screen_height // 2 - 75, 300,100)
quit_button = Button(quit_image, screen_width // 2 - 160, screen_height // 2 + 75, 300,100)
restart_button = Button(restart, screen_width // 2 - 160, screen_height // 2 - 62, 300,100)

easy_button = Button(easy_btn_image, screen_width // 2 + 250, screen_height // 2 - 250, 300,100)
medium_button = Button(medium_btn_image, screen_width // 2 + 250, screen_height // 2 - 50, 300,100)
hard_button = Button(hard_btn_image, screen_width // 2 + 250, screen_height // 2 + 150, 300,100)

level_select = Button(level_select_image, screen_width // 3 + 80, screen_height // 2 - 75, 350,100)
resume_button = Button(resume_button, screen_width // 2 - 160, screen_height // 2 - 200, 300,100)
go_back_button = Button(go_back_image, 40, 40, 200,50)

# передаем аргументы в классы меню
difficulty_draw = ScreenImage(difficulty_image, screen_width // 3 + 50, screen_height // 2 - 100, 400,200)
win_draw = ScreenImage(win_image, screen_width // 3 - 25, screen_height // 2 - 350, 550,300)
game_over_draw = ScreenImage(game_over_image, screen_width // 3 - 55, screen_height // 2 - 350, 600,300)

# передаем аргументы в тексты меню
run = True
while run:
    
    keys = pygame.key.get_pressed()
    # при проигрыше появляется кнопка [Restart] для того, чтобы начать игру заного
    if transition == -1:
        screen.fill((0,0,0))
        game_over_draw.draw()
        if restart_button.update():     
            player.restart(130,600)
            transition = 0

    # если переменная [transition] равна 0, то возврашаются все функции, отвечающие за игрока и уровень
    if transition == 0:
        
        screen.fill((90,143,220))
        # ((185,209,225))

        level.draw() # уровень
        spikes_group.draw(screen) # иголки
        ladder_group.draw(screen) # лестница
        star_group.draw(screen) # звезды

        # начисление очков при подборе звезд
        if pygame.sprite.spritecollide(player, star_group, True):
            score += 1
            if score == 3:
               appear = True

        if appear:
            # дверь в конце уровня
            end_group.draw(screen)

        # возвращается [transition] в зависимости от того, проиграл игрок или нет, если да то [transition] равна -1
        transition = player.move(transition)

        # если игрок дошел до конца уровня, то при нахождении у двери и при нажатии на клавишу [E] игрок победит
        if pygame.sprite.spritecollide(player, end_group, False):
            if keys[pygame.K_RSHIFT] or keys[pygame.K_e]:
                transition = 3
                if transition == 3:
                    screen.fill((0,0,0))
                    win_draw.draw()
                    spikes_group.empty()
                    star_group.empty()
                    end_group.empty()
                    ladder_group.empty()
                    
                    appear = False

        if keys[pygame.K_ESCAPE]:
            transition = 1

    if transition == 1:
        screen.fill((0,0,0))
        if resume_button.update():
            transition = 0
        if quit_button.update():
            transition = 2
            spikes_group.empty()
            star_group.empty()
            end_group.empty()
            ladder_group.empty()
            score = 0
            appear = False
        if restart_button.update():     
            player.restart(130,600)
            transition = 0


    # если переменная [transition] равна 2, то игрок находится в меню уровней.
    # при выборе уровня, переменная [transition] равна 0
    if transition == 2:
        screen.fill((0,0,0))

        if score == 1:
            easy_star_1.update()
        if score == 2:
            easy_star_1.update()
            easy_star_2.update()
        if score == 3:
            easy_star_1.update()
            easy_star_2.update()
            easy_star_3.update()

        difficulty_draw.draw()

        # уровень легкой сложности
        if easy_button.update():
            player.restart(130, 600)
            transition = 0
            level = Level(level_look)

        # уровень средней сложности
        if medium_button.update():
            player.restart(130, 600)
            transition = 0
            level = Level(level_look2)

        # уровень сложной сложности
        if hard_button.update():
            player.restart(130, 600)
            transition = 0
            level = Level(level_look3)

        if go_back_button.update():
            transition = 4
        if keys[pygame.K_ESCAPE]:
            transition = 4
        
    # если уровень пройден, то появляется кнопка [Select Level]
    # при нажатии на кнопку [Select Level], осуществляется переход в меню уровней
    # если переменная [transition] равна 3, то игрок находится в меню, пока не нажмет на кнопку 
    if transition == 3:
        if level_select.update():
            transition = 2
     
    if transition == 4:
        screen.fill((0,0,0))
        # если нажата кнопка для игры, то переменная [transition] равна 2
        if play_button.update():
            transition = 2
        if quit_button.update():
            pygame.quit()

    # если игрок нажимает на выход с помощью [X] то окно закрывается
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(fps)
    #обновление экрана
    pygame.display.update()
pygame.quit()
