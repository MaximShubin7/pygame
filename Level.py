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
        # Определение цветов
        black = (0, 0, 0)
        yellow = (255, 255, 0)
        red = (255, 0, 0)
        # Установка размеров окна
        window_width = 1000
        window_height = 600
        window = pg.display.set_mode((window_width, window_height))
        window.fill((245, 234, 233))
        # Отображение изображения на всем окне
        background = load_image('bricks.png')
        background = pg.transform.scale(background, (1000, 600))
        background.set_alpha(100)
        window.blit(background, (0, 0))
        pg.display.flip()
        self.generate_blocks()
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

            # Обновление экрана
            self.all_sprites.draw(window)
            self.all_sprites.update()
            pg.display.flip()

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
        if self.type == 2:
            pass
        if self.type == 3:
            pass
        if self.type == 4:
            pass
