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


class Level:
    def __init__(self, type):
        self.all_sprites = pg.sprite.Group()
        self.type = type

    def run_level(self):
        # Инициализация Pygame
        pg.init()
        # Установка размеров окна
        self.window_width = 1000
        self.window_height = 600
        self.FPS = 60
        window = pg.display.set_mode((self.window_width, self.window_height))
        window.fill((245, 234, 233))
        # Отображение изображения на всем окне
        background = load_image('bricks.png')
        background = pg.transform.scale(background, (1000, 600))
        background.set_alpha(100)
        window.blit(background, (0, 0))
        pg.display.flip()
        # физика

        clock = pg.time.Clock()
        draw_options = pymunk.pygame_util.DrawOptions(window)

        # настройки Pymunk
        self.space = pymunk.Space()
        self.space.gravity = 0, 8000

        # Основной цикл программы
        running1 = True
        self.generate_blocks()
        while running1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running1 = False
                    pg.quit()
                    sys.exit()
            self.space.step(1 / self.FPS)
            self.space.debug_draw(draw_options)
            # Обновление экрана
            self.all_sprites.draw(window)
            self.all_sprites.update()
            pg.display.flip()
            clock.tick(self.FPS)

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
