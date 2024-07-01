import pygame
import sys 
import neptune
import uranus

pygame.init()
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.display.set_caption('Menu')
screen = pygame.display.set_mode((1080, 720),0,32)
fondo = pygame.image.load("../retro-galaxy/src/sprites/Menu/fondo.jpg")
fondo = pygame.transform.scale(fondo, (1080, 720))
font = pygame.font.SysFont('Arial', 60)

nmusic = pygame.mixer.Sound("../retro-galaxy/src/sounds/neptune.mp3")


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    global click
    while True:
 
        screen.blit(fondo, (0,0))

        mercurio = pygame.image.load('../retro-galaxy/src/sprites/Menu/mercurio.png')
        mercurio = pygame.transform.scale(mercurio, (150, 150))
        venus = pygame.image.load('../retro-galaxy/src/sprites/Menu/venus.png')
        venus = pygame.transform.scale(venus, (150, 150))
        tierra = pygame.image.load('../retro-galaxy/src/sprites/Menu/tierra.png')
        tierra = pygame.transform.scale(tierra, (150, 150))
        marte = pygame.image.load('../retro-galaxy/src/sprites/Menu/marte.png')
        marte = pygame.transform.scale(marte, (150, 150))
        jupiter = pygame.image.load('../retro-galaxy/src/sprites/Menu/jupiter.png')
        jupiter = pygame.transform.scale(jupiter, (150, 150))
        saturno = pygame.image.load('../retro-galaxy/src/sprites/Menu/saturno.png')
        saturno = pygame.transform.scale(saturno, (170, 150))
        urano = pygame.image.load('../retro-galaxy/src/sprites/Menu/Urano.png')
        urano = pygame.transform.scale(urano, (150, 150))
        neptuno = pygame.image.load('../retro-galaxy/src/sprites/Menu/neptuno.png')
        neptuno = pygame.transform.scale(neptuno, (150, 150))
        pluton = pygame.image.load('../retro-galaxy/src/sprites/Menu/pluton.png')
        pluton = pygame.transform.scale(pluton, (150, 150))

        mx, my = pygame.mouse.get_pos()
        
        button_1 = mercurio.get_rect()
        button_1.center = (200, 280)
        button_2 = venus.get_rect()
        button_2.center = (320, 150)
        button_3 = tierra.get_rect()
        button_3.center = (530, 90)
        button_4 = marte.get_rect()
        button_4.center = (730, 150)
        button_5 = jupiter.get_rect()
        button_5.center = (850, 280)
        button_6 = saturno.get_rect()
        button_6.center = (800, 450)
        button_7 = urano.get_rect()
        button_7.center = (430, 560)
        button_8 = neptuno.get_rect()
        button_8.center = (620, 560)
        button_9 = pluton.get_rect()
        button_9.center = (280, 450)
        
        if button_1.collidepoint((mx, my)):
            if click:
                planet1()
        if button_2.collidepoint((mx, my)):
            if click:
                planet2()
        if button_3.collidepoint((mx, my)):
            if click:
                planet3()
        if button_4.collidepoint((mx, my)):
            if click:
                planet4()
        if button_5.collidepoint((mx, my)):
            if click:
                planet5()
        if button_6.collidepoint((mx, my)):
            if click:
                planet6()
        if button_7.collidepoint((mx, my)):
            if click:
                planet7()
                uranus.urano.asteroids.mstate = False

        if button_8.collidepoint((mx, my)):
            if click:
                planet8()
                neptune.neptune.travel.mstate = False
        if button_9.collidepoint((mx, my)):
            if click:
                planet9()
       
        screen.blit(mercurio, button_1)
        screen.blit(venus, button_2)
        screen.blit(tierra, button_3)
        screen.blit(marte, button_4)
        screen.blit(jupiter, button_5)
        screen.blit(saturno, button_6)
        screen.blit(urano, button_7)
        screen.blit(neptuno, button_8)
        screen.blit(pluton, button_9)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def planet1():
    global click
    running = True
    while running:
        screen.fill((0, 0, 0))
        
        draw_text('Mercurio', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def planet2():
    global click
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Venus', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet3():
    global click
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Tierra', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet4():
    global click
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Marte', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet5():
    global click
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Jupiter', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet6():
    global click
    global click
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Saturno', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet7():
    global click
    running = True
    while running:
        screen.fill((0,0,0))

        uranus.urano.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if uranus.urano.asteroids.mstate == True:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet8():
    global nmusic, click
    running = True
    while running:
        neptune.neptune.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if neptune.neptune.travel.mstate == True:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet9():
    global click
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Pluton', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
