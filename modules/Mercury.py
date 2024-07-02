from global_variables import *
from interface import Interface
import Dino


class Mercurio:
    def __init__(self):

        bg_image_path = "../retro-galaxy/src/backgrounds/dino-bg.jpg"
        game_icon_path = "../retro-galaxy/src/sprites/mercurio/dino.png"
        x = 0
        y = 0
        title = "Dino Run"
        color_title = (255, 255, 255)
        color_text = (255, 255, 255)

        paragraph = [
            "En  este  juego,  los  jugadores  controlan  a  un",
            "dinosaurio  que  debe  correr,  saltar  y  esquivar",
            "obstaculos  para  evitar  la  extincion,  huyendo  de",
            "meteoritos  voladores  entre  otros  desafios.  El",
            "juego  no  tiene  niveles  fijos,  por  lo  que  el  jugador",
            "debe  adaptarse  a  las  plataformas  y  obstaculos",
            "que  se  generan  en  tiempo  real."

        ]

        menu_icon = "../retro-galaxy/src/sprites/mercurio/mercurio.png"

        self.dino = Interface(menu_icon, bg_image_path, game_icon_path, x, y, title, paragraph, color_title, color_text)


    def draw(self):
        if self.dino.gstate == True:
            Dino.main()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] == True:
                self.dino.gstate = False

        elif self.dino.gstate == False:
            self.dino.draw()

mercurio = Mercurio()


