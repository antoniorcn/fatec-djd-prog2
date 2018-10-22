import pygame
import random
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


def calcula_velocidade( obj ):
    chegou = False
    if obj['x'] == obj['destinoX']:
        obj['velX'] = 0
        chegou = True
    elif obj['x'] > obj['destinoX']:
        obj['velX'] = -1
    else:
        obj['velX'] = 1

    if obj['y'] == obj['destinoY']:
        obj['velY'] = 0
        chegou = chegou and True
    elif obj['y'] > obj['destinoY']:
        obj['velY'] = -1
    else:
        obj['velY'] = 1

    return chegou

def movimenta(obj):
    obj['x'] = obj['x'] + obj['velX']
    obj['y'] = obj['y'] + obj['velY']


def pintar( scr, obj ):
    scr.blit(obj['imagem'], (obj['x'], obj['y']))


def teste_colisao( obj1, obj2 ):
    r1 = obj1['imagem'].get_rect()
    r1.x = obj1['x']
    r1.y = obj1['y']
    r2 = obj2['imagem'].get_rect()
    r2.x = obj2['x']
    r2.y = obj2['y']

    if rect_colide(r1, r2):
        return True
    else:
        return False


ciclos = 0

tela = pygame.display.set_mode((800, 600), 0, 32)
imagem1 = pygame.image.load("./images/gato.png").convert_alpha()
imagem2 = pygame.image.load("./images/enemy.png").convert_alpha()
imagem3 = pygame.image.load("./images/explosion.png").convert_alpha()

rinimigo = imagem2.get_rect()
img_explod = pygame.transform.scale(imagem3, rinimigo.size)
explode = False

gato = {'x': 100, 'y': 100, 'velX': 0, 'velY': 0, 'imagem': imagem1}
inimigo = {'x': 400, 'y': 300, 'velX': 1,
           'velY': -1, 'imagem': imagem2, 'destinoX': 10, 'destinoY': 10}

while True:
    # Calcular Regras
    ciclos += 1
    movimenta(gato)
    chegou = calcula_velocidade(inimigo)
    movimenta(inimigo)

    if ciclos % 100 == 0 and chegou:
        # inimigo['destinoX'] = random.randint(50, 750)
        # inimigo['destinoY'] = random.randint(50, 550)
        inimigo['destinoX'] = gato['x']
        inimigo['destinoY'] = gato['y']

    # Desenhar na tela
    tela.fill((0, 0, 0))
    pintar(tela, gato)
    pintar(tela, inimigo)
    if teste_colisao(gato, inimigo):
        tela.blit(img_explod, (inimigo['x'], inimigo['y']))
    pygame.draw.circle(tela, (0, 255, 0), (600, 100), 50, 0)
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_d:
                gato['velX'] = 1
            elif e.key == K_a:
                gato['velX'] = -1
            elif e.key == K_w:
                gato['velY'] = -1
            elif e.key == K_s:
                gato['velY'] = 1
        elif e.type == KEYUP:
            if e.key == K_d:
                gato['velX'] = 0
            elif e.key == K_a:
                gato['velX'] = 0
            elif e.key == K_w:
                gato['velY'] = 0
            elif e.key == K_s:
                gato['velY'] = 0