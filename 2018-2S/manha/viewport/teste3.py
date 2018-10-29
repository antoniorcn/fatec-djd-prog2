import json
import pygame
from tiles import TileSet, Layer
from pygame.constants import QUIT, KEYDOWN, KEYUP, K_RIGHT, K_LEFT, K_UP, K_DOWN
from pygame.rect import Rect

VIEW_PORT_WIDTH = 400
VIEW_PORT_HEIGHT = 400

filename = "mapa.json"
f = open(filename)
jobj = json.load(f)

ts = TileSet(jobj["tilesets"][0])
pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)

layer = Layer(jobj["layers"][0])
layer.prepare(ts)
x = 0
y = 0
velX = 0
velY = 0
clk = pygame.time.Clock()
cooldown = 1 * 1
inicio = pygame.time.get_ticks()
cenario = Rect((0, 0), (20 * 32, 20 * 32))
while (True):

    #Pintar
    screen.fill((0, 0, 0))
    r = Rect((x, y), (VIEW_PORT_WIDTH, VIEW_PORT_HEIGHT))
    img = layer.get_frame_rect(r)
    screen.blit(img, (10, 10))
    pygame.display.update()
    
    clk.tick(120)

    #Capturar Eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN:
            if e.key == K_RIGHT:
                velX = 10
            if e.key == K_LEFT:
                velX = -10
            if e.key == K_UP:
                velY = -10
            if e.key == K_DOWN:
                velY = 10
        if e.type == KEYUP:
            if e.key == K_RIGHT:
                velX = 0
            if e.key == K_LEFT:
                velX = 0
            if e.key == K_UP:
                velY = 0
            if e.key == K_DOWN:
                velY = 0

    agora = pygame.time.get_ticks()

    if agora > (inicio + cooldown):
        inicio = agora
        rDesejavel = Rect((x + velX, y + velY),
                          (VIEW_PORT_WIDTH + 1, VIEW_PORT_HEIGHT + 1))
           
        if cenario.contains(rDesejavel):
            x += velX
            y += velY
    
    