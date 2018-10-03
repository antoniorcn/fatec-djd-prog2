import pygame
from pygame.locals import QUIT, MOUSEMOTION, MOUSEBUTTONDOWN, KEYDOWN
import random
tela = pygame.display.set_mode((800, 600), 0, 32)
r = 0
g = 0
b = 0
x = 0
y = 0
while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # b = 100
    #x = random.randint(0, 800)
    #y = random.randint(0, 600)
    w = random.randint(0, 400)
    h = random.randint(0, 300)
    pygame.draw.rect(tela, (r, g, b),
                     ((x, y), (w, h)), 0)
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        if e.type == MOUSEMOTION:
            x, y = e.pos
        if e.type == MOUSEBUTTONDOWN:
            print("Pos:", e.pos, " Botao:", e.button)
        if e.type == KEYDOWN:
            print("Unicode: ", e.unicode, "  Mod:", e.mod, "  Key:", e.key)