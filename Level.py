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


def equal(a, b):
    return abs(a - b) <= 20


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
        self.all_sprites.draw(self.window)

        im = load_image('grass.png')
        im = pg.transform.scale(im, (60, 60))
        self.window.blit(im, (550, 200))
        pg.display.flip()

        line = []
        start_time = 0
        r = False
        while running1:
            if r:
                continue
            if flag and pg.time.get_ticks() - start_time >= 5000:
                background = load_image('resultfon.jpg')
                background = pg.transform.scale(background, (1000, 600))
                self.window.blit(background, (0, 0))

                font = pg.font.SysFont('Comic Sans MS', 100)
                text = font.render(f'Победа!!!', False, (255, 255, 255))
                self.window.blit(text, (300, 100))

                font1 = pg.font.Font(None, 72)
                exit_text = font1.render('К выбору уровня', True, (0, 255, 0))
                exit_rect = exit_text.get_rect(center=(self.window_width / 2 - 150, self.window_height / 2 + 50))
                self.window.blit(exit_text, exit_rect)

                font1 = pg.font.Font(None, 72)
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
                    if j.__class__.__name__ == 'Water':
                        x = (j.rect.x + 20) - pos[0]
                        y = j.rect.y - pos[1]
                        if x >= -40 and y >= -40 and x <= 40 and y <= 40:
                            pg.quit()
                            sys.exit()
                    if j.__class__.__name__ == 'Thorn':
                        x = (j.rect.x + 20) - pos[0]
                        y = j.rect.y - pos[1]
                        if x >= -40 and y >= -10 and x <= 40 and y <= 10:
                            pg.quit()
                            sys.exit()
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
            pass
        if self.type == 3:
            pass
        if self.type == 4:
            pass

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
