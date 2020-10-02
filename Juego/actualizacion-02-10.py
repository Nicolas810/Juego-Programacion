import pygame,sys
from pygame.locals import *
from random import randint

ancho = 596
alto = 387

BLANCO = (255, 255, 255)

lanza_list = pygame.sprite.Group()


class Enemigo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.enemigo1 = pygame.image.load("jabalipre.bmp")
		self.enemigo1 = pygame.transform.scale(self.enemigo1, (700, 400))
		self.enemigo1.set_colorkey(BLANCO)
		
		self.rect = self.enemigo1.get_rect()
		self.rect.topleft = (210, 150)

	def update(self):
		self.rect.move_ip(1, 0)
	
	def dibujar(self, superficie):
		superficie.blit(self.enemigo1, self.rect)
			
				
class Protagonista(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		pygame.sprite.Sprite.__init__(self)
		
		self.protagonista = pygame.image.load("hombrepre.bmp").convert()
		self.protagonista = pygame.transform.scale(self.protagonista, (130, 110))
		self.protagonista.set_colorkey(BLANCO)
		
		self.rect = self.protagonista.get_rect()
		self.rect.centerx = ancho/12
		self.rect.centery = alto-220
		
		self.listaDisparo = []
		
		
	def dibujar(self, superficie):
		superficie.blit(self.protagonista, self.rect)

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

class Lanza(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		pygame.sprite.Sprite.__init__(self)
		
		self.lanza = pygame.image.load("lanzapre.png").convert()
		self.lanza = pygame.transform.scale(self.lanza, (150, 70))
		self.lanza.set_colorkey(BLANCO)
		
		self.rect = self.lanza.get_rect()
		self.rect.centerx = ancho/4
		self.rect.centery = alto-250
		
	def update(self):
		self.rect.x += 5
		
	def dibujar(self, superficie):
		superficie.blit(self.lanza, self.rect)
		
	
def Juego():
	pygame.init()
	pantalla = pygame.display.set_mode((ancho, alto))
	pygame.display.set_caption("Juego")
	
	fondo1 = pygame.image.load("fondopre.png")
	jabali = Enemigo()
	cueva = Torre()
	cavernicola = Protagonista()
	lanza = Lanza()
	
	reloj = pygame.time.Clock()
	
	pygame.mouse.set_cursor(*pygame.cursors.diamond)
	
	while True:
		reloj.tick(60)
		
		for evento in pygame.event.get(): 
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			
			if evento.type == pygame.MOUSEBUTTONDOWN:
				lanza = Lanza()
				lanza.rect.x = cavernicola.rect.x + 45
				lanza.rect.y = cavernicola.rect.y -20
				
				lanza_list.add(lanza)
				
			if lanza.rect.x < -10:
				lanza_list.remove(lanza)
				
		
		pantalla.blit(fondo1, [0, 0])
		jabali.dibujar(pantalla)
		cueva.dibujar(pantalla)
		cavernicola.dibujar(pantalla)
		lanza.dibujar(pantalla)
		pygame.display.update()
Juego()		


