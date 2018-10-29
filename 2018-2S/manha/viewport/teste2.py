'''
Created on 30/10/2014

@author: Aluno
'''
import pygame
from pygame.constants import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, KEYUP
from pygame.rect import Rect



def drawTabuleiro (surface, colunas, linhas, width, height):
    for l in range(linhas):
        for c in range(colunas):
            x = c * width
            y = l * height
            pygame.draw.rect(surface, (0, 0, 0), Rect( (x, y), (width, height) ), 1)

pygame.init()
screen = pygame.display.set_mode( (640, 480), 0, 32)



x = 50
y = 50
while (True):
    screen.fill( (255, 255, 255) )

    drawTabuleiro( screen, 8, 8, 32, 32 )
    
    pygame.display.update()
    
    for e in pygame.event.get():
        
        if (e.type == QUIT):
            exit()
