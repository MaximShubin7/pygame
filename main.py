import os
import sys
import pygame as pg
import pymunk.pygame_util
from random import randrange
from loadimage import load_image
from Level import Level


def rules_window():
    # Инициализация Pygame
    pg.init()

    # Установка размеров окна
    window_width = 1000
    window_height = 600
    window = pg.display.set_mode((window_width, window_height))

    # Отображение изображения на всем окне
    background = load_image('rulesfon.png')
    background = pg.transform.scale(background, (1000, 600))
    window.blit(background, (0, 0))
    pg.display.flip()

    # Определение цветов
    black = (0, 0, 0)
    yellow = (255, 255, 0)
    red = (255, 0, 0)

    # Создание объекта шрифта
    font = pg.font.SysFont('Comic Sans MS', 104)

    # Основной цикл программы
    running2 = True
    while running2:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running2 = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 420 <= x <= 580 and 480 <= y <= 520:
                    # Вернуться в главное меню
                    running2 = False
                    start_window()

        # Создание кнопок
        text = font.render('Правила', True, yellow)
        text_rect = text.get_rect(center=(window_width // 2, 50))
        window.blit(text, text_rect)

        # текст правил
        font2 = pg.font.SysFont('Comic Sans MS', 35)
        text1 = font2.render('Save the Dog — Игра головоломка, в которой вы', True, black)
        window.blit(text1, (60, 120))
        text2 = font2.render('будете рисовать линии пальцем или мышкой, чтобы', True, black)
        window.blit(text2, (60, 160))
        text3 = font2.render('создать заграждение и спасти собаку от пчел', True, black)
        window.blit(text3, (60, 200))
        text4 = font2.render('и других опасностей. После того как вы нарисуете', True, black)
        window.blit(text4, (60, 240))
        text5 = font2.render('линии вам необходимо продержаться 10 секунд и', True, black)
        window.blit(text5, (60, 280))
        text6 = font2.render('не допустить чтобы собачку укусили пчелы или', True, black)
        window.blit(text6, (60, 320))
        text7 = font2.render('она не попала на шипы. Если вы застряли и не', True, black)
        window.blit(text7, (60, 360))
        text8 = font2.render('знаете как пройти какой-то из уровней, то это', True, black)
        window.blit(text8, (60, 400))
        text9 = font2.render('ваши проблемы. Развивайте мозг и все получится!', True, black)
        window.blit(text9, (60, 440))

        # кнопка назад
        font1 = pg.font.SysFont('Comic Sans MS', 72)
        exit_text = font1.render('Назад', True, red)
        exit_rect = exit_text.get_rect(center=(window_width / 2, window_height / 2 + 200))
        window.blit(exit_text, exit_rect)

        # Обновление экрана
        pg.display.flip()


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
    red = (255, 0, 0)

    # Создание объекта шрифта
    font = pg.font.SysFont('Comic Sans MS', 104)

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
                    level = Level(1)
                    level.run_level()
                elif 175 <= x <= 275 and 100 <= y <= 200:
                    # Открытие 2 лвла
                    level = Level(2)
                    level.run_level()
                elif 300 <= x <= 400 and 100 <= y <= 200:
                    # Открытие 3 лвла
                    level = Level(3)
                    level.run_level()
                elif 420 <= x <= 580 and 480 <= y <= 520:
                    # Вернуться в главное меню
                    running1 = False
                    start_window()

        # Создание кнопок
        text = font.render('Уровни', True, yellow)
        text_rect = text.get_rect(center=(window_width // 2, 50))
        window.blit(text, text_rect)

        # Создание квадратов с надписями
        level1 = pg.draw.rect(window, yellow, (50, 100, 100, 100))
        text1 = font.render('1', True, black)
        window.blit(text1, (80, 80))

        level2 = pg.draw.rect(window, yellow, (175, 100, 100, 100))
        text2 = font.render('2', True, black)
        window.blit(text2, (205, 80))

        level3 = pg.draw.rect(window, yellow, (300, 100, 100, 100))
        text3 = font.render('3', True, black)
        window.blit(text3, (330, 80))

        # кнопка назад
        font1 = pg.font.SysFont('Comic Sans MS', 72)
        exit_text = font1.render('Назад', True, red)
        exit_rect = exit_text.get_rect(center=(window_width / 2, window_height / 2 + 200))
        window.blit(exit_text, exit_rect)

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
    yellow = (255, 255, 0)

    # Создание объекта шрифта
    font = pg.font.SysFont('Comic Sans MS', 104)

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
                if 400 <= x <= 600 and 175 <= y <= 225:
                    # Логика для кнопки "Играть"
                    # Открытие окна с выбором уровня
                    level_window()
                elif 400 <= x <= 600 and 275 <= y <= 325:
                    # Логика для кнопки "Правила"
                    # Открытие окна с правилами
                    rules_window()
                elif 400 <= x <= 600 and 375 <= y <= 425:
                    # Логика для кнопки "Выход"
                    running = False
                    pg.quit()
                    sys.exit()

        # Создание кнопок
        text = font.render('Save the dog', True, yellow)
        text_rect = text.get_rect(center=(window_width // 2, 50))
        window.blit(text, text_rect)

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
