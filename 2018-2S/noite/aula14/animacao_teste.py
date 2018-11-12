import pygame
from pygame import QUIT, KEYDOWN, KEYUP, K_SPACE, K_RIGHT, K_LEFT

screen = pygame.display.set_mode((800, 600), 0, 32)

img = pygame.image.load("EpicArmor.png").convert_alpha()
img_dwarf = pygame.image.load("dwarf.png").convert_alpha()

def get_frame(sprite_sheet, gId, columns, width, height,
                margin=0, top=0, space_v=0, space_h=0):
    col = gId % columns
    lin = int(gId / columns)
    x = margin + (col * (width + space_h))
    y = top + (lin * (height + space_v))
    frame = sprite_sheet.subsurface(x, y, width, height)
    return frame


def update_frame( sprite ):
    lista_estado = sprite[sprite["estado_atual"]]
    sprite["frame_index"] += 1
    if sprite["frame_index"] > len(lista_estado) - 1:
        sprite["frame_index"] = 0


thiago = {  "sprite_sheet":img_dwarf,
            "andando_dir": [10, 11, 12, 13, 14, 15, 16, 17],
            "parado_dir": [10],
            "andando_esq": [60, 61, 62, 63, 64, 65, 66, 67],
            "machado": [20, 21, 22, 23, 24, 25, 26],
            "estado_atual": "andando_dir",
            "frame_index": 0}

clk = pygame.time.Clock()
while True:
    print(pygame.key.get_pressed()[K_LEFT],
          pygame.key.get_pressed()[K_SPACE])
    #Calcular Regras
    update_frame(thiago)

    #Pintar a tela
    screen.fill((0, 0, 0))
    gId = thiago[thiago["estado_atual"]][thiago["frame_index"]]
    sprite_dwarf = get_frame(thiago["sprite_sheet"], gId
                             , 10, 32, 32)

    sprite_dwarf_large = pygame.transform.scale(sprite_dwarf, (128, 128))
    screen.blit(sprite_dwarf_large, (600, 300))
    pygame.display.update()
    clk.tick(20)

    #Capturar Eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                thiago["estado_atual"] = "machado";
            elif e.key == K_RIGHT:
                thiago["estado_atual"] = "andando_dir";
            elif e.key == K_LEFT:
                thiago["estado_atual"] = "andando_esq";
        elif e.type == KEYUP:
            if e.key == K_RIGHT:
                thiago["estado_atual"] = "parado_dir";


