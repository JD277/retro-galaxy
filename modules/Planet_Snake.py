
import pygame, sys
from pygame.locals import *
from game import *

color_fondo = (15,30,0)
color_fondo2 = (200,10,0)
alto = 720
ancho = 1080
pantalla = pygame.display.set_mode((ancho,alto))
op=1
on = False
menu_sound = pygame.mixer.Sound("../retro-galaxy/src/sounds/Planet_Snake/menu.mp3")
start_sound = pygame.mixer.Sound("../retro-galaxy/src/sounds/Planet_Snake/start.mp3")


pygame.init()
#Falta redimensionar

fuente = pygame.font.Font(None, 30)
IconoScreen = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/Logo.png')
Menu = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/Menu4.png')
Flechita = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/flechitachiquita.png')
texto1 = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/texto 1m.png')
texto2 = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/texto 2m.png')
texto3 = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/texto 3.png')
morada = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/Morada2.png')
amarila = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/amar2.png')
flechamov = 440
mov = 22
fondoIns = pygame.image.load('../retro-galaxy/src/backgrounds/PSnake/fondoIns.jpg')

def windowInit():
 pantalla.fill((0,0,0))
 pantalla.blit(Flechita,(315,flechamov,10, 30))
 pantalla.blit(Menu,(340,440))
 pantalla.blit(IconoScreen, (260,40,0,0))
 pygame.display.update()
 
def windowGame():
 main()
 
def windowOp():
 pantalla.fill((0,0,0))
 
 pantalla.blit(morada,(150,300))
 pantalla.blit(amarila,(140,380))

 pantalla.blit(texto1,(100,200))
 pantalla.blit(texto3,(200,320))
 pantalla.blit(texto2,(200,408))
 
 pygame.display.update()
 
def windowIns():
 pantalla.fill((150,20,100))
 pantalla.blit(fondoIns, (-45,0))
 pygame.display.update()
 
iniciar = True
finalizar = False

def game():
  global flechamov, mov, on, iniciar, finalizar

  windowInit()
  while iniciar: #pygame time loop
  
    for event in pygame.event.get():
      if event.type == QUIT:
          finalizar = True
          pygame.quit()
          sys.exit()
            

      if event.type == pygame.KEYDOWN:
            if event.key == K_UP and flechamov > 440 and on != True:
             flechamov = flechamov - mov
             pantalla.blit(Flechita,(400,flechamov,10, 30))
             menu_sound.play()                      
             windowInit()
            
            if event.key == K_DOWN and flechamov < 506 and on != True:
             flechamov = flechamov + mov
             pantalla.blit(Flechita,(400,flechamov,10, 30))
             menu_sound.play()
             windowInit()
            
            if event.key == K_x: 
             if flechamov == 440 :
              op=1 
              start_sound.play()  
              if on == False:
               windowGame()
               on =True
              else:
                windowInit()
                on=False
            
             if flechamov == 462:
              op=2 
              if on == False:
               windowOp()
               on =True
              else:
                windowInit()
                on=False
             if flechamov == 484:
              if on == False:
               windowIns()
               on =True
              else:
                windowInit()
                on=False
             if flechamov == 506:
               finalizar = True
               iniciar = False
               sys.exit()
             
             

                                    
             
    pygame.display.update()

