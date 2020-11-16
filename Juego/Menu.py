
import pygame, sys, pygame.freetype
 

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Tower Defense')
dimensiones = (920, 512)
screen = pygame.display.set_mode(dimensiones)

font = pygame.font.SysFont("Bahnschrift SemiLight SemiConde", 30)

def draw_text(text, font, color, surface, x, y):
    
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def menu_principal():
    while True:
 
        screen.fill((0, 0, 0))
        """screen.blit(fondo, (0, 0))"""
        draw_text('Tower Defense', font, (255, 255, 255), screen, 400, 20)
        draw_text('Menu Principal', font, (255, 255, 255), screen, 50, 50)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 150, 50)
        button_2 = pygame.Rect(50, 155, 150, 50)
        button_3 = pygame.Rect(30, 250, 150, 30)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                niveles()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
		
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        pygame.draw.rect(screen, (0, 0, 0), button_3)
        
        draw_text('Jugar', font, (255, 255, 255), screen, 110, 120)
        draw_text('Niveles', font, (255, 255, 255), screen, 110, 170)
        draw_text('Salir', font, (255, 255, 255), screen, 110, 220)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def jugar():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('Jugar', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def niveles():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Niveles', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
        
def salir():
	import sys
	sys.exit(0)
	      
if __name__ == '__main__':
    
    salir = False
    opciones = [
        ("Jugar", jugar),
        ("Niveles", niveles),
        ("Salir", salir)
        ]

    pygame.font.init()
    screen = pygame.display.set_mode((320, 240))
    fondo = pygame.image.load("fondomenu.jpg").convert()
    menu_principal = Menu(niveles)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)

 
menu_principal()
