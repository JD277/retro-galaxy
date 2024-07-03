from global_variables import *
from interface import Interface


class Mars:
    def __init__(self):
    # ----------------------------Interface Variables-------------------------
        # Class arguments
        bg_image_path = "../retro-galaxy/src/backgrounds/MBreaker/MarsB-bg.jpg"
        game_icon_path = "../retro-galaxy/src/sprites/Mars/MarsIcon.png"
        x = 0
        y = 0
        title = "Mars Breaker"
        color_title = (255,255,255)
        color_text = (255,255,255)

        # Element to create the paragraph, because pygame does not support paragraphs
        paragraph = [
            "Mars Breaker es un juego basado en Pong",
            "en en cual podrás enfrentarte a tus compañeros",
            "al estilo de ese mítico juego o buscar llegar lo",
            "más lejos posible destruyendo bloques de manera",
            "constante en el modo infinito, ahora en el planeta Marte"
        ]
        menu_icon = "../retro-galaxy/src/buttons/marte.png"

        self.Breaker = Interface(menu_icon, bg_image_path, game_icon_path, x, y,title, paragraph, color_title, color_text)
    # ----------------------------Interface Variables-------------------------
    def draw(self):
        if self.Breaker.gstate == True:
            M.juego()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] == True and M.finalizar == True:
                 self.Breaker.gstate = False

        elif self.Breaker.gstate == False:
            self.Breaker.draw()
            
    
mars = Mars()

