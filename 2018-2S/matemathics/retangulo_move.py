import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_d, K_a, K_w, K_s, Rect
import math
tela = pygame.display.set_mode((800, 600), 0, 32)
r1 = {"rect":Rect((100, 100), (200, 100)),
      "velX":0, "velY":0, "cor":(255, 0, 0)}
cor = (0, 0, 255)
h = 1
a = 87.0 / 180.0 * math.pi
vel = 200.0
tempo = 1.0
acc = 0.01
g = 9.8
while True:
    x = vel * math.cos(a) * (tempo)
    y = (h + vel * math.sin(a) * (tempo) - (0.5 * g * ((tempo) ** 2)))
    print ("X: {}   Y: {}".format(x, y))
    # Calcular Regras
    # r1["rect"].x = r1["rect"].x + r1["velX"]
    # r1["rect"].y = r1["rect"].y + r1["velY"]
    r1["rect"].x = int(x)
    r1["rect"].y = 600 - int(y)

    tempo += acc
    r2 = Rect((400, 300), (100, 100))

    if r1["rect"].colliderect(r2):
        cor = (255, 255, 0)
    else:
        cor = (0, 0, 255)

    # Desenhar na tela
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, r1["cor"], r1["rect"], 0)
    pygame.draw.rect(tela, cor, r2, 0)
    pygame.display.update()

    # Capturar eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_d:
                r1["velX"] = 1
            elif e.key == K_a:
                r1["velX"] = -1
            elif e.key == K_w:
                r1["velY"] = -1
            elif e.key == K_s:
                r1["velY"] = 1
        elif e.type == KEYUP:
            if e.key == K_d:
                r1["velX"] = 0
            elif e.key == K_a:
                r1["velX"] = 0
            elif e.key == K_w:
                r1["velY"] = 0
            elif e.key == K_s:
                r1["velY"] = 0

