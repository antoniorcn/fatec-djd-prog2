import pygame
from pygame import QUIT, KEYUP, KEYDOWN, K_UP, K_DOWN

pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
sprite_sheet = pygame.image.load("EpicArmor.png").convert_alpha()

sergio = {  "state": "images_state_down_run",
            "images_state_up_run":[1, 2, 3, 4, 5, 6, 7, 8],
            "images_state_up_stop":[0],
            "images_state_down_run": [19, 20, 21, 22, 23, 24, 25, 26],
            "images_state_down_stop": [18],
            "frame_index": 0
        }

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
    tela.blit(sur_frame, (400, 300))

clk = pygame.time.Clock()
while True:
    # Calcular Regras

    # Pintar
    tela.fill((0, 0, 0))
    anima(sergio)
    pygame.display.update()
    clk.tick(10)

    # Captura eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                sergio["state"] = "images_state_up_run"
            elif e.key == K_DOWN:
                sergio["state"] = "images_state_down_run"
        elif e.type == KEYUP:
            if e.key == K_UP:
                sergio["state"] = "images_state_up_stop"
            elif e.key == K_DOWN:
                sergio["state"] = "images_state_down_stop"