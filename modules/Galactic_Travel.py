# Libraries
from global_variables import *
import random
from interface import Button_game

pygame.init()
clock = pygame.time.Clock()
bg = pygame.image.load('../retro-galaxy/src/backgrounds/travel-bg.jpeg')

# Game variables
running = True
dt = 0
game_speed = 3
frequency = 2000
last_asteroid = pygame.time.get_ticks() - frequency
start = False
game_over = False
score = 0
bombs = 3
lifes = 3
inv_frames = 0
milestone = 1
milestone_lifes = 1
milestone_speed = 1
explosion = pygame.mixer.Sound('../retro-galaxy/src/sounds/Galactic-Travel/8-bit-explosion_F.wav')
music = pygame.mixer.music.load('../retro-galaxy/src/sounds/Galactic-Travel/DesireDrive.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.pause()
game_over_sfx = pygame.mixer.Sound('../retro-galaxy/src/sounds/Galactic-Travel/game_over.wav')
crash_sfx = pygame.mixer.Sound('../retro-galaxy/src/sounds/Galactic-Travel/ovni_hit.wav')
pass_asteroid = False

x_sprites = [ "../retro-galaxy/src/buttons/x-btn.png", "../retro-galaxy/src/buttons/x-btn-press.png"]
z_sprites = [ "../retro-galaxy/src/buttons/z-btn.png", "../retro-galaxy/src/buttons/z-btn-press.png"]

button_x = Button_game(x_sprites[0]," ", 650,500)
button_z = Button_game(z_sprites[0]," ", 250,500)
button_x_pressed = Button_game(x_sprites[1]," ", 650,500)
button_z_pressed = Button_game(z_sprites[1]," ", 250,500)

class Ovni(pygame.sprite.Sprite):
    #Constructor function for the class
    def __init__(self, posicion, player_image):

        pygame.sprite.Sprite.__init__(self)

        self.pos_inicial = posicion
        self.aceleracion = 0.0
        self.velocidad = 0.0
        self.pressed = False
        self.pressed2 = False
        self.image = pygame.transform.scale(pygame.image.load(player_image),(80,40))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos_inicial
    
    def movimiento(self, keys):
        global button_x, button_z, z_sprites

        if button_z.click or keys[pygame.K_z] and self.pressed == False:
          self.velocidad = -400
          self.pressed = True  
          

        elif button_z.click == False and keys[pygame.K_z]== False: 
            self.pressed = False

        if keys[pygame.K_z]:
            button_z_pressed.draw()
            

    #Defines the movement of the playable character
    def posicion(self):
        global game_over
        if game_over == False:
           self.movimiento(pygame.key.get_pressed()) 

        if start == True:
           self.aceleracion = 1500

           self.rect.y += self.velocidad*dt + (self.aceleracion*dt**2)*0.5
           
           self.velocidad += self.aceleracion*dt

        screen.blit(self.image, self.rect)
    
    #Method that gives rewards according to the score
    def score(self, scr):
        global milestone, bombs, lifes, milestone_lifes, milestone_speed, game_speed, frequency

        if scr == 20*milestone:
            bombs += 1
            milestone += 1
            pygame.mixer.Sound.play(pygame.mixer.Sound('../retro-galaxy/src/sounds/Galactic-Travel/bomb.mp3'))

        if scr == 30*milestone_lifes:
            lifes += 1
            milestone_lifes *= 2
            pygame.mixer.Sound.play(pygame.mixer.Sound('../retro-galaxy/src/sounds/Galactic-Travel/life.mp3'))

        if scr == 30*milestone_speed and game_speed < 10:
            game_speed += 1
            milestone_speed += 1
            frequency -= 200

    def clear(self, keys, group = pygame.sprite.Group()):
        global bombs,button_x, x_sprites
        if keys[pygame.K_x] and self.pressed2 == False and bombs > 0:
          
          pygame.mixer.Sound.play(explosion)
          group.empty()
          self.pressed2 = True 
          bombs -= 1

        if keys[pygame.K_x] == False: 
            self.pressed2 = False
        
        if keys[pygame.K_x]:
            button_x_pressed.draw()

    
    def collide(self, time):

        global inv_frames, lifes

        pygame.mixer.Sound.play(crash_sfx)
        lifes -= 1
        inv_frames = time

    def lose(self):
        pygame.mixer.Sound.play(game_over_sfx)
        self.image = pygame.transform.flip(self.image, False, True)
        global game_over, button_x, button_z, z_sprites, x_sprites
        game_over = True
        screen.blit(self.image, self.rect)


class Message:
    def __init__(self, text, x, y, font, size, color):
        self.text = text
        self.x = x
        self.y = y
        self.text_font = pygame.font.Font(font, size)
        self.text_surf = self.text_font.render(text, True, color)
        self.text_rect = pygame.Surface.get_rect(self.text_surf, center = (x,y))

    def draw_text(self):
        screen.blit(self.text_surf,self.text_rect)

class Obstaculos(pygame.sprite.Sprite):
    
    #Constructor class that gives and x and y position to the obstacle and an animation
    def __init__(self, image1, x, y, type):

        pygame.sprite.Sprite.__init__(self)

        if type == 1:
           self.image = pygame.transform.scale(pygame.image.load(image1), (100,100))
           self.rect = self.image.get_rect()
           self.rect.topleft = [x,y]
        
        if type == 2:
           self.image = pygame.transform.scale(pygame.image.load(image1), (150,150))
           self.rect = self.image.get_rect()
           self.rect.topleft = [x,y]

        if type == 3:
           self.image = pygame.transform.scale(pygame.image.load(image1), (200,200))
           self.rect = self.image.get_rect()
           self.rect.topleft = [x,y]

    def update(self):
        global game_speed, score

        self.rect.x -= game_speed

        if self.rect.right < -20:
            self.kill()
            score +=1


jugador = Ovni((340,200),'../retro-galaxy/src/sprites/Galactic-Travel/ufo.png')
asteroid_group = pygame.sprite.Group()
start_text = Message('Presione Z para comenzar', 540, 150, '../retro-galaxy/src/fonts/font2.ttf', 40, 'white')

label1 = Message("Saltar", 315,480,'../retro-galaxy/src/fonts/font2.ttf', 30, "white" )
label2 = Message("Bomba", 715,480,'../retro-galaxy/src/fonts/font2.ttf', 30, "white" )


restart = Message("¡Haz  perdido!", 540, 150,'../retro-galaxy/src/fonts/font1.otf', 40, "red")
restart2 = Message("1.  Presiona  ESC  para  volver  al  menu  de  Neptuno", 540, 220,'../retro-galaxy/src/fonts/font1.otf', 20, "white")
restart3 = Message("2.  Presiona  SPACE  para  volver a  jugar", 540, 270,'../retro-galaxy/src/fonts/font1.otf', 20, "white")
def galactic_travel():
    global running, start, dt, frequency, last_asteroid, score, bombs, lifes, inv_frames, pass_asteroid, button_x, button_z,game_over

    screen.blit(bg,(0,0))
    time = pygame.time.get_ticks()
    button_x.draw()
    button_z.draw()
    label1.draw_text()
    label2.draw_text()

    if start == False:
        
        start_text.draw_text()
        check = pygame.key.get_pressed()

        if check[pygame.K_z]:
            start = True
    
    score_show = Message(f"Score: {score}", 180, 25, '../retro-galaxy/src/fonts/font1.otf', 40, (166,212,242))
    score_show.draw_text()

    bomb_numb = Message(f"Bombs: {bombs}", 510, 25, '../retro-galaxy/src/fonts/font1.otf', 40, (127, 255, 212))
    bomb_numb.draw_text()

    lifes_numb = Message(f"Vidas: {lifes}", 850, 25, '../retro-galaxy/src/fonts/font1.otf', 40, (255, 49, 49))
    lifes_numb.draw_text()

    if start == True and game_over == False:
        
        pygame.mixer.music.unpause()
        jugador.score(score)
        #Generates more obstacles
        if time - last_asteroid > frequency:

            asteroid_type = random.randint(1,3)

            if asteroid_type == 1:
                 asteroid_pos = random.randint(0, 300)
            
            if asteroid_type == 2:
                 asteroid_pos = random.randint(0, 250)
            
            if asteroid_type == 3:
                 asteroid_pos = random.randint(0, 200)
            
            obstacle = Obstaculos('../retro-galaxy/src/sprites/Galactic-Travel/asteroid1.png', 1080, 0 + asteroid_pos, asteroid_type )
            asteroid_group.add(obstacle)
            last_asteroid = time
        
        asteroid_group.update()
        
    asteroid_group.draw(screen)
    jugador.posicion()

    if game_over == False and start == True:
        if pygame.sprite.spritecollide(jugador, asteroid_group, False) and time - inv_frames > 3000:
            jugador.collide(time)

        if lifes == 0 or jugador.rect.y > 420 or jugador.rect.y < -30:
            lifes = 0
            jugador.lose()

            
            pygame.mixer.music.stop()
        jugador.clear(pygame.key.get_pressed(), asteroid_group)
        
    if game_over == True: 
        restart.draw_text()
        restart2.draw_text()
        restart3.draw_text()


    pygame.draw.line(screen, 'white',(0,430),(1080,430),5)

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

def new_game():
    global running, start, dt, frequency, last_asteroid, score, bombs, lifes, inv_frames, pass_asteroid,game_over, milestone_lifes, milestone, milestone_speed, game_speed, jugador, asteroid_group
    running = True
    dt = 0
    game_speed = 3
    frequency = 2000
    start = False
    game_over = False
    score = 0
    bombs = 3
    lifes = 3
    inv_frames = 0
    milestone = 1
    milestone_lifes = 1
    milestone_speed = 1
    jugador = Ovni((340,200),'../retro-galaxy/src/sprites/Galactic-Travel/ufo.png')
    asteroid_group = pygame.sprite.Group()
    pygame.mixer.music.play(-1)
    pygame.mixer.music.pause()