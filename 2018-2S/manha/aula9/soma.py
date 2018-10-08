import pygame
from pygame import QUIT,MOUSEMOTION,MOUSEBUTTONDOWN,KEYDOWN,K_d,K_a,K_w,K_s,K_LEFT,K_RIGHT,K_UP,K_DOWN

pygame.init()
import random


screen = pygame.display.set_mode ((800, 600), 0, 32)

screen.set_at ((400, 300), (255, 255, 0))
red=0
azu=0
ver=0


red = random.randint(0, 255)
azu = random.randint(0, 255)
ver = random.randint(0, 255)
#red=255
#azu=0
#ver=0
# ys = random.randint(0, 400)
# xt = random.randint(100, 400)
#yt = random.randint(100, 400)
xs=100
ys=100
xt=200
yt=200
while True:
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (red, ver, azu), ((xs, ys), (xt, yt)) )

    pygame.display.update()
    for e in pygame.event.get():
        print(e)
        if e.type == QUIT:
            exit()
        #if e.type == MOUSEMOTION:
            #xs,ys=e.pos
        #if e.type == MOUSEBUTTONDOWN:
            #print("Pos:",e.pos,"Botao:".e.button)
        if e.type == KEYDOWN:
            if e.key == K_d or (e.key == K_RIGHT):
                xs = xs+5
            if e.key == K_a or (e.key == K_LEFT):
                xs = xs -5
            if e.key == K_w or (e.key == K_UP):
                ys = ys-5
            if (e.key == K_s) or (e.key == K_DOWN):
                ys = ys+5
    if xs >= 600 :
        xs=xs-5
    if xs <= 0 :
        xs=xs+5
    if ys >= 0 :
        ys=ys-5
    if ys <= 400 :
        ys=ys+5