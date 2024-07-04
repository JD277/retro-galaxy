from global_variables import *
from interface import Interface
import Buscaminas
class Earth:
    def __init__(self):
    # ----------------------------Interface Variables-------------------------
        # Class arguments
        bg_image_path = "../retro-galaxy/src/backgrounds/buscaminas/interfaz.png"
        game_icon_path = "../retro-galaxy/src/buttons/bomb.png"
        x = 0
        y = 0
        title = "Buscaminas"
        color_title = (255,255,255)
        color_text = (255,255,255)

        # Element to create the paragraph, because pygame does not support paragraphs
        paragraph = [
            "Buscaminas  es  un  popular  videojuego  arcade",
            "consiste  en  despejar  todas  las  casillas  de  una  pantalla",
            "que  no  oculten  una mina.  Algunas  casillas  tienen  ",
            "un  número,  este número  indica  las minas que estan ",
            "en todas las  casillas  circundantes.",
            "Suerte  desarmando  minas!!!"

            
        ]
        menu_icon = "../retro-galaxy/src/buttons/tierra.png"

        self.buscaminas = Interface(menu_icon, bg_image_path, game_icon_path, x, y,title, paragraph, color_title, color_text)
        self.buscaminas.game_btn.BTN_RECT.x = self.buscaminas.game_btn.BTN_RECT.x - 40
        self.buscaminas.game_btn.xt = self.buscaminas.game_btn.xt - 40
    # ----------------------------Interface Variables-------------------------
    def draw(self):
        if self.buscaminas.gstate == True:
            screen.fill("#000000")
            Buscaminas.main()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] == True: 
                 self.buscaminas.gstate = False

        elif self.buscaminas.gstate == False:

            self.buscaminas.draw()

earth = Earth()

