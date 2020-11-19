import random
import pygame, sys, pygame.freetype
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Tower Defense')
dimensiones = (596, 387)
pantalla = pygame.display.set_mode(dimensiones)
fondo = pygame.image.load("fondomenu.jpg")
font = pygame.font.SysFont("Bahnschrift SemiLight SemiConde", 30)


def draw_text(text, font, color, surface, x, y):
    
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def menu_principal():
    while True:
 
        pantalla.blit(fondo, (0, 0))
        draw_text('Tower Defense', font, (255, 255, 255), pantalla, 230, 20)
        draw_text('Menu Principal', font, (255, 255, 255), pantalla, 50, 70)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(60, 100, 150, 50)
        button_2 = pygame.Rect(60, 155, 150, 50)
        button_3 = pygame.Rect(60, 210, 150, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                ayuda()
        if button_2.collidepoint((mx, my)):
            if click:
                niveles()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
		
        pygame.draw.rect(pantalla, (0, 0, 0), button_1)
        pygame.draw.rect(pantalla, (0, 0, 0), button_2)
        pygame.draw.rect(pantalla, (0, 0, 0), button_3)
        
        draw_text('Ayuda', font, (255, 255, 255), pantalla, 110, 115)
        draw_text('Niveles', font, (255, 255, 255), pantalla, 110, 170)
        draw_text('Salir', font, (255, 255, 255), pantalla, 110, 225)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def ayuda():
    running = True
    while running:
        pantalla.blit(fondo, (0, 0))
        
        mx, my = pygame.mouse.get_pos()
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        volver_1 = pygame.Rect(230, 250, 100, 40)
        if volver_1.collidepoint((mx, my)):
            if click:
                pygame.quit()
                volver()
        pygame.draw.rect(pantalla, (0, 0, 0), volver_1)       
        
        draw_text('Ayuda', font, (255, 255, 255), pantalla, 20, 20)
        draw_text('Bueno, en una explicacion rapida y sencilla este juego', font, (255, 255, 255), pantalla, 20, 70)
        draw_text('trata de un defensor que se ubica encima de una torre,', font, (255, 255, 255), pantalla, 20, 100)
        draw_text('tiene que defenderla hasta que pasen 5 enemigos, y si', font, (255, 255, 255), pantalla, 20, 130)
        draw_text('con el defensor logras que el enemigo no impacte 3 veces', font, (255, 255, 255), pantalla, 20, 160)
        draw_text('con la torre ganas.', font, (255, 255, 255), pantalla, 20, 190)
        draw_text('Volver', font, (255, 255, 255), pantalla, 250, 260)
        
        
        pygame.display.update()
        mainClock.tick(60)
 
def niveles():
    running = True
    while running:
        pantalla.blit(fondo, (0, 0))
 
        mx, my = pygame.mouse.get_pos()
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        nivel_1 = pygame.Rect(10, 60, 290, 50)
        nivel_2 = pygame.Rect(10, 140, 340, 50)
        nivel_3 = pygame.Rect(10, 220, 320, 50)
        nivel_4 = pygame.Rect(10, 300, 390, 50)
        volver_2 = pygame.Rect(480, 10, 100, 40)
        if nivel_1.collidepoint((mx, my)):
            if click:
                nivel1()
        if nivel_2.collidepoint((mx, my)):
            if click:
                nivel2()
        if nivel_3.collidepoint((mx, my)):
            if click:
                nivel3()
        if nivel_4.collidepoint((mx, my)):
            if click:
                nivel4()
        if volver_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                volver()        
        pygame.draw.rect(pantalla, (0, 0, 0), nivel_1)
        pygame.draw.rect(pantalla, (0, 0, 0), nivel_2)
        pygame.draw.rect(pantalla, (0, 0, 0), nivel_3)
        pygame.draw.rect(pantalla, (0, 0, 0), nivel_4)
        pygame.draw.rect(pantalla, (0, 0, 0), volver_2)
        
        draw_text('Niveles', font, (255, 255, 255), pantalla, 20, 20)
        draw_text('Nivel 1 - Prehistoria - Facil', font, (255, 255, 255), pantalla, 30, 80)
        draw_text('Nivel 2 - Edad Antigua - Medio', font, (255, 255, 255), pantalla, 30, 160)
        draw_text('Nivel 3 - Edad Media - Dificil', font, (255, 255, 255), pantalla, 30, 240)
        draw_text('Nivel 4 - Edad Moderna - Muy Dificil', font, (255, 255, 255), pantalla, 30, 320)
        draw_text('Volver', font, (255, 255, 255), pantalla, 500, 20)
                
                
        pygame.display.update()
        mainClock.tick(60)
        
def nivel1():
	from subprocess import check_output
	comando = "Nivel1.py"
	check_output(comando, shell=True)
	
def nivel2():
	from subprocess import check_output
	comando = "Nivel2.py"
	check_output(comando, shell=True)
	
def nivel3():
	from subprocess import check_output
	comando = "Nivel3.py"
	check_output(comando, shell=True)
	
def nivel4():
	from subprocess import check_output
	comando = "Nivel4.py"
	check_output(comando, shell=True)
	
def volver():
	from subprocess import check_output
	comando = "Menu.py"
	check_output(comando, shell=True)

        
menu_principal()
