from load_image import load_image
import pygame as pg


class Lava(pg.sprite.Sprite):
    image = load_image("lava_texture.jpg")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Lava.image
        self.image = pg.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
