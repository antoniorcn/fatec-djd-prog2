import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_d, K_a, K_w, K_s, Rect


def overlapping(minA, maxA, minB, maxB):
    return minB <= maxA and minA <= maxB


def rect_colide( rectA, rectB ):
    aLeft = rectA.x
    aRight = rectA.x + rectA.w
    aTop = rectA.y
    aBottom = rectA.y + rectA.h
    bLeft = rectB.x
    bRight = rectB.x + rectB.w
    bTop = rectB.y
    bBottom = rectB.y + rectB.h
    collideX = overlapping( aLeft, aRight, bLeft, bRight )
    collideY = overlapping( aTop, aBottom, bTop, bBottom )
    return collideX and collideY


tela = pygame.display.set_mode((800, 600), 0, 32)
x = 100
y = 100
velX = 0
velY = 0
cor = (0, 0, 255)
while True:
    # Calcular Regras
    x = x + velX
    y = y + velY
    r1 = Rect((x, y), (200, 100))
    r2 = Rect((400, 300), (100, 100))

    if rect_colide(r1, r2):
        cor = (255, 255, 0)
    else:
        cor = (0, 0, 255)

    # Desenhar na tela
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 0, 0), ((x, y), (200, 100)), 0)
    pygame.draw.rect(tela, cor, ((400, 300), (100, 100)), 0)
    pygame.draw.circle(tela, (0, 255, 0), (600, 100), 50, 0)
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_d:
                velX = 1
            elif e.key == K_a:
                velX = -1
            elif e.key == K_w:
                velY = -1
            elif e.key == K_s:
                velY = 1
        elif e.type == KEYUP:
            if e.key == K_d:
                velX = 0
            elif e.key == K_a:
                velX = 0
            elif e.key == K_w:
                velY = 0
            elif e.key == K_s:
                velY = 0