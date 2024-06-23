from global_variables import screen, running, pygame
from interface_example import Button_game 

class intro(): 
    def __init__(self, x, y, img, xt, yt, title, size):
        # Logo variables
        self.x = x
        self.y = y
        self.logo = pygame.image.load(img)
        self.RECT = pygame.Surface.get_rect(self.logo,center = (self.x, self.y))

        # Text label
        self.title = title
        self.xt = xt
        self.yt = yt
        self.click = False
        self.size = size


    def CREATE_TEXT (self, size, pos_x, pos_y, text):
        # text variables
        text_content = text
        text_font = pygame.font.Font("../retro-galaxy/src/fonts/font2.ttf", size)
        self.TEXT_SURF = text_font.render(text_content, True, "#000000")
        
        X_TEXT = pos_x
        Y_TEXT = pos_y
        self.TEXT_RECT = pygame.Surface.get_rect(self.TEXT_SURF, topleft =(X_TEXT,Y_TEXT))
        screen.blit(self.TEXT_SURF, self.TEXT_RECT)

    def draw(self):
        global screen
        screen.fill("#ffffff")
        screen.blit(self.logo, self.RECT)

intro1 = intro(512, 260, "../retro-galaxy/src/sprites/udo_logo.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    intro1.draw()
    
    pygame.display.update()   
pygame.quit()   
