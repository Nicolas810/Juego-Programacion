import pygame,sys
from pygame.locals import *

ancho = 596
alto = 387

BLANCO = (255, 255, 255)



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
		
		self.image = pygame.image.load("hombrepre.bmp").convert()
		self.image = pygame.transform.scale(self.image, (130, 110))
		self.image.set_colorkey(BLANCO)
		
		self.rect = self.image.get_rect()
		self.rect.centerx = ancho/12
		self.rect.centery = alto-220
		
	def dibujar(self, superficie):
		superficie.blit(self.image, self.rect)

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
		self.image.set_colorkey(BLANCO)
		
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

jabali2 = Enemigo()

listade_bloques = pygame.sprite.Group()
listade_todoslos_sprites = pygame.sprite.Group()
listade_lanzas = pygame.sprite.Group()
lista_jabalis = pygame.sprite.Group()

listade_bloques.add(jabali)
listade_bloques.add(jabali2)
listade_todoslos_sprites.add(cueva)
listade_todoslos_sprites.add(jabali)
listade_todoslos_sprites.add(lanza)
lista_jabalis.add(jabali2)

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
				lanza.rect.x = pos[0]
				lanza.rect.y = pos[1]
				
				listade_lanzas.add(lanza)
	
	listade_todoslos_sprites.update()
	lista_jabalis.update()
	
	lista_impactos_bloques = pygame.sprite.spritecollide(cueva, listade_bloques, True)
		
	for bloque in lista_impactos_bloques:
		puntuacion += 1
		print (puntuacion)
		lista_jabalis.draw(pantalla)
		
	pantalla.blit(fondo1, [0, 0])
	listade_todoslos_sprites.draw(pantalla)
	cavernicola.dibujar(pantalla)
	pygame.display.update()

 



