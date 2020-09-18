import pygame,sys
from pygame.locals import *
from random import randint

ancho = 596
alto = 387

BLANCO = (255, 255, 255)


class Enemigo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.enemigo1 = pygame.image.load("jabalipre.bmp")
		self.enemigo1 = pygame.transform.scale(self.enemigo1, (150, 130))
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
				
class Protagonista(pygame.sprite.Sprite) :
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.protago1 = pygame.image.load("hombrepre.bmp").convert()
		self.protago1 = pygame.transform.scale(self.protago1, (130, 110))
		self.protago1.set_colorkey(BLANCO)
		
		self.rect = self.protago1.get_rect()
		self.rect.centerx = ancho/12
		self.rect.centery = alto-220
		
		self.listaDisparo = []
		
	def disparar(self, x, y):
		miProyectil = Proyectil(x,y)
		self.listaDisparo.append(miProyectil)
		
	def dibujar(self, superficie):
		superficie.blit(self.protago1, self.rect)

class Lanza(pygame.sprite.Sprite):
	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)
		
		self.imageLanza = pygame.image.load("lanzapre.png").convert()
		self.rect = self.imageLanza.get_rect()
		
		self.velocidadDisparo = 5
		self.rect.top = posy
		self.rect.left = posx
		
	def trayectoria(self):
		self.rect.top = self.rect.top - self.velocidadDisparo
	
	def dibujar(self):
		superficie.blit(self.imageProyectil, self.rect)
		

class Torre(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.torre1 = pygame.image.load("torrepre.bmp").convert()
		self.torre1 = pygame.transform.scale(self.torre1, (225, 140))
		self.torre1.set_colorkey(BLANCO)
		
		self.rect = self.torre1.get_rect()
		self.rect.centerx = ancho/6
		self.rect.centery = alto-100
		
	def dibujar(self, superficie):
		superficie.blit(self.torre1, self.rect)
		
contador = 0
print(contador)
def contador(self):
	if enemigo.colliderect(torre1):
		self.contador += 1
		
def Juego():
	pygame.init()
	pantalla = pygame.display.set_mode((ancho, alto))
	pygame.display.set_caption("Programacion 2")
	
	fondo1 = pygame.image.load("fondopre.png")
	jabali = Enemigo()
	cueva = Torre()
	cavernicola = Protagonista()
	
	reloj = pygame.time.Clock()
	
	while True:
		reloj.tick(60)
		
		for evento in pygame.event.get(): 
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
		
		pantalla.blit(fondo1, [0, 0])
		jabali.dibujar(pantalla)
		cueva.dibujar(pantalla)
		cavernicola.dibujar(pantalla)
		pygame.display.update()
Juego()		


