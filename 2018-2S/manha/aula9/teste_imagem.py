import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_d, K_a, K_w, K_s, K_q, K_e, Rect
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pinguim = pygame.image.load("images/avatar.png").convert_alpha()
pinguim_flip_h = pygame.transform.flip(pinguim, True, False)
pinguim_flip_v = pygame.transform.flip(pinguim, False, True)
scala_x = 95
scala_y = 100
angulo = 0
while True:
    pinguim_reduzido = pygame.transform.scale(pinguim, (scala_x, scala_y))
    pinguim_rotacionado = pygame.transform.rotate(pinguim, angulo)
    tela.fill((255, 255, 0))
    tela.blit(pinguim, (100, 0))
    tela.blit(pinguim_flip_h, (100, 200))
    tela.blit(pinguim_flip_v, (100, 400))
    tela.blit(pinguim_reduzido, (500, 100))
    tela.blit(pinguim_rotacionado, (500, 300))
    w = pinguim_rotacionado.get_width()
    h = pinguim_rotacionado.get_height()
    pygame.draw.rect(tela, (0, 0, 0), ((500, 300), (w, h)), 3)
    pygame.display.update()

    # Capturar eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_w:
                scala_y += 10
            elif e.key == K_s:
                scala_y -= 10
            elif e.key == K_a:
                scala_x -= 10
            elif e.key == K_d:
                scala_x += 10
            elif e.key == K_q:
                angulo -= 10
            elif e.key == K_e:
                angulo += 10