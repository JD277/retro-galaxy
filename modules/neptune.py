from global_variables import *
from interface import Interface
from  Galactic_Travel import *

import Galactic_Travel as gt
class Neptune:
    def __init__(self):
    # ----------------------------Interface Variables-------------------------
        # Class arguments
        bg_image_path = "../retro-galaxy/src/backgrounds/travel-bg.jpeg"
        game_icon_path = "../retro-galaxy/src/sprites/navecita.png"
        x = 0
        y = 0
        title = "Galactic Travel"
        color_title = (255,255,255)
        color_text = (255,255,255)

        # Element to create the paragraph, because pygame does not support paragraphs
        paragraph = [
            "Travel  es  un  juego  basado  en  Flappy  bird",
            "el  cual  consiste  en  explorar  el  inhospito",
            "Neptuno  esquivando  los  asteroides  para",
            "cumplir  la  misión  de  crear  un  mapa  de  la",
            "Galaxia.  Suerte  soldado!!"
        ]
        menu_icon = "../retro-galaxy/src/buttons/neptuno.png"

        self.travel = Interface(menu_icon, bg_image_path, game_icon_path, x, y,title, paragraph, color_title, color_text)
    # ----------------------------Interface Variables-------------------------
    def draw(self):
        if self.travel.gstate == True:
            galactic_travel()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] == True and gt.game_over == True: 
                 self.travel.gstate = False
            if keys[pygame.K_SPACE] == True and gt.game_over == True:
                 new_game()

        elif self.travel.gstate == False:
            self.travel.draw()
            new_game()

neptune = Neptune()   
