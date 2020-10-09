import pygame,sys
from pygame.locals import *

ancho = 596
alto = 387

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

class Enemigo(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load("jabalipre.bmp").convert()
		self.image = pygame.transform.scale(self.image, (190, 110))
		self.image.set_colorkey(BLANCO)
		
		self.rect = self.image.get_rect()
		self.rect.centerx = ancho/1
		self.rect.centery = alto-100
		
	def update(self):
		self.rect.move_ip(-1, 0)
			
class Protagonista(pygame.sprite.Sprite) :
	def __init__(self):
		super().__init__()
		pygame.sprite.Sprite.__init__(self)
		
		self.protago1 = pygame.image.load("hombrepre.bmp").convert()
		self.protago1 = pygame.transform.scale(self.protago1, (130, 110))
		self.protago1.set_colorkey(BLANCO)
		
		self.rect = self.protago1.get_rect()
		self.rect.centerx = ancho/12
		self.rect.centery = alto-220
		
	def dibujar(self, superficie):
		superficie.blit(self.protago1, self.rect)

class Torre(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load("torrepre.bmp").convert()
		self.image = pygame.transform.scale(self.image, (225, 140))
		self.image.set_colorkey(BLANCO)
		
		self.rect = self.image.get_rect()
		self.rect.centerx = ancho/6
		self.rect.centery = alto-100
	
class Objeto(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load("lanzapre.png").convert()
		self.image = pygame.transform.scale(self.image, (150, 70))
		self.image.set_colorkey(NEGRO)
		
		self.rect = self.image.get_rect()
		self.rect.centerx = ancho/4
		self.rect.centery = alto-250
		
	def update(self):
		self.rect.x += 3
		self.rect.y += 3

pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego")
	
fondo1 = pygame.image.load("fondopre.png")
jabali = Enemigo()
cueva = Torre()
cavernicola = Protagonista()
lanza = Objeto()
	
listade_bloques = pygame.sprite.Group()
listade_todoslos_sprites = pygame.sprite.Group()
listade_lanzas = pygame.sprite.Group()
listade_jabalis = pygame.sprite.Group()

listade_bloques.add(jabali)
listade_todoslos_sprites.add(cueva)
listade_todoslos_sprites.add(jabali)
listade_todoslos_sprites.add(lanza)

pygame.mouse.set_cursor(*pygame.cursors.diamond)
	
reloj = pygame.time.Clock()

puntuacion = 0	
while 1:
	reloj.tick(60)
		
	for evento in pygame.event.get(): 
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
			
		if evento.type == pygame.MOUSEBUTTONDOWN:
			lanza.rect.x = cavernicola.rect.x + 45
			lanza.rect.y = cavernicola.rect.y -20
				
			listade_lanzas.add(lanza)
				
		
	if  pygame.sprite.spritecollide(cueva, listade_bloques, True):
		puntuacion += 1
		print (puntuacion)
		
		jabali.rect.x = jabali.rect.centerx = ancho/1
		jabali.rect.y = jabali.rect.centery = alto-100
		
		listade_jabalis.add(jabali)
						
	
	listade_todoslos_sprites.update()
	
	pantalla.blit(fondo1, [0, 0])
	listade_todoslos_sprites.draw(pantalla)
	cavernicola.dibujar(pantalla)
	pygame.display.update()

 



