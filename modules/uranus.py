from global_variables import *
from interface import Interface
from asteroids import *
import asteroids
class Uranus:
    def __init__(self):
    # ----------------------------Interface Variables-------------------------
        # Class arguments
        bg_image_path = "../retro-galaxy/src/backgrounds/bg-asteroid-2.jpg"
        game_icon_path = "../retro-galaxy/src/buttons/asteroide.png"
        x = 0
        y = 0
        title = "Asteroids"
        color_title = (255,255,255)
        color_text = (255,255,255)

        # Element to create the paragraph, because pygame does not support paragraphs
        paragraph = [
            "Asteroids  es  un  popular  videojuego  arcade",
            "basado  en  vectores  lanzado  en  1979  por  Atari.",
            "El  objetivo  del  juego  es  disparar  y  destruir",
            "evitando  chocar  contra  los  fragmentos  que  se ",
            "desprenden  de  estos.  Suerte  surcando  la  galaxia!!!"

            
        ]
        menu_icon = "../retro-galaxy/src/buttons/urano.png"

        self.asteroids = Interface(menu_icon, bg_image_path, game_icon_path, x, y,title, paragraph, color_title, color_text)
    # ----------------------------Interface Variables-------------------------
    def draw(self):
        if self.asteroids.gstate == True:
            asteroids.asteroids()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] == True and asteroids.finalizar == True : 
                 self.asteroids.gstate = False

        elif self.asteroids.gstate == False:
            self.asteroids.draw()

urano = Uranus()    