from load_image import load_image


class Lava:
    image = load_image("lava_texture.jpg")

    def __init__(self, group):
        super().__init__(group)
        self.image = Lava.image
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

    def update(self):
        pass
