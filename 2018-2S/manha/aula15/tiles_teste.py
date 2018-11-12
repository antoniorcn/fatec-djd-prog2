import json
import pygame
from pygame.locals import Rect, QUIT


pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)

filename = "./bombeman.json"
f = open(filename)
json_dict = json.load(f)
layer = json_dict["layers"][0]
print (layer)
tileset = json_dict["tilesets"][0]
img_w = tileset["imagewidth"]
img_h = tileset["imageheight"]
tile_w = tileset["tilewidth"]
tile_h = tileset["tileheight"]
space_x = 0
space_y = 0
if "tileoffset" in tileset:
    space_x = tileset["tileoffset"]["x"]
    space_y = tileset["tileoffset"]["y"]
top = tileset["spacing"]
margin = tileset["margin"]
firstgId = tileset["firstgid"]
tileset["surface"] = pygame.image.load(tileset["image"])
tileset["columns"] = (img_w - margin) / (tile_w + space_x)
tileset["lines"] = (img_h - top) / (tile_w + space_y)
tileset["lastgid"] = 1 - firstgId + (tileset["columns"] * tileset["lines"])
print(tileset["columns"])    # 8.0
print(tileset["lines"])      # 6.0
print(tileset["lastgid"])   # 48.0


def parse_layer(tile_set, layer):
    internal_structure = []
    for l in range(layer["height"]):
        celulas = []
        for c in range(layer["width"]):
            data_index = l * layer["width"] + c
            gid = layer["data"][data_index]
            brk = get_brick_by_tileset_gid(tile_set, gid)
            celulas.append(brk)
        internal_structure.append(celulas)
    layer["structure"] = internal_structure


def get_brick_by_tileset_gid(tileset, gId):
    currentFrame = (gId - tileset["firstgid"])
    column = currentFrame % tileset["columns"]
    line = int(currentFrame / tileset["columns"])
    space_x = 0
    space_y = 0
    if "tileoffset" in tileset:
        space_x = tileset["tileoffset"]["x"]
        space_y = tileset["tileoffset"]["y"]
    w = tileset["tilewidth"]
    h = tileset["tileheight"]
    x = tileset["margin"] + ((w + space_x) * column)
    y = tileset["spacing"] + ((h + space_y) * line)
    r = Rect((x, y), (w, h))
    image = tileset["surface"].subsurface(r)
    brick = {"tileset": tileset, "gid": gId, "image": image,
             "column": column, "line": line, "rect": r}
    return brick


parse_layer(tileset, layer)

while True:
    # Calcula regras

    # Desenha Tela
    #b = get_brick_by_tileset_gid(tileset, 0)
    '''
    b1 = layer["structure"][0][0]
    b2 = layer["structure"][0][1]
    b3 = layer["structure"][0][2]
    screen.blit(b1["image"], (10, 10))
    screen.blit(b2["image"], (40, 10))
    screen.blit(b3["image"], (80, 10))
'''

    for lin in range(0, 20):
        for col in range(0, 20):
            brk = layer["structure"][lin][col]
            r = brk["rect"]
            screen.blit(brk["image"], (col * r.w, lin * r.h))

    pygame.display.update()

    for e in pygame.event.get():
        if e.type == QUIT:
            exit()