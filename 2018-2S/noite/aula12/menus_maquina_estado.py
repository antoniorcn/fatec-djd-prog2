import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, Rect
# 0 - Menu principal
# 1 - Jogando
# 2 - Pausado
# 3 - Menu configuracao
estado = 0

def calcular_menu( menu_opcoes ):
    for opcao in menu_opcoes:
        opcao_renderizada = font.render(opcao["text"], True, opcao["cor"])
        opcao["surface"] = opcao_renderizada
        opcao["rect"] = opcao_renderizada.get_rect()
        opcao["rect"].x = opcao["pos"][0]
        opcao["rect"].y = opcao["pos"][1]

def pintar_menu(scr, menu_opcoes):
    for opcao in menu_opcoes:
        scr.blit(opcao["surface"], opcao["pos"])


def capturar_menu(menu_opcoes, e):
    for opcao in menu_opcoes:
        if opcao["rect"].collidepoint(e.pos[0], e.pos[1]):
            opcao["execute"]()
            #pygame.draw.rect(tela, (255, 0, 0), opcao["rect"], 3)

def funcao_padrao():
    print("Executada funcao padrao")

def menu_configurar():
    global estado
    estado = 3

def menu_principal():
    global estado
    estado = 0

pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
font = pygame.font.Font("C:/WINDOWS/FONTS/JOKERMAN.TTF", 48)
lista_opcoes = []
lista_opcoes.append({"text": "Jogar", "pos": [100, 100], "cor": (255, 255, 0), "execute": funcao_padrao})
lista_opcoes.append({"text": "Configurar", "pos": [100, 200], "cor": (255, 255, 0), "execute": menu_configurar})
lista_opcoes.append({"text": "Sair", "pos": [100, 300], "cor": (255, 255, 0), "execute": exit})

lista_opcoes_config = []
lista_opcoes_config.append({"text": "Audio", "pos": [100, 100], "cor": (255, 255, 0), "execute": funcao_padrao})
lista_opcoes_config.append({"text": "Video", "pos": [100, 200], "cor": (255, 255, 0), "execute": funcao_padrao})
lista_opcoes_config.append({"text": "Mouse", "pos": [100, 300], "cor": (255, 255, 0), "execute": funcao_padrao})
lista_opcoes_config.append({"text": "Voltar", "pos": [100, 400], "cor": (255, 255, 0), "execute": menu_principal})

while True:
    tela.fill((0, 0, 0))
    # Calcular Regras
    if estado == 0:
        calcular_menu(lista_opcoes)
    elif estado == 3:
        calcular_menu(lista_opcoes_config)

    # Pintar
    if estado == 0:
        pintar_menu(tela, lista_opcoes)
    elif estado == 3:
        pintar_menu(tela, lista_opcoes_config)

    pygame.display.update()

    # Capturar Eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == MOUSEBUTTONDOWN:
            if estado == 0:
                capturar_menu(lista_opcoes, e)
            elif estado == 3:
                capturar_menu(lista_opcoes_config, e)


