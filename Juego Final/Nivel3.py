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
	
		self.image = pygame.image.load("caballomed.png").convert()
		self.image = pygame.transform.scale(self.image, (150, 100))
		self.image.set_colorkey(BLANCO)
		self.image.set_colorkey(NEGRO)
		
		self.rect = self.image.get_rect()
		self.rect.centerx = ancho/1
		self.rect.centery = alto-110
		
	def update(self):
		self.rect.move_ip(-20, 0)
			
class Protagonista(pygame.sprite.Sprite) :
	def __init__(self):
		super().__init__()
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load("caballeromed.png").convert()
		self.image = pygame.transform.scale(self.image, (90, 110))
		self.image.set_colorkey(BLANCO)
		self.image.set_colorkey(NEGRO)
		
		self.rect = self.image.get_rect()
		self.rect.centerx = ancho/9
		self.rect.centery = alto-220
		
	def dibujar(self, superficie):
		superficie.blit(self.image, self.rect)

class Torre(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load("castillomed.png").convert()
		self.image = pygame.transform.scale(self.image, (180, 250))
		self.image.set_colorkey(BLANCO)
		self.image.set_colorkey(NEGRO)
		
		self.rect = self.image.get_rect()
		self.rect.centerx = ancho/9
		self.rect.centery = alto-180
	
class Objeto(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load("flechamed.png").convert()
		self.image = pygame.transform.scale(self.image, (100, 60))
		self.image.set_colorkey(BLANCO)
		self.image.set_colorkey(NEGRO)
		
		self.rect = self.image.get_rect()
		self.rect.centerx = ancho/4
		self.rect.centery = alto-250
		
	def update(self):
		self.rect.x += 15
		self.rect.y += 15

pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego")

fondo1 = pygame.image.load("fondomed.jpg")
jabali = Enemigo()
cueva = Torre()
cavernicola = Protagonista()
lanza = Objeto()
gameover = pygame.image.load("gameover.bmp")
ganaste = pygame.image.load("ganaste.jpg")
	
jabali2 = Enemigo()
jabali3 = Enemigo()
jabali4 = Enemigo()
jabali5 = Enemigo()

listade_bloques = pygame.sprite.Group()
listade_todoslos_sprites = pygame.sprite.Group()
listade_lanzas = pygame.sprite.Group()

listade_bloques.add(jabali)
listade_bloques.add(jabali2)
listade_bloques.add(jabali3)
listade_bloques.add(jabali4)
listade_bloques.add(jabali5)
listade_todoslos_sprites.add(cueva)
listade_todoslos_sprites.add(jabali)
listade_todoslos_sprites.add(lanza)

pygame.mouse.set_cursor(*pygame.cursors.diamond)
	
reloj = pygame.time.Clock()

puntuacion = 0	
puntuacion1 = 0

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
	
	listade_todoslos_sprites.update()
	
	lista_impactos_lanza = pygame.sprite.spritecollide (lanza, listade_bloques, True)
	
	for h in lista_impactos_lanza:
		puntuacion1 += 1
		print ("Mataste", puntuacion1, "jabalies.")
	
	lista_impactos_bloques = pygame.sprite.spritecollide(cueva, listade_bloques, True)
		
	for i in lista_impactos_bloques:
		puntuacion += 1
		print ("El jabali golpeo", puntuacion, "veces a la torre.")
		
	if puntuacion == 0 and puntuacion1 == 1 or puntuacion == 1 and puntuacion1 == 0:
		listade_todoslos_sprites.add(jabali2)
		
	if puntuacion == 1 and puntuacion1 == 1 or puntuacion == 0 and puntuacion1 == 2 or puntuacion == 2 and puntuacion1 == 0:
		listade_todoslos_sprites.add(jabali3)
		
	if puntuacion == 1 and puntuacion1 == 2 or puntuacion == 2 and puntuacion1 == 1 or puntuacion == 0 and puntuacion1 == 3:
		listade_todoslos_sprites.add(jabali4)
	
	if puntuacion == 2 and puntuacion1 == 2 or puntuacion == 0 and puntuacion1 == 4 or puntuacion == 4 and puntuacion1 == 0 or puntuacion == 1 and puntuacion1 == 3:
		listade_todoslos_sprites.add(jabali5)
	
	pantalla.blit(fondo1, [0, 0])
	listade_todoslos_sprites.draw(pantalla)
	cavernicola.dibujar(pantalla)
	
	if puntuacion == 3:
		pantalla.blit(gameover, [0, 0])
		
	if puntuacion == 2 and puntuacion1 == 3 or puntuacion == 0 and puntuacion1 == 5 or puntuacion == 1 and puntuacion1 == 4:
		pantalla.blit(ganaste, [0, 0])
		
	pygame.display.update()

