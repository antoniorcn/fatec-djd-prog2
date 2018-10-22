import pygame
import random
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_d, K_a, K_w, K_s, Rect

matriz = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [2, 0, 2, 2, 1, 2, 2, 1],
    [1, 2, 2, 2, 1, 2, 2, 1],
    [1, 1, 2, 1, 1, 2, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2],
    [1, 2, 1, 1, 1, 2, 2, 1],
    [1, 2, 2, 1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

pygame.init()

font = pygame.font.Font("c:/windows/fonts/snap____.ttf", 48)

pontos = 0

tela = pygame.display.set_mode((800, 600), 0, 32)
w = 800 / 8
h = 600 / 8
pac_orig = pygame.image.load("./images/pac.png").convert_alpha()
brick_orig = pygame.image.load("./images/brick.jpg").convert_alpha()
pilula_orig = pygame.image.load("./images/pilula.png").convert_alpha()
pac = pygame.transform.scale(pac_orig, (int(w), int(h)))
brick = pygame.transform.scale(brick_orig, (int(w), int(h)))
pilula = pygame.transform.scale(pilula_orig, (int(w), int(h)))

pacman = {'col': 1, 'lin': 1, 'imagem': pac}


while True:
    # Calcular Regras

    # Pintar Mapa
    tela.fill((0,0,0))
    for linha in range(8):
        for coluna in range(8):
            x = w * coluna
            y = h * linha
            celula = matriz[linha][coluna]
            if celula == 1:
                # pygame.draw.rect(tela, (255, 255, 0), ((x, y), (w, h)), 0)
                tela.blit(brick, (x, y))
            elif celula == 2:
                # pygame.draw.rect(tela, (0, 0, 0), ((x, y), (w, h)), 0)
                tela.blit(pilula, (x, y))


    # Pintar Minimapa
    for linha in range(8):
        for coluna in range(8):
            x = 10 * coluna
            y = 8 * linha
            celula = matriz[linha][coluna]
            if celula == 1:
                pygame.draw.rect(tela, (255, 0, 0), ((x, y), (10, 8)), 0)
            elif celula == 2:
                pygame.draw.rect(tela, (0, 0, 0), ((x, y), (10, 8)), 0)

    pac_x = pacman['col'] * w
    pac_y = pacman['lin'] * h
    tela.blit(pac, (pac_x, pac_y))
    pontos_img = font.render("Pontos : " + str(pontos), True, (255, 255, 0))
    tela.blit(pontos_img, (500, 5))
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN:
            coluna_target = pacman['col']
            if e.key == K_a:
                coluna_target = pacman['col'] - 1
            elif e.key == K_d:
                coluna_target = pacman['col'] + 1
            if matriz[pacman['lin']][coluna_target] == 2:
                pontos += 1
                matriz[pacman['lin']][coluna_target] = 0
            if matriz[pacman['lin']][coluna_target] != 1:
                pacman['col'] = coluna_target
