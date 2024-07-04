import pygame
from global_variables import *
from interface import Interface
import car_race

class Saturno:
    def __init__(self):

        bg_image_path = "../retro-galaxy/src/backgrounds/saturno.jpg"
        game_icon_path = "../retro-galaxy/src/sprites/Car-race/car.png"
        x = 0
        y = 0
        title = "Car Race"
        color_title = (255, 255, 255)
        color_text = (255, 255, 255)

        paragraph = [
           "El jugador puede experimentar carreras en",
            "distintos paisajes, cada uno con diferentes",
            "dificultades. ¿Serás capaz de ganar en todas las pistas?",
        ]

        menu_icon = "../retro-galaxy/src/buttons/saturno.png"

        self.cars = Interface(menu_icon, bg_image_path, game_icon_path, x, y, title, paragraph, color_title, color_text)


    def draw(self):
        if self.cars.gstate == True:
            car_race.game.run()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] == True and car_race.fin == True:
                self.cars.gstate = False

        elif self.cars.gstate == False:
            self.cars.draw()

saturno = Saturno()

