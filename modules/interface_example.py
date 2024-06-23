# Importing lib
from global_variables import screen, running, pygame
class Button_game:
    def __init__(self,img, title="lorem   ipsum", x=0, y=0, xt=0, yt=0, color1 =(255,255,255), color2=(255,255,255), size=16):
        # Button label
        self.color1 = color1
        self.color2 = color2
        self.title = title
        self.xt = xt
        self.yt = yt
        self.click = False
        self.size = size

        self.X_POS = x
        self.Y_POS = y
        self.btn_surf = pygame.image.load(img)
        self.BTN_RECT = pygame.Surface.get_rect(self.btn_surf, topleft =(self.X_POS,self.Y_POS))
    # Function to create dynamic text
    def CREATE_TEXT (self, size, pos_x, pos_y, text, bold=0,):
        # text variables
        text_content = text
        if bold == 1:
            text_font = pygame.font.Font("../retro-galaxy/src/fonts/font1.otf", size)
            self.TEXT_SURF = text_font.render(text_content, True, self.color1)

        elif bold == 0:
            text_font = pygame.font.Font("../retro-galaxy/src/fonts/font2.ttf", size)
            self.TEXT_SURF = text_font.render(text_content, True, self.color2)
        
        X_TEXT = pos_x
        Y_TEXT = pos_y
        self.TEXT_RECT = pygame.Surface.get_rect(self.TEXT_SURF, topleft =(X_TEXT,Y_TEXT))
        screen.blit(self.TEXT_SURF, self.TEXT_RECT)
    
    def btn_is_press(self):
        self.mouse = pygame.mouse.get_pressed(num_buttons=3)
        self.click = False
        if self.BTN_RECT.collidepoint(pygame.mouse.get_pos()) and self.mouse[0]:
            self.click = True
        else:
            self.click = False

    def draw(self):
        global screen
        screen.blit(self.btn_surf, self.BTN_RECT)
        if self.title != " " or self.title != "lorem  ipsum":
          self.CREATE_TEXT(self.size,self.xt, self.yt, self.title, 1)



        
