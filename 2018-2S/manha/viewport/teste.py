'''
Created on 30/10/2014

@author: Aluno
'''

import json
import pygame

from tiles import TileSet, Layer
from pygame.constants import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, KEYUP
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
x = 50
y = 50
velX = 0
velY = 0
while (True):
    screen.fill( (0, 0, 0) )
    
    for linha in range(layer.height):
        for coluna in range(layer.width): 
            b = layer.internal_structure[linha][coluna]
            x = coluna * b.rect.width
            y = linha * b.rect.height
            screen.blit( b.image, (x, y) )  
            
    pygame.display.update()            
                  
#     r1 = Rect( (x, y), (150, 150) )
#     
#     r2 = Rect( (x, y), (100, 100) )
# 
#     i1 = layer.getFrameRect( r1 )
#         
#     i2 = layer.getFrameRect( r2 )
#     
#     screen.blit( i1, (10, 10))    
#     screen.blit( i2, (300, 10))
#     pygame.display.update()
#     
#     x = x + velX
#     y = y + velY
    
    for e in pygame.event.get():
        
        if (e.type == QUIT):
            exit()
        elif (e.type == KEYDOWN):
            if (e.key == K_RIGHT):
                velX = 1
            if (e.key == K_LEFT):
                velX = -1
            if (e.key == K_UP):
                velY = -1
            if (e.key == K_DOWN):
                velY = 1
        elif (e.type == KEYUP):
            if (e.key == K_RIGHT or e.key == K_LEFT):
                velX = 0
            if (e.key == K_UP or e.key == K_DOWN):
                velY = 0
                                                                