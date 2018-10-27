import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, Rect
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
font = pygame.font.Font("C:/WINDOWS/FONTS/JOKERMAN.TTF", 48)
lista_opcoes = []
lista_opcoes.append({"text": "Jogar", "pos": [100, 100], "cor": (255, 255, 0)})
lista_opcoes.append({"text": "Configurar", "pos": [100, 200], "cor": (255, 255, 0)})
lista_opcoes.append({"text": "Sair", "pos": [100, 300], "cor": (255, 255, 0)})
while True:
    for opcao in lista_opcoes:
        opcao_renderizada = font.render(opcao["text"], True, opcao["cor"])
        opcao["rect"] = opcao_renderizada.get_rect()
        opcao["rect"].x = opcao["pos"][0]
        opcao["rect"].y = opcao["pos"][1]
        tela.blit(opcao_renderizada, opcao["pos"])
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == MOUSEBUTTONDOWN:
            for opcao in lista_opcoes:
                if opcao["rect"].collidepoint(e.pos[0], e.pos[1]):
                    pygame.draw.rect(tela, (255, 0, 0), opcao["rect"], 3)

