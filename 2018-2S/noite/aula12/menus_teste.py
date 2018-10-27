
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, Rect

pygame.init()

tela = pygame.display.set_mode((800, 600), 0, 32)
font = pygame.font.Font("C:/WINDOWS/FONTS/JOKERMAN.TTF", 48)
opcao1 = font.render("Jogar", True, (255, 255, 0))
r1 = opcao1.get_rect()
r1.x = 100
r1.y = 100
# r2 = Rect()
while True:
    tela.blit(opcao1, (r1.x, r1.y))
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == MOUSEBUTTONDOWN:
            if r1.collidepoint(e.pos[0], e.pos[1]):
                pygame.draw.rect(tela, (255, 0, 0), r1, 3)


