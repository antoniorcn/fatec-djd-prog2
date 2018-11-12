import Box2D as b2
import pygame
from pygame.locals import QUIT
import math

g = (0, -9.8)

screen = pygame.display.set_mode((800, 600), 0, 32)

PPM = 800 / 100

def draw(corpo):
    for fix in corpo.fixtures:
        if fix.type == b2.b2Shape.e_circle:
            pos = corpo.position
            x = int(pos[0] * PPM)
            y = 600 - int(pos[1] * PPM)
            raio = int(fix.shape.radius * PPM)
            pygame.draw.circle(screen, (255, 255, 0), (x, y), raio, 0)
        elif fix.type == b2.b2Shape.e_polygon:
            lista_pontos = []
            vertices = fix.shape.vertices
            for vertice in vertices:
                v = corpo.transform * vertice * PPM
                x = int(v[0] * PPM)
                y = 600 - int(v[1] * PPM)
                lista_pontos.append([x, y])
            pygame.draw.polygon(screen, (255, 255, 0), lista_pontos)

# Criando o mundo
cenario = b2.b2World(g, True)

# Definição do corpo
corpoDef = b2.b2BodyDef()
corpoDef.position = (1, 50)
corpoDef.angle = 0
corpoDef.type = b2.b2_dynamicBody

# Definição do Piso
pisoDef = b2.b2BodyDef()
pisoDef.position = (0, 0)
pisoDef.angle = -10 * math.pi / 180
pisoDef.type = b2.b2_staticBody

# Criar o corpo com a definição
piso = cenario.CreateBody(pisoDef)

# Criar o corpo com a definição
corpo = cenario.CreateBody(corpoDef)

# Definição do Fixture
fixDef = b2.b2FixtureDef()
fixDef.restitution = 0.9
fixDef.friction = 0.6
fixDef.density = 3
fixDef.shape = b2.b2CircleShape(radius=1)

# Definição do Fixture Piso
pisoFixDef = b2.b2FixtureDef()
pisoFixDef.restitution = 0.5
pisoFixDef.friction = 0.6
pisoFixDef.density = 1
pisoFixDef.shape = b2.b2PolygonShape(box=(50, 2))


# Associa o Fixture ao corpo
corpo.CreateFixture( fixDef )
piso.CreateFixture( pisoFixDef )

while True:
    # Calcula regras
    cenario.Step(1.0/30.0, 8, 3)

    # Desenha cenario
    screen.fill((0, 0, 0))
    draw(corpo)
    draw(piso)

    pygame.display.update()

    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
