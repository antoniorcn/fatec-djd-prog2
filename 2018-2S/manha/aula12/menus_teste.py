import pygame
from pygame import QUIT, KEYUP, KEYDOWN, \
                    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, \
                    MOUSEBUTTONDOWN

#Inicialização
# 0 - Menu principal
# 1 - Jogando
# 2 - Pausado
state = 0   #Menu Principal
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
sprite_sheet = pygame.image.load("EpicArmor.png").convert_alpha()

sergio = {  "pos": [400, 300],
            "velX":0,
            "velY":0,
            "state": "images_state_down_run",
            "images_state_up_run":[1, 2, 3, 4, 5, 6, 7, 8],
            "images_state_up_stop":[0],
            "images_state_down_run": [19, 20, 21, 22, 23, 24, 25, 26],
            "images_state_down_stop": [18],
            "images_state_left_run": [10, 11, 12, 13, 14, 15, 16, 17],
            "images_state_left_stop": [9],
            "images_state_right_run": [28, 29, 30, 31, 32, 33, 34, 35],
            "images_state_right_stop": [27],
            "frame_index": 0
        }

def estado_jogar():
    global state
    state = 1

def estado_configurar():
    print ("Clicou na configuração")

jogar = {"texto":"Jogar", "pos":[100, 100], "cor":(255, 255, 0), "funcao":estado_jogar}
config = {"texto":"Configurar", "pos":[100, 200], "cor":(255, 255, 0), "funcao":estado_configurar}

font = pygame.font.Font("C:/WINDOWS/FONTS/ALGER.TTF", 48)

def pintar_opcao(scr, obj):
    sur_opcao = font.render(obj["texto"], True, obj["cor"])
    scr.blit(sur_opcao, obj["pos"])
    obj["renderizado"] = sur_opcao

def testa_colisao(obj, e):
    global state
    r1 = obj["renderizado"].get_rect()
    r1.x = obj["pos"][0]
    r1.y = obj["pos"][1]
    if r1.collidepoint(e.pos):
        obj["funcao"]()

def atualizar_regra_personagem( obj ):
    obj["pos"][0] += (obj["velX"] * 10)
    obj["pos"][1] += (obj["velY"] * 10)
    #if obj["velY"] < 1:
    obj["velY"] += 1
    if obj["pos"][1] > 530:
        obj["pos"][1] = 530
        obj["velY"] = 0

def get_frame( gId ):
    global sprite_sheet
    top = 0
    margin = 0
    space_h = 0
    space_v = 0
    width = 64
    height = 64
    columns = 9
    coluna = gId % columns
    linha = int(gId / columns)
    x = margin + (coluna * (width + space_h))
    y = top + (linha * (height + space_v))
    img = sprite_sheet.subsurface(x, y, width, height)
    return img

def anima( obj ):
    global tela
    chave = obj["state"]
    frames = obj[chave]
    obj["frame_index"] += 1
    if obj["frame_index"] >= len(frames) - 1:
        obj["frame_index"] = 0
    gId = frames[obj["frame_index"]]
    sur_frame = get_frame(gId)
    tela.blit(sur_frame, obj["pos"])

#Loop do Jogo
clk = pygame.time.Clock()
while True:
    # Calcular Regras
    if state == 1:
        atualizar_regra_personagem(sergio)

    # Pintar
    tela.fill((0, 0, 0))
    if state == 1:
        anima(sergio)
    elif state == 0:
        pintar_opcao(tela, jogar)
        pintar_opcao(tela, config)
    pygame.display.update()
    clk.tick(10)

    # Captura eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN and state == 1:
            if e.key == K_UP:
                sergio["state"] = "images_state_up_run"
                sergio["velY"] = -1
            elif e.key == K_DOWN:
                sergio["state"] = "images_state_down_run"
                sergio["velY"] = 1
            elif e.key == K_LEFT:
                sergio["state"] = "images_state_left_run"
                sergio["velX"] = -1
            elif e.key == K_RIGHT:
                sergio["state"] = "images_state_right_run"
                sergio["velX"] = 1
            elif e.key == K_SPACE:
                sergio["velY"] = -5
        elif e.type == KEYUP:
            if e.key == K_UP:
                sergio["state"] = "images_state_up_stop"
                sergio["velY"] = 0
            elif e.key == K_DOWN:
                sergio["state"] = "images_state_down_stop"
                sergio["velY"] = 0
            elif e.key == K_LEFT:
                sergio["state"] = "images_state_left_stop"
                sergio["velX"] = 0
            elif e.key == K_RIGHT:
                sergio["state"] = "images_state_right_stop"
                sergio["velX"] = 0
        elif e.type == MOUSEBUTTONDOWN:
            testa_colisao(jogar, e)
            testa_colisao(config, e)