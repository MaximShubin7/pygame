import pygame

background_colour = (37, 150, 190)
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('gmfdjgfgfdg')
screen.fill(background_colour)
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
