import pygame
from pygame.locals import QUIT, KEYDOWN, K_d, K_a
tela = pygame.display.set_mode((800, 600), 0, 32)
r = 255
g = 0
b = 0
x = 100
y = 100
w = 200
h = 100
while True:
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (r, g, b), ((x, y), (w, h)), 0)
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_d:
                x = x + 5
            elif e.key == K_a:
                x = x - 5
