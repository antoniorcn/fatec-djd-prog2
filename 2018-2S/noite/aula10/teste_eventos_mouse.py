import pygame
from pygame import QUIT, MOUSEMOTION, MOUSEBUTTONDOWN

pygame.init()
info = pygame.display.Info()
tela = pygame.display.set_mode(
    (info.current_w, info.current_h), 0, 32)

while True:
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == MOUSEMOTION:
            # tela.set_at((255, 255, 0), (e.pos[0], e.pos[1]))
            if e.buttons[0] == 1:
                tela.set_at(e.pos, (255, 255, 0))
        elif e.type == MOUSEBUTTONDOWN:
            print("Botão pressionado : ", e.button)

