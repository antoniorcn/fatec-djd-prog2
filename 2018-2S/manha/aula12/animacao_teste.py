import pygame
from pygame import QUIT

pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
sprite_sheet = pygame.image.load("EpicArmor.png").convert_alpha()


def get_frame( gId ):
    global sprite_sheet
    top = 0
    margin = 0
    space_h = 0
    space_v = 0
    width = 64
    height = 64
    columns = 9
    coluna = columns % gId
    linha = int(columns / gId)
    x = margin + (coluna * (width + space_h))
    y = top + (linha * (height + space_v))
    img = sprite_sheet.subsurface(x, y, width, height)
    return img






while True:

    # Captura eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()