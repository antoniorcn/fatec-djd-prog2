import pygame
from pygame.locals import Rect, QUIT


def parallax(surf, initial_pos, img, pos_x):
    pos_x %= img.get_width()
    rect1 = Rect((0, 0), (pos_x, img.get_height()))
    temp_img1 = img.subsurface(rect1)
    rect2 = Rect((pos_x, 0), (img.get_width() - pos_x, img.get_height()))
    temp_img2 = img.subsurface(rect2)
    surf.blit(temp_img1, (img.get_width() - pos_x, initial_pos[1]))
    surf.blit(temp_img2, initial_pos)

screen = pygame.display.set_mode((800, 600), 0, 32)
img_fundo = pygame.image.load("space.jpg").convert()
img_ground = pygame.image.load("lunar_ground.png").convert_alpha()

x_fundo = 0
x_ground = 0
while True:
    # Calcular Regras
    x_fundo += -0.1
    x_ground += -1

    # Desenha na tela
    parallax(screen, (0, 0), img_fundo, x_fundo)
    parallax(screen, (0, 300), img_ground, x_ground)
    pygame.display.update()

    # Captura Eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()