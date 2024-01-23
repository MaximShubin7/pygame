import os
import sys
import pygame as pg


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f"No file was found")
        sys.exit()
    image = pg.image.load(fullname)
    return image
