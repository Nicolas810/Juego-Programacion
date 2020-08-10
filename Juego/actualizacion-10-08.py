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

fondo1 = pygame.image.load("fondopre.png").convert()

torre1 = pygame.image.load("torrepre.bmp").convert()
torre1 = pygame.transform.scale(torre1, (225, 140))
torre1.set_colorkey(BLANCO)

enemigo1 = pygame.image.load("jabalipre.bmp").convert()
enemigo1 = pygame.transform.scale(enemigo1, (700, 400))
enemigo1.set_colorkey(BLANCO)

flecha = pygame.image.load("lanzapre.png").convert()

class Personaje(pygame.sprite.Sprite):
	defensor1 = pygame.image.load("hombrepre.bmp").convert()
	defensor1 = pygame.transform.scale(defensor1, (100, 100))
	defensor1.set_colorkey(BLANCO)


class enemigo1:
	def__init__(self, posx)
	self.derecha = True
	self.contador = 0
		
	def comoportamiento(self, tiempo):
		self.movimientos()
			
	def __movimientos(self):
		if self.contador >3:
			self.__movimientoLateral()
			
	def __movimientoLateral(self):
		if self.derecha == True:
			self.rect.left = self.rect.left+ self.velocidad
			
			if self.rect.left > 500:
				self.derecha = False
				self.contador +=1
		else:
			self.rect.left = self.rect.left - self.velocidad
			if self.rct.left <0:
				sself.derecha = True
		
personaje = defensor1(35, 105)

pos = pygame.mouse.get_pos()

hecho = False

while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            hecho = True
	


    pantalla.blit(fondo1, [0, 0])
    pantalla.blit(torre1, [10, 200])
    pantalla.blit(defensor1)
    pantalla.blit(enemigo1, [200 ,120])

    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
