import random

from load_image import load_image
import pygame as pg


class Lava(pg.sprite.Sprite):
    image = load_image("lava_texture.png")
    hot_image = load_image("hot_lava_texture.png")

    def __init__(self, group, x, y, flag):
        super().__init__(group)
        self.flag = flag
        self.image = Lava.image
        self.image = pg.transform.scale(self.image, (40, 40))
        self.hot_image = pg.transform.scale(self.hot_image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alpha = 255

    def update(self):
        if self.flag:
            #апдейт для текстур, которые не нужно перезагружать
            self.image = self.hot_image
            return
        #анимация нагревания / охлаждения
        add = random.randint(-1, 1)
        if self.alpha + add < 0:
            add = 1
        elif self.alpha + add >= 255:
            add = -1
        if add == -1:
            add = -3
        if add == 1:
            add = 3
        self.alpha += add
        self.image.set_alpha(self.alpha)
