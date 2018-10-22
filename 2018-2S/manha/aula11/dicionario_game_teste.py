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
imagem1 = pygame.image.load("./images/gato.png").convert_alpha()
imagem2 = pygame.image.load("./images/enemy.png").convert_alpha()
imagem3 = pygame.image.load("./images/explosion.png").convert_alpha()

rinimigo = imagem2.get_rect()
img_explod = pygame.transform.scale(imagem3, rinimigo.size)
x = 100
y = 100
velX = 0
velY = 0
explode = False
while True:
    # Calcular Regras
    x = x + velX
    y = y + velY
    r1 = imagem1.get_rect()
    r1.x = x
    r1.y = y
    r2 = imagem2.get_rect()
    r2.x = 400
    r2.y = 300

    if rect_colide(r1, r2):
        explode = True
    else:
        explode = False

    # Desenhar na tela
    tela.fill((0, 0, 0))
    tela.blit(imagem1, (x, y))
    tela.blit(imagem2, (400, 300))
    if explode == True:
        tela.blit(img_explod, (400, 300))
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