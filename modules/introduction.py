from global_variables import screen, running, pygame, Message
import menu_planetas

# Defining variables
counter = 0
condition = False
end = False
background = pygame.transform.scale(pygame.image.load('../retro-galaxy/src/backgrounds/intro-galaxy.png'),(1080,720))

class intro: 
    def __init__(self, x, y, img, xt, yt, title, size, scale, scale_x = 0, scale_y = 0):
        # Logo variables
        self.x = x
        self.y = y

        if scale == True:
            self.logo = pygame.transform.scale(pygame.image.load(img), (scale_x, scale_y))

        if scale == False:
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
        text_font = pygame.font.Font("../retro-galaxy/src/fonts/font1.otf", size)
        self.TEXT_SURF = text_font.render(text_content, False, (0,0,0))
        
        X_TEXT = pos_x
        Y_TEXT = pos_y
        self.TEXT_RECT = pygame.Surface.get_rect(self.TEXT_SURF, topleft =(X_TEXT,Y_TEXT))
        screen.blit(self.TEXT_SURF, self.TEXT_RECT)

    def draw(self):
        global screen
        screen.blit(self.logo, self.RECT)
        self.CREATE_TEXT(self.size,self.xt, self.yt, self.title)

    def rect_draw(self, color, width, heigth):

        self.rect = pygame.draw.rect(screen, color, pygame.Rect(self.xt,self.yt, width, heigth))

intro1 = intro(512, 260, "../retro-galaxy/src/sprites/Logo.png", 30, 30, 'UDO', 10, True, 600,500)
intro_load = intro(512, 480, "../retro-galaxy/src/sprites/rect.png", 213, 468, '', 10, False)
message1 = Message('Universidad de Oriente', 3, 1, "../retro-galaxy/src/fonts/font1.otf", 15, 'white',1)
message2 = Message('Departamento de Computacion y Sistemas', 3, 20, "../retro-galaxy/src/fonts/font1.otf", 15, 'white',1)
message3 = Message('Objetos y Abstraccion de datos', 3, 39, "../retro-galaxy/src/fonts/font1.otf", 15, 'white',1)
message4 = Message('Seccion  01', 3, 58, "../retro-galaxy/src/fonts/font1.otf", 15, 'white',1)

while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            condition = True
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background,(0,0))
    intro1.draw()
    intro_load.draw()
    message1.draw_text()
    message2.draw_text()
    message3.draw_text()
    message4.draw_text()
    intro_load.rect_draw('purple', 0 + counter, 24)

    if condition == True and end == False:
       counter += 1.5   
    
    if counter >= 598:
        end = True
        menu_planetas.main_menu()
    pygame.display.flip()
      
pygame.quit()   