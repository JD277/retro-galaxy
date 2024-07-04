from global_variables import *
from interface import Interface
import pygame, math, copy
from pygame.locals import *

class Venus:
    def __init__(self):

        bg_image_path = "../retro-galaxy/src/backgrounds/venus-bg.jpg"
        game_icon_path = "../retro-galaxy/src/sprites/pacman.png"
        x = 0
        y = 0
        title = "Pac-Man"
        color_title = (255, 255, 255)
        color_text = (255, 255, 255)

        paragraph = [
            'Es uno de los juegos más populares y reconocibles de',
            'la historia de los videojuegos. En Pac-Man, el jugador',
            'controla a un personaje amarillo en forma de boca,',
            'Pac-Man, que se mueve a través de un laberinto comiendo',
            'puntos y evitando a cuatro fantasmas de colores',
            'El objetivo principal del juego es comer todos los puntos',
            '(pequeños círculos) que se encuentran en el laberinto,',
            'mientras se evita ser atrapado por los fantasmas. ',
            'Si Pac-Man es tocado por un fantasma, pierde una vida.',

        ]

        menu_icon = "../retro-galaxy/src/buttons/venus.png"

        self.dino = Interface(menu_icon, bg_image_path, game_icon_path, x, y, title, paragraph, color_title, color_text)


    def draw(self):
        if self.dino.gstate == True:

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] == True:
                self.dino.gstate = False

        elif self.dino.gstate == False:
            self.dino.draw()

venus = Venus()
