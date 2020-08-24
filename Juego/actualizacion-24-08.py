import pygame,sys
from pygame.locals import *
from random import randint

dimensiones = (596, 387)

class Enemigo(pygame.sprite.Sprite):
	def __init__(self, posx):
		pygame.sprite.Sprite.__init__(self)
		
		self.enemigo1 = pygame.imagen.load("jabalipre.bmp")
		self.enemigo1 = pygame.transform.scale(enemigo1, (700, 400))
		self.enemigo1.set_colorkey(BLANCO)
		
		self.listaImagenes = [self.enemigo1]
		self.posImagen = 0
		
		self.imagenEnemigo = self.listaImagenes[self.posImagen]
		self.rect = self.imagenEnemigo.get_rect()
		
		self.velocidad = 10
		self.rect.left = posx
		
		self.derecha = True
		self.contador = 0
		
	def comportamiento(self, tiempo):
		self.__movimientos()
			
	def __movimientos(self):
		if self.contador >3 :
			self.__movimientoLateral()
			
	def __movimientoLateral(self):
		if self.derecha == True:
			self.rect.left = self.rect.left + self.velocidad
			if self.rect.left > 500:
				self.derecha = False
				self.contador +=1
		else:
			self.rect.left = self.rect.left - self.velocidad
			if self.rect.left < 0:
				self.derecha = True

def Juego():
	pygame.init()
	pantalla = pygame.display.set_mode(dimensiones)
	pygame.display.set_caption("Programacion 2")
	
	fondo1 = pygame.image.load("fondopre.png")
	
	reloj = pygame.time.Clock()
	
	while True:
		reloj.tick(60)
		
		for evento in pygame.event.get(): 
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
		
			
		pantalla.blit(fondo1, [0, 0])
		pygame.display.update()
Juego()		


