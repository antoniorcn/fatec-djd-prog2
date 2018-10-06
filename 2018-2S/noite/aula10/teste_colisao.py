import pygame
from pygame import QUIT, KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT, MOUSEMOTION


# def overlapping(minA, maxA, minB, maxB):
#     return minB <= maxA and minA <= maxB


# def rect_colide(rectA, rectB):
#     aLeft = rectA['x']
#     aRight = rectA['x'] + rectA['w']
#     aTop = rectA['y']
#     aBottom = rectA['y'] + rectA['h']
#     bLeft = rectB['x']
#     bRight = rectB['x'] + rectB['w']
#     bTop = rectB['y']
#     bBottom = rectB['y'] + rectB['h']
#     collideX = overlapping(aLeft, aRight, bLeft, bRight)
#     collideY = overlapping(aBottom, aTop, bBottom, bTop)
#     return collideX and collideY

pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
x = 100
y = 100
velY = 0
velX = 0
cor = (0, 0, 255)
while True:
    #Desenhar a tela
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 0, 0), ((x, y), (200, 50)), 0)
    pygame.draw.rect(tela, cor, ((400, 400), (100, 50)), 0)
    pygame.display.update()
    #Calcular regras
    y = y + velY
    x = x + velX
    # r1 = {'x':x, 'y':y, 'w':200, 'h':50}
    # r2 = {'x':400, 'y':400, 'w':100, 'h': 50}
    r1 = pygame.Rect((x, y), (200, 50))
    r2 = pygame.Rect((400, 400), (100, 50))
    if r1.colliderect(r2):
        print ("Colidiu")
        cor = (255, 255, 0)
    else:
        cor = (0, 0, 255)

    #if rect_colide(r1, r2):
    #    print("Colidiu")



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
