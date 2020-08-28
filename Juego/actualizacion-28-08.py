import pygame, sys
from pygame.locals import *
from random import randint

ancho = 596
alto = 387

BLANCO = (255, 255, 255)


class Personaje(pygame.sprite.Sprite):
	defensor1 = pygame.image.load("hombrepre.bmp").convert()
	defensor1 = pygame.transform.scale(defensor1, (100, 100))
	defensor1.set_colorkey(BLANCO)


class Enemigo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	
		self.enemigo1 = pygame.image.load("jabalipre.bmp")
		self.enemigo1 = pygame.transform.scale(self.enemigo1, (700, 400))
		self.enemigo1.set_colorkey(BLANCO)
		
		self.rect = self.enemigo1.get_rect()
		self.rect.centerx = ancho/1
		self.rect.centery = alto-60
		
		self.velocidad = 10
		
		self.derecha = True
		self.contador = 0
		
	def dibujar(self, superficie):
		superficie.blit(self.enemigo1, self.rect)
			
	def comportamiento(self, tiempo):
		self.__movimientos()
			
	def __movimientos(self):
		if self.contador > 3:
			self.__movimientoLateral()
			
	def __movimientoLateral(self):
		if self.derecha = True:
			self.rect.left = self.rect.left + self.velocidad
			if self.rect.left > 500:
				self.derecha = False
				self.contador += 1
		else:
			self.rect.left = self.rect.left - self.velocidad
			if self.rect.left < 0:
				self.derecha = True


def Juego():
	pygame.init()
	pantalla = pygame.display.set_mode((ancho, alto))
	pygame.display.set_caption("Programacion 2")
	
	fondo1 = pygame.image.load("fondopre.png")
	
	jabali = Enemigo()
	
	reloj = pygame.time.Clock()
	
	while True:
		reloj.tick(60)
		
		for evento in pygame.event.get(): 
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
		
		pantalla.blit(fondo1, [0, 0])
		jabali.dibujar(pantalla)
		pygame.display.update()
Juego()		


