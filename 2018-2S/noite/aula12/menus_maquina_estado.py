import pygame
import time
import os
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, \
    K_SPACE, K_ESCAPE, K_UP, K_DOWN, Rect
# 0 - Menu principal
# 1 - Jogando
# 2 - Pausado
# 3 - Menu configuracao
estado = 0
indice_menu = 0

clk = pygame.time.Clock()

tempo = 0

def calcular_menu( menu_opcoes ):
    global indice_menu
    for opcao in menu_opcoes:
        opcao_renderizada = font.render(opcao["text"], True, opcao["cor"])
        opcao["surface"] = opcao_renderizada
        opcao["rect"] = opcao_renderizada.get_rect()
        opcao["rect"].x = opcao["pos"][0]
        opcao["rect"].y = opcao["pos"][1]
    if indice_menu < 0:
        indice_menu = 0

    if indice_menu >= len(menu_opcoes):
        indice_menu = len(menu_opcoes) - 1


def pintar_menu(scr, menu_opcoes):
    global indice_menu
    for opcao in menu_opcoes:
        scr.blit(opcao["surface"], opcao["pos"])
    menu_selecionado = menu_opcoes[indice_menu]
    pos = menu_selecionado["pos"]
    pygame.draw.circle(scr, (255, 255, 0), pos, 10)


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

def menu_jogar():
    global estado
    estado = 1

#os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (600, 200)
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
font = pygame.font.Font("C:/WINDOWS/FONTS/JOKERMAN.TTF", 48)
lista_opcoes = []
lista_opcoes.append({"text": "Jogar", "pos": [100, 100], "cor": (255, 255, 0), "execute": menu_jogar})
lista_opcoes.append({"text": "Configurar", "pos": [100, 200], "cor": (255, 255, 0), "execute": menu_configurar})
lista_opcoes.append({"text": "Sair", "pos": [100, 300], "cor": (255, 255, 0), "execute": exit})

lista_opcoes_config = []
lista_opcoes_config.append({"text": "Audio", "pos": [100, 100], "cor": (255, 255, 0), "execute": funcao_padrao})
lista_opcoes_config.append({"text": "Video", "pos": [100, 200], "cor": (255, 255, 0), "execute": funcao_padrao})
lista_opcoes_config.append({"text": "Mouse", "pos": [100, 300], "cor": (255, 255, 0), "execute": funcao_padrao})
lista_opcoes_config.append({"text": "Voltar", "pos": [100, 400], "cor": (255, 255, 0), "execute": menu_principal})

bola = {"pos": [10, 10], "velX": 1, "velY": 1, "cor": (255, 0, 0)}
tempo_inicial = (int(round(time.time())) % 10000)
while True:
    tela.fill((0, 0, 0))
    # Calcular Regras

    tempo = (int(round(time.time())) % 10000) - tempo_inicial
    if estado == 0:
        calcular_menu(lista_opcoes)
    elif estado == 1:
        bola["pos"][0] += bola["velX"]
        bola["pos"][1] += bola["velY"]
        if bola["pos"][0] < 0:
            bola["velX"] = 1
        elif bola["pos"][0] > 800:
            bola["velX"] = -1
        if bola["pos"][1] < 0:
            bola["velY"] = 1
        elif bola["pos"][1] > 600:
            bola["velY"] = -1
    elif estado == 3:
        calcular_menu(lista_opcoes_config)

    # Pintar
    if estado == 0:
        pintar_menu(tela, lista_opcoes)
    elif estado == 1:
        pygame.draw.circle(tela, bola["cor"], bola["pos"], 20)
        tempo_img = font.render("Tempo: " + str(tempo), True, (255, 255, 0))
        tela.blit(tempo_img, (100, 50))
    elif estado == 2:
        pygame.draw.circle(tela, bola["cor"], bola["pos"], 20)
        pausado_img = font.render("PAUSADO", True, (255, 255, 0))
        tela.blit(pausado_img, (200, 200))
    elif estado == 3:
        pintar_menu(tela, lista_opcoes_config)

    pygame.display.update()
    clk.tick(1000)

    # Capturar Eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == MOUSEBUTTONDOWN:
            if estado == 0:
                capturar_menu(lista_opcoes, e)
            elif estado == 3:
                capturar_menu(lista_opcoes_config, e)
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if estado == 1:
                    estado = 2
                elif estado == 2:
                    estado = 1
            elif e.key == K_ESCAPE:
                estado = 0

            if estado == 0 or estado == 3:
                if e.key == K_UP:
                    indice_menu -= 1
                elif e.key == K_DOWN:
                    indice_menu += 1

            if estado == 0:
                if e.key == K_SPACE:
                    lista_opcoes[indice_menu]["execute"]()
                    indice_menu = 0

            if estado == 3:
                if e.key == K_SPACE:
                    lista_opcoes_config[indice_menu]["execute"]()
                    indice_menu = 0

