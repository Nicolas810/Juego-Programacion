import pygame
import random

pygame.init()

flecha = False

reloj = pygame.time.Clock()

dimensiones = (596, 387)

pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Programacion 2")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

fondo = pygame.image.load("fondopre.png").convert()

torre = pygame.image.load("torrepre.bmp").convert()
torre = pygame.transform.scale(torre, (225, 140))
torre.set_colorkey(BLANCO)

defensor = pygame.image.load("hombrepre.bmp").convert()
defensor = pygame.transform.scale(defensor, (100, 100))
defensor.set_colorkey(BLANCO)

flecha = pygame.image.load("lanzapre.png").convert()


personaje = defensor

pos = pygame.mouse.get_pos()

hecho = False

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    pantalla.blit(fondo, [0, 0])
    pantalla.blit(torre, [10, 200])
    pantalla.blit(defensor, [35, 105])

    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
