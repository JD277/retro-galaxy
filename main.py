# Importing lib
import pygame 
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Retro Galaxy")
pygame.init()
running = True
class Interface:
    # Define the constructor function for the class
    def __init__(self, img, x, y, title, description =["Lorem ipsum"], color1 =(255,255,255), color2=(255,255,255)):
        # Text variables
        self.color1 = color1
        self.color2 = color2
        self.title = title
        self.des = description
        #Bg variables
        self.X_POS = x
        self.Y_POS = y
        self.bg_surf = pygame.image.load(img)
        self.BG_RECT = pygame.Surface.get_rect(self.bg_surf, topleft =(self.X_POS,self.Y_POS))

    # Function to create dynamic text
    def CREATE_TEXT (self, size, pos_x, pos_y, text, bold=0,):
        # text variables
        text_content = text
        if bold == 1:
            text_font = pygame.font.Font("src/fonts/font1.otf", size)
            self.TEXT_SURF = text_font.render(text_content, True, self.color1)

        elif bold == 0:
            text_font = pygame.font.Font("src/fonts/font2.ttf", size)
            self.TEXT_SURF = text_font.render(text_content, True, self.color2)
        
        X_TEXT = pos_x
        Y_TEXT = pos_y
        self.TEXT_RECT = pygame.Surface.get_rect(self.TEXT_SURF, topleft =(X_TEXT,Y_TEXT))
        screen.blit(self.TEXT_SURF, self.TEXT_RECT)
    
    # Draw the interface
    def draw(self):
        global screen
        screen.blit(self.bg_surf, self.BG_RECT)
        self.CREATE_TEXT(50,50,200, self.title,1)
        value = 300
        for text in self.des:
            self.CREATE_TEXT(20,50,value, text,1)
            value += 25


# Element to create the paragraph, because pygame does not support paragraphs
paragraph = [
    "Travel  es  un  juego  basado  en  Flappy  bird",
    "el  cual  consiste  en  exolorar  el  inospito",
    "Neptuno  esquivando  los  asteroides  para",
    "Cumplir  la misión  de  crear  un  mapa  de  la",
    "Galaxia.  Suerte  soldado!!"
]
# Making the instance for the class interface (image path, posx, posy, Name of the game, paragraph) 
travel = Interface("./src/backgrounds/travel-bg.jpeg", 0, 0,"Travel", paragraph)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    travel.draw()
    
    pygame.display.update()

