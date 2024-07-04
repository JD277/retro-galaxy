from global_variables import *
from interface import Interface
from Planet_Snake import *
import Planet_Snake as ps

class Pluto:
    def __init__(self):
    # ----------------------------Interface Variables-------------------------
        # Class arguments
        bg_image_path = "../retro-galaxy/src/backgrounds/PSnake/plutonBg.jpeg"
        game_icon_path = "../retro-galaxy/src/sprites//Planet_Snake/img/Logo.png"
        x = 0
        y = 0
        title = "Planet Snake"
        color_title = (255,255,255)
        color_text = (255,255,255)

        # Element to create the paragraph, because pygame does not support paragraphs
        paragraph = [
            "Planet Snake es un juego basado en el clásico Snake.",
            "Controlas a una serpiente abrienta que se desliza por",
            "las vastas llanuras heladas de Plutón.", 
            "Tu misión es guiar a la serpiente a través de este", 
            "mundo congelado, recolectando",
            "manzanas para alimentar tu energía.",
            

            
        ]
        menu_icon = "../retro-galaxy/src/buttons/pluton.png"

        self.snake = Interface(menu_icon, bg_image_path, game_icon_path, x, y,title, paragraph, color_title, color_text)
    # ----------------------------Interface Variables-------------------------
    def draw(self):
        if self.snake.gstate == True:
            ps.game()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] == True and ps.finalizar == True : 
                 self.ps.gstate = False

        elif self.snake.gstate == False:
            self.snake.draw()

pluton = Pluto()

