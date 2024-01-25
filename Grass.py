import random

from loadimage import load_image
import pygame as pg


class Grass(pg.sprite.Sprite):
    image = load_image("grass.png")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Grass.image
        self.image = pg.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alpha = 255

    def update(self):
        pass
