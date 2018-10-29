'''
Created on 30/10/2014

@author: Aluno
'''

import json
import pygame

from tiles import TileSet, Layer
from pygame.constants import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN
from pygame.rect import Rect

filename = "mapa.json"

f = open( filename )

jobj = json.load( f )

ts = TileSet( jobj["tilesets"][0] )

print(jobj["tilesets"][0]["image"])

pygame.init()
screen = pygame.display.set_mode( (640, 480), 0, 32)

layer = Layer( jobj["layers"][0] )
layer.prepare( ts )
print(layer.width, layer.height)
x = 0
y = 0
velX = 20
velY = 20
clk = pygame.time.Clock()

cooldown = 1 * 1000

inicio = pygame.time.get_ticks()

cenario = Rect( (0, 0), (20 * 32, 20 * 32) )
while (True):
    screen.fill( (0, 0, 0) )
    
    r = Rect ((x, y), (200, 200))   
    
    img = layer.getFrameRect( r )
    
    screen.blit(img, (10, 10) )
            
    pygame.display.update()
      
    
    clk.tick( 60 )
    for e in pygame.event.get():
        
        if (e.type == QUIT):
            exit()
            
        if (e.type == KEYDOWN):
            if (e.key == K_RIGHT):
                velX = 1
            if (e.key == K_LEFT):
                velX = -1
            if (e.key == K_UP):
                velY = -1
            if (e.key == K_DOWN):
                velY = 1
                
        
    agora = pygame.time.get_ticks()
            
    if (agora > (inicio + cooldown)):
        inicio = agora
        rDesejavel = Rect ( (x + velX, y + velY), (201, 201) )
           
        if ( cenario.contains( rDesejavel ) ):
            x += velX
            y += velY
    
    