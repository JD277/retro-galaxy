# Importing lib
import pygame 
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Retro Galaxy")

running = True
class Interface:
    def __init__(self, img, x, y, title):
        self.text_content = title
        self.x_pos = x
        self.y_pos = y
        self.surface = pygame.image.load(img)
        self.RECT = pygame.Surface.get_rect(self.surface, topleft =(self.x_pos,self.y_pos))


    def draw(self):
        global screen
        screen.blit(self.surface, self.RECT)


travel = Interface("./src/backgrounds/travel-bg.jpeg", 0, 0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    travel.draw()
    
    pygame.display.update()

