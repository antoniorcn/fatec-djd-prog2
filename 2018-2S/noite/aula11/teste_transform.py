import pygame
import random
from pygame import QUIT, KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE

pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
imagem = pygame.image.load("images/gato.png").convert_alpha()
angulo = 50
while True:
    #Calcular regras
    gato_rot = pygame.transform.rotate(imagem, angulo)
    angulo += 1
    r1 = gato_rot.get_rect()
    r1.x = 400 - (r1.w / 2) # 400 - r1.centerx
    r1.y = 300 - (r1.h / 2) # 300 - r1.centery

    #Desenhar a tela
    tela.fill((0, 0, 0))

    # Pinta imagem
    tela.blit(gato_rot, [r1.x, r1.y])
    pygame.draw.rect(tela, (255, 255, 0), r1, 3)
    pygame.display.update()

    #Captura eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()