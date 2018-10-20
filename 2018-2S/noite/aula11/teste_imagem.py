import pygame
import random
from pygame import QUIT, KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE

def calculaTiros( lista ):
    for tiro in lista:
        tiro['pos'][1] += tiro['velY']

def calculaHeroi( hero ):
    hero['pos'][0] += hero['velX']
    hero['pos'][1] += hero['velY']

def calculaInimigo( inimigo ):
    if (inimigo['pos'][0] != inimigo['destino'][0]):
        inimigo['pos'][0] += inimigo['velX']

    if (inimigo['pos'][1] != inimigo['destino'][1]):
        inimigo['pos'][1] += inimigo['velY']

    if (inimigo['pos'] == inimigo['destino']):
        inimigo['destino'] = [random.randint(50, 500), random.randint(50, 400)]
        if inimigo['destino'][0] > inimigo['pos'][0]:
            inimigo['velX'] = 1
        else:
            inimigo['velX'] = -1

        if inimigo['destino'][1] > inimigo['pos'][1]:
            inimigo['velY'] = 1
        else:
            inimigo['velY'] = -1


pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
enemy = pygame.image.load("images/enemy.png").convert_alpha()
heroi_img = pygame.image.load("images/hero.png").convert_alpha()
tiro_img = pygame.image.load("images/shot.png").convert_alpha()
#font = pygame.font.SysFont("arial", 48, False, False)
font = pygame.font.Font("C:\WINDOWS\FONTS\BAUHS93.TTF", 48)
#enemy_convertida = enemy.convert_alpha()
imgPontos = font.render("Pontos : 10", True, (255, 255, 0))
imgVidas = font.render("Vidas : 3", True, (255, 255, 0))
enemy1 = {'pos':[100, 100], 'velX':1, 'velY':1, 'destino':[500, 400], 'imagem':enemy}
enemy2 = {'pos':[500, 100], 'velX':1, 'velY':1, 'destino':[600, 400], 'imagem':enemy}
heroi = {'pos':[400, 500], 'velX':0, 'velY':0, 'destino':[400, 500], 'imagem':heroi_img}
lista_tiros = []
while True:
    #Calcular regras
    calculaInimigo(enemy1)
    calculaInimigo(enemy2)
    calculaHeroi(heroi)
    calculaTiros(lista_tiros)

    #Desenhar a tela
    tela.fill((0, 0, 0))
    # Pinta imagem
    tela.blit(enemy1['imagem'], enemy1['pos'])
    tela.blit(enemy2['imagem'], enemy2['pos'])
    tela.blit(heroi['imagem'], heroi['pos'])
    for tiro in lista_tiros:
        tela.blit(tiro['imagem'], tiro['pos'])
    tela.blit(imgPontos, (550, 10))
    tela.blit(imgVidas, (50, 10))
    pygame.display.update()
    # Captura eventos
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                heroi['velX'] = -1
            elif e.key == K_RIGHT:
                heroi['velX'] = 1
            elif e.key == K_SPACE:
                lista_tiros.append({'pos':heroi['pos'].copy(), 'velY':-1, 'imagem':tiro_img})

