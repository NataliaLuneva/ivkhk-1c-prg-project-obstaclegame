#Импорт и инициализация
from pathlib import Path
# Для случайного размещения монет
from random import randint
# Для поиска ресурсов
from typing import Tuple
# Для аннотации типов
import pygame

# Устанавливает размеры окна
WIDTH = 800
HEIGHT = 600

# Как часто должны генерироваться звёздочки (мс)
stars_countdown = 2500
stars_interval = 100

# Сколько звёзд должно быть на экране, чтобы игра закончилась
STARS_COUNT = 3

# Определяет спрайт для игрока
class Player(pygame.sprite.Sprite):
    """_Класс персонажа_

    Args:
        pygame (_sprite_): _Это элемент компьютерной графики, который показывает, что персонаж игры подвижный_
    """
    def __init__(self):
        """Инициализирует спрайт игрока"""
        super(Player, self).__init__()

        '''Получает изображение игрока'''
        player_image = str(
            Path.cwd() /"images/nuts.png"
        )
        '''Загружает изображение, настраивает альфа канал для прозрачности'''
        self.surf = pygame.image.load(player_image).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (80, 80))
        '''Сохраняет в прямоугольнике, чтобы перемещать объект'''
        self.rect = self.surf.get_rect()

    def update(self, pos: Tuple):
        """Обновляет позицию персонажа

        Аргументы:
            pos {Tuple} -- (X,Y) позиция для движения персонажа
        """
        self.rect.center = pos

# Определяет спрайт для звёзд
class Stars(pygame.sprite.Sprite):
    """_Класс звёздочек_

    Args:
        pygame (_sptite_): _Это элемент компьютерной графики, который показывает, что звёзды подвижны__
    """
    def __init__(self):
        """Инициализирует спрайт звезды"""
        super(Stars, self).__init__()
        '''Получает изображение звезды'''
        stars_image = str(Path.cwd() /"images/stars .png")
        '''Загружает изображение, настраивает альфа канал для прозрачности'''
        self.surf = pygame.image.load(stars_image).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (80, 80))
        '''Задает стартовую позицию, сгенерированную случайным образом'''
        self.rect = self.surf.get_rect(
            center=(
                randint(10, WIDTH - 10),
                randint(10, HEIGHT - 10),
            )
        )

# Инициализирует движок
pygame.init()

# Инициализирует движок
screen = pygame.display.set_mode(size=[WIDTH, HEIGHT])

# Настраивает окно
pygame.mouse.set_visible(False)

# Скрывает курсор мыши
clock = pygame.time.Clock()

# Запускает часы для фиксации времени фрейма
ADDSTARS = pygame.USEREVENT + 1
pygame.time.set_timer(ADDSTARS, stars_countdown)

# Настраивает список звёзд
stars_list = pygame.sprite.Group()

# Инициализирует счет
score = 0

# Создает спрайт героя и устанавливаем на заданную позицию
player = Player()
player.update(pygame.mouse.get_pos())

# Цикл событий
running = True
while running:
    '''Проверяет, нажал ли пользователь кнопку закрытия окна'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            '''Определяет, нужно ли добавлять новую звезду'''
        elif event.type == ADDSTARS:
            '''Добавляет новую звезду'''
            new_stars = Stars()
            stars_list.add(new_stars)
            '''Ускоряет игру, если на экранее менее 3 звезд'''
            if len(stars_list) < 3:
                stars_countdown -= stars_interval
            '''Ограничивает скорость'''
            if stars_countdown < 100:
                stars_countdown = 100
            '''Останавливает предыдущий таймер'''
            pygame.time.set_timer(ADDSTARS, 0)
            '''Запускает новый таймер'''
            pygame.time.set_timer(ADDSTARS, stars_countdown)
    '''Обновляетпозицию персонажа'''
    player.update(pygame.mouse.get_pos())
    '''Проверяет, столкнулся ли игрок со звездой и удаляет, если это так'''
    stars_collected = pygame.sprite.spritecollide(
        sprite=player, group=stars_list, dokill=True
    )
    for stars in stars_collected:
        '''Каждая каждая звезда стоит 10 очков'''
        score += 10
    # Проверяет, не слишком ли много звёзд
    if len(stars_list) >= STARS_COUNT:
        '''Если монет много, останавливает игру'''
        running = False

    '''Указывает цвет фона'''
    screen.fill((0, 255, 255))

    '''Рисует следующие звёзды'''
    for stars in stars_list:
        screen.blit(stars.surf, stars.rect)

    '''Отрисовывает персонажа'''
    screen.blit(player.surf, player.rect)

    '''Выводит текущий счет'''
    score_font = pygame.font.SysFont("any_font", 36)
    score_block = score_font.render(f"Score: {score}", False, (0, 0, 0))
    screen.blit(score_block, (50, HEIGHT - 50))

    '''Отображает всё на экране'''
    pygame.display.flip()

    '''Скорость обновления - 30 кадров в секунду'''
    clock.tick(30)

# Печатает итоговый результат
print(f"Game over! Final score: {score}")

# Делает курсор мыши вновь видимым
pygame.mouse.set_visible(True)

# Выходит из игры
pygame.quit()
