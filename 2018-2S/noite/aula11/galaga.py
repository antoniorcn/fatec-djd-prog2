import pygame
import random
from pygame import QUIT, KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE

inimigos = 20
destinos = [[random.randint(50, 500), random.randint(50, 400)] for _ in range(10)]
def testa_colisao( obj1, obj2 ):
    r1 = pygame.Rect(obj1['pos'], obj1['size'])
    r2 = pygame.Rect(obj2['pos'], obj2['size'])
    return r1.colliderect(r2)


def calcular_tiros(lista):
    for tiro in lista:
        if tiro['status'] == 'vivo':
            tiro['pos'][1] += tiro['velY']
            if tiro['pos'][1] < 0:
                lista.remove(tiro)
        else:
            lista.remove(tiro)


def calcular_heroi(hero):
    hero['pos'][0] += hero['velX']
    hero['pos'][1] += hero['velY']


def calculate_new_velocity( inimigo ):
    global destinos
    destino = destinos[inimigo['destinoId']]
    if destino[0] > inimigo['pos'][0]:
        inimigo['velX'] = 1
    else:
        inimigo['velX'] = -1
    if destino[1] > inimigo['pos'][1]:
        inimigo['velY'] = 1
    else:
        inimigo['velY'] = -1


def calcular_inimigo(inimigo):
    global destinos
    destino = destinos[inimigo['destinoId']]
    if inimigo['status'] == 'vivo':
        if inimigo['pos'][0] != destino[0]:
            inimigo['pos'][0] += inimigo['velX']

        if inimigo['pos'][1] != destino[1] :
            inimigo['pos'][1] += inimigo['velY']

        if inimigo['pos'] == destino:
            if inimigo['head']:
                destinos.append([random.randint(50, 500), random.randint(50, 400)])
            inimigo['destinoId'] += 1
            calculate_new_velocity(inimigo)


def pintar(scr, obj):
    if obj['status'] == 'vivo':
        scr.blit(obj['imagem'], obj['pos'])


def generate_inimigos(lista):
    global inimigos
    x = 100
    for i in range(inimigos):
        e = {'pos':[x, 100], 'velX':1, 'velY':1,
             'destinoId': 0, 'imagem':enemy,
             'size':[38, 37], 'status':'vivo', 'head':False}
        calculate_new_velocity(e)
        if i == 0:
            e['head'] = True
        lista.append( e )
        x -= 50

def get_primeiro_inimigo_vivo(lista):
    for e in lista:
        if e['status'] == 'vivo':
            return e

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
heroi = {'pos':[400, 500], 'velX':0, 'velY':0, 'destino':[400, 500], 'imagem':heroi_img, 'size':[70, 39], 'status':'vivo'}
lista_tiros = []
lista_inimigos = []
generate_inimigos(lista_inimigos)
while True:
    #Calcular regras
    for inimigo in lista_inimigos:
        calcular_inimigo(inimigo)
    calcular_heroi(heroi)
    calcular_tiros(lista_tiros)

    for tiro in lista_tiros:
        remove_tiro = False
        for inimigo in lista_inimigos:
            if testa_colisao(inimigo, tiro):
                inimigo['status'] = 'morto'
                if inimigo['head']:
                    get_primeiro_inimigo_vivo(lista_inimigos)['head']=True
                lista_inimigos.remove(inimigo)
                remove_tiro = True
        if remove_tiro:
            lista_tiros.remove(tiro)

    #Desenhar a tela
    tela.fill((0, 0, 0))
    # Pinta imagem
    for inimigo in lista_inimigos:
        pintar(tela, inimigo)

    pintar(tela, heroi)
    for tiro in lista_tiros:
        pintar(tela, tiro)
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
                lista_tiros.append({'pos':heroi['pos'].copy(), 'velY':-1, 'imagem':tiro_img, 'size':[5, 22], 'status':'vivo'})

