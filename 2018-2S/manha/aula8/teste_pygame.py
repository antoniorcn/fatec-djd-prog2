import pygame, random
pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)

screen.set_at((400, 300), (255, 255, 0))

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    x = random.randint(0, 600)
    y = random.randint(0, 400)
    w = random.randint(0, 400)
    h = random.randint(0, 300)
    pygame.draw.rect(screen, (r, g, b), ((x, y), (w, h)))
    pygame.display.update()

print("Fim do programa")
