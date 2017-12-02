import pygame
import math
import sys
from pygame.locals import K_LEFT, K_RIGHT, K_SPACE, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEMOTION, QUIT, Rect

screen = pygame.display.set_mode( (800, 600), 0 , 32 )
tiros = []


class Tiro(object):
    def __init__(self, tiro_def, sprite_ref):
        self.tiro_def = tiro_definition


tiro_definition = {
}

tank = {
    'spritesheet':  {
        'image': pygame.image.load("./assets/image/tank.png").convert_alpha(),
        'rows':  7,
        'columns': 9,
        'margin': (6, 6, 0, 0)  # left, top, right, bottom
    },
    'frame_index': 0,
    'frame_delay': 0,
    'frame_delay_animation_max': 50,
    'pos': [350, 500],
    'size': [71, 70],
    'vel_x': 0,
    'vel_y': 0,
    'states' : {
        'MOVING_CANNON': range(18, 27) + range(26, 19, -1),
        'MOVING_LEFT': range(0, 6),
        'MOVING_RIGHT': range(14, 9, -1),
        'POINTING_LEFT': range(18, 27),
        'POINTING_RIGHT': range(27, 36)
    },
    'state_current' : 'MOVING_RIGHT'
}

inimigo = {
    'spritesheet':  {
        'image': pygame.image.load("./assets/image/alien_space_ship.png").convert_alpha(),
        'rows':  2,
        'columns': 3,
        'margin': (1, 0, 0, 0)  # left, top, right, bottom
    },
    'frame_index': 0,
    'frame_delay': 0,
    'frame_delay_animation_max': 50,
    'pos': [150, 50],
    'size': [91, 91],
    'vel_x': 0,
    'vel_y': 0,
    'states' : {
        'MOVING': [0, 1, 2, 1],
    },
    'state_current' : 'MOVING'
}


def get_pos_from_center( sprite ):
    x = sprite['pos'][0] - (sprite['size'][0] / 2)
    y = sprite['pos'][1] - (sprite['size'][1] / 2)
    return x, y


def get_image_frame(image_info, frame_index):
    rows = image_info['rows']
    columns = image_info['columns']
    linha = frame_index / columns
    coluna = frame_index % columns
    width = image_info['image'].get_width()
    height = image_info['image'].get_height()
    frame_width = (width - (image_info['margin'][0] + image_info['margin'][2])) / columns
    frame_height = (height - (image_info['margin'][1] + image_info['margin'][3])) / rows
    x = (coluna * frame_width) + image_info['margin'][0]
    y = (linha * frame_height) + image_info['margin'][1]
    # print "Frame {} frame_width:{}  frame_height:{}  Coluna:{}   Linha:{}   X:{}   Y:{}".format(frame_index, frame_width, frame_height, coluna, linha, x, y)
    image = image_info['image'].subsurface(Rect((x, y), (frame_width, frame_height)))
    return image


def draw_sprite(sprite, perform_animation):
    current_state = sprite['state_current']
    animation_list = sprite['states'][current_state]
    if perform_animation:
        sprite['frame_delay'] += 1
        if sprite['frame_delay'] > sprite['frame_delay_animation_max']:
            sprite['frame_delay'] = 0
            sprite['frame_index'] += 1
    if sprite['frame_index'] >= len(animation_list):
        sprite['frame_index'] = 0
    img = get_image_frame(sprite['spritesheet'], animation_list[sprite['frame_index']])
    if img.get_width() != sprite['size'][0] or img.get_height() != sprite['size'][1]:
        img = pygame.transform.scale(img, sprite['size'])
    screen.blit(img, get_pos_from_center(sprite))


def calcular_regras():
    tank['pos'][0] += tank['vel_x']
    tank['pos'][1] += tank['vel_y']


def pintar_tela():
    screen.fill((0, 0, 0))
    draw_sprite(tank, False)
    draw_sprite(inimigo, True)
    pygame.display.update()


def calc_cannon_position( mouse_pos ):
    dx = mouse_pos[0] - tank['pos'][0]
    dy = mouse_pos[1] - tank['pos'][1]
    h = math.sqrt(dx * dx + dy * dy)
    seno = dy / h
    if seno > 0:
        seno = 0
    coseno = dx / h
    angulo_rad = math.asin(seno)
    angulo = angulo_rad / math.pi * 180
    if coseno < 0:
        angulo = - angulo
    else:
        angulo = 180 + angulo
    if tank['state_current'] == 'MOVING_LEFT':
        tank['state_current'] = 'POINTING_LEFT'
    elif tank['state_current'] == 'MOVING_RIGHT':
        tank['state_current'] = 'POINTING_RIGHT'

    tank['frame_index'] = math.trunc(angulo / 20)
    tank['frame_index'] %= 9

    print "State Current {}   Frame :{}  Seno {}  Coseno {}  Angulo {}".format(tank['state_current'], tank['frame_index'], seno, coseno, angulo)


def capturar_eventos():
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                tank['vel_x'] = -1
                tank['state_current'] = 'MOVING_LEFT'
            elif e.key == K_RIGHT:
                tank['vel_x'] = 1
                tank['state_current'] = 'MOVING_RIGHT'
            elif e.key == K_SPACE:
                tiros.append(Tiro(tiro_definition, tank))
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                tank['vel_x'] = 0
            elif e.key == K_RIGHT:
                tank['vel_x'] = 0
        elif e.type == MOUSEMOTION:
            calc_cannon_position( e.pos )


def main(argv):
    while True:
        calcular_regras()
        pintar_tela()
        capturar_eventos()

if __name__ == "__main__":
    print "Inicio do jogo"
    main(sys.argv)