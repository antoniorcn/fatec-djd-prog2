import pygame
from math import sqrt
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_d, K_a, K_w, K_s, Rect


def circle_point_collide(c, p):
    hipo = sqrt(abs(c['x'] - p['x']) ** 2 + abs(c['y'] - p['y']) ** 2)
    return hipo <= c['radius']


def clamp_on_range(x, min, max):
    if x < min:
        return min
    elif max < x:
        return max
    else:
        return x

def clamp_on_rectangle(p, r):
    clamp = {
            'x': clamp_on_range(p['x'], r.x, r.x + r.w),
            'y': clamp_on_range(p['y'], r.y, r.y + r.h)
            }
    return clamp

def circle_rectangle_collide(c, r):
    clamped = clamp_on_rectangle(c, r)
    return circle_point_collide(c, clamped)



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
    c1 = {'x':400, 'y':100, 'radius':50}

    if circle_rectangle_collide(c1, r1):
        cor = (255, 255, 0)
    else:
        cor = (0, 0, 255)

    # Desenhar na tela
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 0, 0), ((x, y), (200, 100)), 0)
    pygame.draw.circle(tela, cor, (c1['x'], c1['y']), c1['radius'], 0)
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