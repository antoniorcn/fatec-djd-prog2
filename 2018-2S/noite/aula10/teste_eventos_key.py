import pygame
from pygame import QUIT, KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT, MOUSEMOTION

pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
x = 100
y = 100
velY = 0
velX = 0
while True:

    #Desenhar a tela
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 0, 0), ((x, y), (200, 50)), 0)
    pygame.display.update()

    #Calcular regras
    y = y + velY
    x = x + velX

    #Capturar eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_RIGHT:
                velX = 1
            elif e.key == K_DOWN:
                velY = 1
        elif e.type == KEYUP:
            if e.key == K_RIGHT:
                velX = 0
            elif e.key == K_DOWN:
                velY = 0