class Interface:
    # Define the constructor function for the class
    def __init__(self, micon, img, img_icon, x, y, title, description =["Lorem ipsum"], color1 =(255,255,255), color2=(255,255,255), wimg="../retro-galaxy/src/buttons/warning-btn.png", wicon="../retro-galaxy/src/buttons/clock-icon.png"):
        
        # btn stuff
        self.btn = []
        btn_margin = 50
        self.btn_num = 5
        for i in range (self.btn_num):
            self.btn.append(Button_game("../retro-galaxy/src/buttons/btn-white-m.png",x = btn_margin, y = 550))
            btn_margin += 200


        # Game icon
        X_POSGI = 600
        Y_POSGI = 150
        self.gicon_surf = pygame.image.load(img_icon)
        self.GI_RECT = pygame.Surface.get_rect(self.gicon_surf, topleft =(X_POSGI,Y_POSGI))


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


        # Warning window vaiables
        self.wimg = pygame.image.load(wimg).convert_alpha()
        self.WRECT = pygame.Surface.get_rect(self.wimg,center = (540,360))
        self.wicon =pygame.image.load(wicon).convert_alpha()
        self.wirect = pygame.Surface.get_rect(self.wicon,center = (540,330))
        self.wclose = Button_game("../retro-galaxy/src/buttons/cancel.png","",890,220)
        self.wstate = False
        
        # Menu btn
        self.menu_icon = micon
        self.menu_btn = Button_game(self.menu_icon,"Menu",994,30,1004,94)
        self.mstate = False

        # Game btn
        self.game_btn = Button_game("../retro-galaxy/src/buttons/btn.png","Start",770,440,790,445,size= 25)
        self.gstate = False

    # Function to create dynamic text
    def CREATE_TEXT (self, size, pos_x, pos_y, text, bold=0,):
        # text variables
        text_content = text
        if bold == 1:
            text_font = pygame.font.Font("../retro-galaxy/src/fonts/font1.otf", size)
            self.TEXT_SURF = text_font.render(text_content, True, self.color1)

        elif bold == 0:
            text_font = pygame.font.Font("../retro-galaxy/src/fonts/font2.ttf", size)
            self.TEXT_SURF = text_font.render(text_content, True, self.color2)
        
        X_TEXT = pos_x
        Y_TEXT = pos_y
        self.TEXT_RECT = pygame.Surface.get_rect(self.TEXT_SURF, topleft =(X_TEXT,Y_TEXT))
        screen.blit(self.TEXT_SURF, self.TEXT_RECT)
    
    
    # Click event for soon btns
    def soon (self):
        for j in range(self.btn_num):
            self.btn[j].btn_is_press()
            if self.btn[j].click:
                self.wstate = True
            
            
    # Warning window
    def window (self):
        global screen
        screen.blit(self.wimg,self.WRECT)
        self.CREATE_TEXT(20,210,400,"Estamos  creando  más  juegos,  esta  atento a  las  actualizaciones :)",1)
        screen.blit(self.wicon,self.wirect)
        self.wclose.draw()

    def wclose_warning(self):
        self.wclose.btn_is_press()  
        if self.wclose.click:
            self.wstate = False

    def back_menu(self):
        self.menu_btn.btn_is_press()  
        if self.menu_btn.click:
            self.mstate = True

    def start_game(self):
        self.game_btn.btn_is_press()  
        if self.game_btn.click:
            self.gstate = True

    # Draw the interface
    def draw(self):
        global screen
        self.soon()
        # Normal Interface 
        if  self.wstate == False and self.mstate == False and self.gstate == False:
            screen.blit(self.bg_surf, self.BG_RECT)
            screen.blit(self.gicon_surf, self.GI_RECT)
            self.CREATE_TEXT(50,50,200, self.title,1)
            value = 300
            for text in self.des:
                self.CREATE_TEXT(20,50,value, text,1)
                value += 25
            for i in range(self.btn_num):
                self.btn[i].draw()
            self.menu_btn.draw()
            self.back_menu()
            self.game_btn.draw()
            self.start_game()

        # Interface with the waning window 
        elif self.wstate and self.mstate == False and self.gstate == False:
            screen.blit(self.bg_surf, self.BG_RECT)
            screen.blit(self.gicon_surf, self.GI_RECT)
            self.CREATE_TEXT(50,50,200, self.title,1)
            value = 300
            for text in self.des:
                self.CREATE_TEXT(20,50,value, text,1)
                value += 25
            for i in range(self.btn_num):
                self.btn[i].draw()
            self.game_btn.draw()
            self.window()
            self.wclose_warning()
            self.menu_btn.draw()




# Class arguments
bg_image_path = "../retro-galaxy/src/backgrounds/travel-bg.jpeg"
game_icon_path = "../retro-galaxy/src/sprites/navecita.png"
x = 0
y = 0
title = "Galactic Travel"
color_title = (255,255,255)
color_text = (255,255,255)

# Element to create the paragraph, because pygame does not support paragraphs
paragraph = [
    "Travel  es  un  juego  basado  en  Flappy  bird",
    "el  cual  consiste  en  explorar  el  inhospito",
    "Neptuno  esquivando  los  asteroides  para",
    "cumplir  la  misión  de  crear  un  mapa  de  la",
    "Galaxia.  Suerte  soldado!!"
]

menu_icon = "../retro-galaxy/src/buttons/neptuno.png"
# Making the instance for the class interface 
travel = Interface(menu_icon, bg_image_path, game_icon_path, x, y,title, paragraph, color_title, color_text)


# while running:
#      for event in pygame.event.get():
#          if event.type == pygame.QUIT:
#              running = False

#      travel.draw()
    
#      pygame.display.update()

