from global_variables import Message
import pygame
import sys
import neptune
import uranus
import earth
import Mercury
import mars
import pluto
import Jupiter

pygame.init()
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.display.set_caption('Menu')
screen = pygame.display.set_mode((1080, 720), 0, 32)
fondo = pygame.image.load("../retro-galaxy/src/sprites/Menu/fondo.jpg")
fondo = pygame.transform.scale(fondo, (1080, 720))
text_box = pygame.image.load("../retro-galaxy/src/sprites/Menu/dialogue_box1.png")
font = pygame.font.SysFont('Arial', 60)
mouse = pygame.mouse.get_cursor()
hover = False



nmusic = pygame.mixer.Sound("../retro-galaxy/src/sounds/neptune.mp3")


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    global click, hover, text_box
    while True:

        screen.blit(fondo, (0, 0))

        message = "RETRO GALAXY"
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

        text_box_rect = text_box.get_rect()
        text_box_rect.center = (540,300)
        button_1 = mercurio.get_rect()
        button_1.center = (170, 280)
        button_2 = venus.get_rect()
        button_2.center = (320, 150)
        button_3 = tierra.get_rect()
        button_3.center = (530, 90)
        button_4 = marte.get_rect()
        button_4.center = (730, 150)
        button_5 = jupiter.get_rect()
        button_5.center = (890, 280)
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
                Mercury.mercurio.dino.mstate = False
            if hover:
                mercurio = pygame.image.load('../retro-galaxy/src/sprites/Menu/mercuriotriste.png')
                mercurio = pygame.transform.scale(mercurio, (150, 150))
                message = "Mercurio (Dino Run)"

        if button_2.collidepoint((mx, my)):
            if click:
                planet2()
            if hover:
                venus = pygame.image.load('../retro-galaxy/src/sprites/Menu/venusglow.png')
                venus = pygame.transform.scale(venus, (150, 150))
                message = "Venus ()"
        if button_3.collidepoint((mx, my)):
            if click:
                planet3()
                earth.earth.buscaminas.mstate = False
            if hover:
                tierra = pygame.image.load('../retro-galaxy/src/sprites/Menu/tierraglow.png')
                tierra = pygame.transform.scale(tierra, (150, 150))
                message = "Tierra (Buscaminas)"
        if button_4.collidepoint((mx, my)):
            if click:
                planet4()
                mars.mars.Breaker.mstate = False
            if hover:
                marte = pygame.image.load('../retro-galaxy/src/sprites/Menu/marteglow.png')
                marte = pygame.transform.scale(marte, (150, 150))
                message = "Marte (Mars Breaker)"
        if button_5.collidepoint((mx, my)):
            if click:
                planet5()
                Jupiter.jupiter.spaceinvader.mstate = False
            if hover:
                jupiter = pygame.image.load('../retro-galaxy/src/sprites/Menu/jupiterglow.png')
                jupiter = pygame.transform.scale(jupiter, (150, 150))
                message = "Jupiter (Space Invader)"
        if button_6.collidepoint((mx, my)):
            if click:
                planet6()
            if hover:
                saturno = pygame.image.load('../retro-galaxy/src/sprites/Menu/saturnoglow.png')
                saturno = pygame.transform.scale(saturno, (170, 150))
                message = "Saturno ()"
        if button_7.collidepoint((mx, my)):
            if click:
                planet7()
                uranus.urano.asteroids.mstate = False
            if hover:
                urano = pygame.image.load('../retro-galaxy/src/sprites/Menu/Uranoglow.png')
                urano = pygame.transform.scale(urano, (150, 150))
                message = "Urano (Asteroids)"
        if button_8.collidepoint((mx, my)):
            if click:
                planet8()
                neptune.neptune.travel.mstate = False
            if hover:
                neptuno = pygame.image.load('../retro-galaxy/src/sprites/Menu/neptunoglow.png')
                neptuno = pygame.transform.scale(neptuno, (150, 150))
                message = "Neptuno (Galactic Travel)"
        if button_9.collidepoint((mx, my)):
            if click:
                planet9()
                pluto.pluton.snake.mstate = False
            if hover:
                pluton = pygame.image.load('../retro-galaxy/src/sprites/Menu/plutonglow.png')
                pluton = pygame.transform.scale(pluton, (150, 150))
                message = "Pluton (Snake)"

        screen.blit(text_box,text_box_rect)
        screen.blit(mercurio, button_1)
        screen.blit(venus, button_2)
        screen.blit(tierra, button_3)
        screen.blit(marte, button_4)
        screen.blit(jupiter, button_5)
        screen.blit(saturno, button_6)
        screen.blit(urano, button_7)
        screen.blit(neptuno, button_8)
        screen.blit(pluton, button_9)

        main_text = Message(message, 540, 300,'../retro-galaxy/src/fonts/font1.otf',30, "white",0)
        main_text.draw_text()

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
            if event.type == MOUSEMOTION:
                hover = True

        pygame.display.update()
        mainClock.tick(60)


def planet1():
    global click
    running = True
    while running:
        
        Mercury.mercurio.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if Mercury.mercurio.dino.mstate == True:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def planet2():
    global click
    running = True
    while running:
        screen.fill((0, 0, 0))

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

        earth.earth.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if earth.earth.buscaminas.mstate == True:
                running = False

        pygame.display.update()
        mainClock.tick(60)


def planet4():
    global click
    running = True
    while running:

        mars.mars.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if mars.mars.Breaker.mstate == True:
                running = False

        pygame.display.update()
        mainClock.tick(60)


def planet5():
    global click
    running = True
    while running:
        
        Jupiter.jupiter.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if Jupiter.jupiter.spaceinvader.mstate == True:
                running = False

        pygame.display.update()
        mainClock.tick(60)


def planet6():
    global click
    global click
    running = True
    while running:
        screen.fill((0, 0, 0))

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
        screen.fill((0, 0, 0))

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

        pluto.pluton.draw()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if pluto.pluton.snake.mstate == True:
                running = False

        pygame.display.update()
        mainClock.tick(60)