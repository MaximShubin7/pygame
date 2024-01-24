import os
import sys
import pygame as pg
import pymunk.pygame_util
from random import randrange
from loadimage import load_image
from Lava import Lava

pymunk.pygame_util.positive_y_is_up = False
background_colour = (44, 70, 145)
RES = WIDTH, HEIGHT = 1000, 600
FPS = 60

pg.init()


def level_window():
    # Инициализация Pygame
    pg.init()

    # Установка размеров окна
    window_width = 1000
    window_height = 600
    window = pg.display.set_mode((window_width, window_height))

    # Отображение изображения на всем окне
    background = load_image('levelfon.png')
    background = pg.transform.scale(background, (1000, 600))
    window.blit(background, (0, 0))
    pg.display.flip()

    # Определение цветов
    black = (0, 0, 0)
    yellow = (255, 255, 0)

    # Создание объекта шрифта
    font = pg.font.Font(None, 104)

    # Основной цикл программы
    running1 = True
    while running1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running1 = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= 150 and 100 <= y <= 200:
                    # Открытие 1 лвла
                    pass
                elif 175 <= x <= 275 and 100 <= y <= 200:
                    # Открытие 2 лвла
                    pass
                elif 300 <= x <= 400 and 100 <= y <= 200:
                    # Открытие 3 лвла
                    pass

        # Создание кнопок
        text = font.render('Уровни', True, black)
        text_rect = text.get_rect(center=(window_width // 2, 50))
        window.blit(text, text_rect)

        # Создание квадратов с надписями
        level1 = pg.draw.rect(window, yellow, (50, 100, 100, 100))
        text1 = font.render('1', True, black)
        window.blit(text1, (85, 125))

        level2 = pg.draw.rect(window, yellow, (175, 100, 100, 100))
        text2 = font.render('2', True, black)
        window.blit(text2, (210, 125))

        level3 = pg.draw.rect(window, yellow, (300, 100, 100, 100))
        text3 = font.render('3', True, black)
        window.blit(text3, (335, 125))

        # Обновление экрана
        pg.display.flip()


def start_window():
    # Инициализация Pygame
    pg.init()

    # Установка размеров окна
    window_width = 1000
    window_height = 600
    window = pg.display.set_mode((window_width, window_height))

    # Отображение изображения на всем окне
    background = load_image('startfon.png')
    background = pg.transform.scale(background, (1000, 600))
    window.blit(background, (0, 0))
    pg.display.flip()

    # Определение цветов
    green = (0, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)

    # Создание объекта шрифта
    font = pg.font.Font(None, 104)

    # Основной цикл программы
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 300 <= x <= 500 and 175 <= y <= 225:
                    # Логика для кнопки "Играть"
                    # Открытие окна с выбором уровня
                    level_window()
                elif 300 <= x <= 500 and 275 <= y <= 325:
                    # Логика для кнопки "Правила"
                    pass
                elif 300 <= x <= 500 and 375 <= y <= 425:
                    # Логика для кнопки "Выход"
                    running = False
                    pg.quit()
                    sys.exit()

        # Создание кнопок
        play_text = font.render('Играть', True, green)
        play_rect = play_text.get_rect(center=(window_width / 2, window_height / 2 - 100))
        window.blit(play_text, play_rect)

        rules_text = font.render('Правила', True, blue)
        rules_rect = rules_text.get_rect(center=(window_width / 2, window_height / 2))
        window.blit(rules_text, rules_rect)

        exit_text = font.render('Выход', True, red)
        exit_rect = exit_text.get_rect(center=(window_width / 2, window_height / 2 + 100))
        window.blit(exit_text, exit_rect)

        # Обновление экрана
        pg.display.flip()


# Вызов функции для отображения окна
start_window()

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)
# физика предметов
space = pymunk.Space()
space.gravity = 0, 8000
segment_shape = pymunk.Segment(space.static_body, (1, HEIGHT), (WIDTH, HEIGHT), 100)
space.add(segment_shape)
segment_shape.elasticity = 0.4
segment_shape.friction = 1.0

all_sprites = pg.sprite.Group()
for x in range(0, 1001, 40):
    for y in range(500, 601, 40):
        Lava(all_sprites, x, y, True)
for x in range(0, 1001, 40):
    for y in range(500, 601, 40):
        Lava(all_sprites, x, y, False)

while True:
    surface.fill(background_colour)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    space.step(1 / FPS)
    space.debug_draw(draw_options)
    all_sprites.draw(surface)
    all_sprites.update()
    pg.display.flip()
    clock.tick(FPS)
