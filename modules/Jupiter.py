from global_variables import *
from interface import Interface
import spaceinvader


class Jupiter:
    def __init__(self):

        bg_image_path = "../retro-galaxy/src/backgrounds/interfaz.jpg"
        game_icon_path = "../retro-galaxy/src/sprites/Jupiter/icono.jpg"
        x = 0
        y = 0
        title = "Space Invader"
        color_title = (255, 255, 255)
        color_text = (255, 255, 255)

        paragraph = [
            "Es un juego donde controlas una nave espacial",
            "para defenderte de oleadas de invasores alienígenas.",
            "Mueve tu nave lateralmente y dispara para destruir",
            "a los alienígenas antes de que lleguen a la base.",
            "Evita el contacto con los enemigos y ten cuidado con",
            "los obstáculos. A medida que avances y consigas puntos,",
            "la dificultad aumentará, haciendo que los invasores",
            "se muevan más rápido. ¡Buena suerte, piloto!"
        ]

        menu_icon = "../retro-galaxy/src/buttons/jupiter.png"

        self.spaceinvader = Interface(menu_icon, bg_image_path, game_icon_path, x, y, title, paragraph, color_title, color_text)


    def draw(self):
        if self.spaceinvader.gstate == True:
            spaceinvader.main_game()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] == True:
                self.spaceinvader.gstate = False

        elif self.spaceinvader.gstate == False:
            self.spaceinvader.draw()

jupiter = Jupiter()

