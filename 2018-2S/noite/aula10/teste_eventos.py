import pygame
from pygame import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT

pygame.init()
info = pygame.display.Info()
tela = pygame.display.set_mode(
    (info.current_w, info.current_h), 0, 32)

while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                print("Seta para cima")
            elif e.key == K_DOWN:
                print("Seta para baixo")
            elif e.key == K_LEFT:
                print("Seta para esquerda")
            elif e.key == K_RIGHT:
                print("Seta para direita")
            else:
                print(e.key, " - ", e.mod)
