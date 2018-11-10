import pygame
from pygame.locals import Rect, QUIT

pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
img_fundo = pygame.image.load("space.jpg").convert()
img_ground = pygame.image.load("lunar_ground.png").convert_alpha()


def parallax(surf, initial_pos, img, pos_x):
    pos_x %= img.get_width()
    retangulo1 = Rect((0, 0), (pos_x, img.get_height()))
    temp_img1 = img.subsurface(retangulo1)
    retangulo2 = Rect((pos_x, 0), (img.get_width() - pos_x, img.get_height()))
    temp_img2 = img.subsurface(retangulo2)
    surf.blit(temp_img1, (img.get_width() - pos_x, initial_pos[1]))
    surf.blit(temp_img2, initial_pos)


clk = pygame.time.Clock()
x_fundo = 0
x_ground = 0
while True:
    #Calcular Regras
    x_fundo += 0.1
    x_ground += 1

    # Pintar
    tela.fill((0, 0, 0))
    parallax(tela, (0, 0), img_fundo, int(x_fundo))
    parallax(tela, (0, 300), img_ground, int(x_ground))

    pygame.display.update()
    clk.tick(200)

    # Captura eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()