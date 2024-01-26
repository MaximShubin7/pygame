import os
import sys
import pygame as pg
import pymunk.pygame_util
from random import randrange
from loadimage import load_image
from Water import Water
from Ground import Ground
from Grass import Grass
from Thorn import Thorn
from Herobrine import Herobrine


def equal(a, b):
    return abs(a - b) <= 20


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


class Level:
    def __init__(self, type):
        self.all_sprites = pg.sprite.Group()
        self.type = type

    def run_level(self):
        pymunk.pygame_util.positive_y_is_up = False
        # Инициализация Pygame
        pg.init()
        # Установка размеров окна
        self.window_width = 1000
        self.window_height = 600
        self.FPS = 60
        self.window = pg.display.set_mode((self.window_width, self.window_height))
        self.window.fill((245, 234, 233))
        # Отображение изображения на всем окне
        background = load_image('bricks.png')
        background = pg.transform.scale(background, (1000, 600))
        background.set_alpha(100)
        self.window.blit(background, (0, 0))
        # физика

        clock = pg.time.Clock()
        draw_options = pymunk.pygame_util.DrawOptions(self.window)

        # настройки Pymunk
        self.space = pymunk.Space()
        self.space.gravity = 0, 8000

        # Основной цикл программы
        running1 = True
        self.create_body((575, 200))
        self.generate_blocks()
        flag = False
        f = False
        dragging = False
        self.window.fill((245, 234, 233))
        self.window.blit(background, (0, 0))
        self.generate_blocks()
        Herobrine(self.all_sprites, 550, 200)
        self.all_sprites.draw(self.window)
        pg.display.flip()

        line = []
        start_time = 0
        r = False
        while running1:
            if r:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                        pg.quit()
                        sys.exit()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if 100 <= x <= 650 and 300 <= y <= 400:
                            level_window()
                        if 700 <= x <= 1000 and 300 <= y <= 400:
                            start_window()

            if flag and pg.time.get_ticks() - start_time >= 10000:
                background = load_image('resultfon.jpg')
                background = pg.transform.scale(background, (1000, 600))
                self.window.blit(background, (0, 0))

                font = pg.font.SysFont('Comic Sans MS', 140)
                text = font.render(f'Победа!!!', False, (0, 255, 0))
                self.window.blit(text, (250, 100))

                font1 = pg.font.SysFont('Comic Sans MS', 72)
                exit_text = font1.render('К выбору уровня', True, (0, 255, 0))
                exit_rect = exit_text.get_rect(center=(self.window_width / 2 - 150, self.window_height / 2 + 50))
                self.window.blit(exit_text, exit_rect)

                font1 = pg.font.SysFont('Comic Sans MS', 72)
                exit_text = font1.render('Назад', True, (255, 0, 0))
                exit_rect = exit_text.get_rect(center=(self.window_width / 2 + 300, self.window_height / 2 + 50))
                self.window.blit(exit_text, exit_rect)
                pg.display.flip()
                r = True
                continue
            if flag:
                font = pg.font.SysFont('Comic Sans MS', 50)
                text = font.render(f'{(pg.time.get_ticks() - start_time) // 1000} сек.', False, (0, 0, 0))
                self.window.blit(text, (430, 10))
                pg.display.flip()

                pos = self.square_body.position
                for j in self.all_sprites:
                    if j.__class__.__name__ == 'Herobrine':
                        j.set_pos(pos)
                    if j.__class__.__name__ == 'Water':
                        x = (j.rect.x + 20) - pos[0]
                        y = j.rect.y - pos[1]
                        if x >= -40 and y >= -40 and x <= 40 and y <= 40:
                            background = load_image('resultfon.jpg')
                            background = pg.transform.scale(background, (1000, 600))
                            self.window.blit(background, (0, 0))

                            font = pg.font.SysFont('Comic Sans MS', 100)
                            text = font.render(f'Ликвидирован', False, (255, 0, 0))
                            self.window.blit(text, (225, 100))

                            font1 = pg.font.SysFont('Comic Sans MS', 72)
                            exit_text = font1.render('К выбору уровня', True, (0, 255, 0))
                            exit_rect = exit_text.get_rect(
                                center=(self.window_width / 2 - 150, self.window_height / 2 + 50))
                            self.window.blit(exit_text, exit_rect)

                            font1 = pg.font.SysFont('Comic Sans MS', 72)
                            exit_text = font1.render('Назад', True, (255, 0, 0))
                            exit_rect = exit_text.get_rect(
                                center=(self.window_width / 2 + 300, self.window_height / 2 + 50))
                            self.window.blit(exit_text, exit_rect)
                            pg.display.flip()
                            r = True
                            break
                    if j.__class__.__name__ == 'Thorn':
                        x = (j.rect.x + 20) - pos[0]
                        y = j.rect.y - pos[1]
                        if x >= -40 and y >= -10 and x <= 40 and y <= 10:
                            background = load_image('resultfon.jpg')
                            background = pg.transform.scale(background, (1000, 600))
                            self.window.blit(background, (0, 0))

                            font = pg.font.SysFont('Comic Sans MS', 100)
                            text = font.render(f'Ликвидирован', False, (255, 0, 0))
                            self.window.blit(text, (225, 100))

                            font1 = pg.font.SysFont('Comic Sans MS', 72)
                            exit_text = font1.render('К выбору уровня', True, (0, 255, 0))
                            exit_rect = exit_text.get_rect(
                                center=(self.window_width / 2 - 150, self.window_height / 2 + 50))
                            self.window.blit(exit_text, exit_rect)

                            font1 = pg.font.SysFont('Comic Sans MS', 72)
                            exit_text = font1.render('Назад', True, (255, 0, 0))
                            exit_rect = exit_text.get_rect(
                                center=(self.window_width / 2 + 300, self.window_height / 2 + 50))
                            self.window.blit(exit_text, exit_rect)
                            pg.display.flip()
                            r = True
                            break
                if r:
                    continue
                self.window.fill((245, 234, 233))
                self.window.blit(background, (0, 0))
                self.generate_blocks()
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running1 = False
                        pg.quit()
                        sys.exit()
                self.space.step(1 / self.FPS)
                self.space.debug_draw(draw_options)
                # Обновление экрана
                self.all_sprites.draw(self.window)
                pg.display.flip()
                clock.tick(self.FPS)
            else:
                for event in pg.event.get():
                    if event.type == pg.MOUSEBUTTONUP:
                        if f:
                            start_time = pg.time.get_ticks()
                            self.draw_line(line)
                            flag = True
                        f = True
                    if event.type == pg.MOUSEBUTTONDOWN:
                        dragging = True
                    if event.type == pg.MOUSEMOTION:
                        if dragging:
                            if len(line) > 0:
                                pg.draw.line(self.window, (0, 0, 0), line[-1], event.pos, 5)
                            else:
                                pg.draw.line(self.window, (0, 0, 0), event.pos, event.pos, 5)
                            line.append(event.pos)
                            pg.display.flip()

    def draw_line(self, array):
        # добавление объекта
        square_mass, square_size = 1, (60, 60)
        body = pymunk.Body(square_mass, 500)
        body.position = (0, 0)
        s = []
        for i in range(1, len(array)):
            s.append(pymunk.Segment(body, array[i - 1], array[i], 5))
            s[-1].density = 1
            s[-1].elasticity = 0.999
        self.space.add(body, *s)

    def generate_blocks(self):
        if self.type == 1:
            for x in range(0, 1001, 40):
                Water(self.all_sprites, x, 560)
                Water(self.all_sprites, x, 520)
                Water(self.all_sprites, x, 480)
            Ground(self.all_sprites, 480, 320)
            Ground(self.all_sprites, 440, 320)
            Ground(self.all_sprites, 520, 320)
            Grass(self.all_sprites, 400, 320)
            Grass(self.all_sprites, 560, 320)
            Thorn(self.all_sprites, 480, 280)
            Thorn(self.all_sprites, 440, 280)
            Thorn(self.all_sprites, 520, 280)
            # платформа
            segment_shape = pymunk.Segment(self.space.static_body, (2, self.window_height),
                                           (self.window_width, self.window_height), 120)
            self.space.add(segment_shape)
            segment_shape.elasticity = 0.8
            segment_shape.friction = 1.0
            platform = pymunk.Segment(self.space.static_body, (420, 340),
                                      (580, 340), 20)
            self.space.add(platform)
            platform.elasticity = 0.8
            platform.friction = 1.0

        if self.type == 2:
            for x in range(0, 1001, 40):
                Water(self.all_sprites, x, 560)
                Water(self.all_sprites, x, 520)
                Water(self.all_sprites, x, 480)
            Ground(self.all_sprites, 380, 320)
            Ground(self.all_sprites, 340, 320)
            Ground(self.all_sprites, 420, 320)
            Grass(self.all_sprites, 300, 320)
            Grass(self.all_sprites, 460, 320)
            Thorn(self.all_sprites, 380, 280)
            Thorn(self.all_sprites, 340, 280)
            Thorn(self.all_sprites, 420, 280)
            # платформа
            segment_shape = pymunk.Segment(self.space.static_body, (2, self.window_height),
                                           (self.window_width, self.window_height), 120)
            self.space.add(segment_shape)
            segment_shape.elasticity = 0.8
            segment_shape.friction = 1.0
            platform = pymunk.Segment(self.space.static_body, (320, 340),
                                      (480, 340), 20)
            self.space.add(platform)
            platform.elasticity = 0.8
            platform.friction = 1.0
        if self.type == 3:
            for x in range(0, 1001, 40):
                Water(self.all_sprites, x, 560)
                Water(self.all_sprites, x, 520)
                Water(self.all_sprites, x, 480)
            Ground(self.all_sprites, 380, 320)
            Ground(self.all_sprites, 640, 320)
            # платформа
            segment_shape = pymunk.Segment(self.space.static_body, (2, self.window_height),
                                           (self.window_width, self.window_height), 120)
            self.space.add(segment_shape)
            segment_shape.elasticity = 0.8
            segment_shape.friction = 1.0
            platform = pymunk.Segment(self.space.static_body, (400, 340),
                                      (400, 340), 20)
            self.space.add(platform)
            platform.elasticity = 0.8
            platform.friction = 1.0
            platform2 = pymunk.Segment(self.space.static_body, (600, 340),
                                       (600, 340), 20)
            self.space.add(platform2)
            platform2.elasticity = 0.8
            platform2.friction = 1.0

    def create_body(self, pos):
        # добавление объекта
        square_mass, square_size = 1, (60, 60)
        self.square_moment = pymunk.moment_for_box(square_mass, square_size)
        self.square_body = pymunk.Body(square_mass, self.square_moment)
        self.square_body.position = pos
        self.square_shape = pymunk.Poly.create_box(self.square_body, square_size)
        self.square_shape.elasticity = 0.4
        self.square_shape.friction = 1.0
        self.space.add(self.square_body, self.square_shape)
