#Libraries
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))
name = pygame.display.set_caption("Galactic Travel")
clock = pygame.time.Clock()
bg = pygame.transform.scale(pygame.image.load('assets/background/travel-bg.jpeg'),(800,400))

#Game variables
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
explosion = pygame.mixer.Sound('assets/sfx/8-bit-explosion_F.wav')
music = pygame.mixer.music.load('assets/sfx/DesireDrive.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.pause()
game_over_sfx = pygame.mixer.Sound('assets/sfx/game_over.wav')
crash_sfx = pygame.mixer.Sound('assets/sfx/ovni_hit.wav')
pass_asteroid = False

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

        if keys[pygame.K_z] == False:
            self.pressed = False

        if keys[pygame.K_z] and self.pressed == False:
          self.velocidad = -400
          self.pressed = True     

    #Defines the movement of the playable character
    def posicion(self):

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
            pygame.mixer.Sound.play(pygame.mixer.Sound('assets/sfx/bomb.mp3'))

        if scr == 50*milestone_lifes:
            lifes += 1
            milestone_lifes *= 2
            pygame.mixer.Sound.play(pygame.mixer.Sound('assets/sfx/life.mp3'))

        if scr == 15*milestone_speed and game_speed < 11:
            game_speed += 1
            milestone_speed += 1
            frequency -= 200

    def clear(self, keys, group = pygame.sprite.Group()):
        global bombs

        if keys[pygame.K_x] == False:
            self.pressed2 = False

        if keys[pygame.K_x] and self.pressed2 == False and bombs > 0:
          
          pygame.mixer.Sound.play(explosion)
          group.empty()
          self.pressed2 = True 
          bombs -= 1
    
    def collide(self, time):

        global inv_frames, lifes

        pygame.mixer.Sound.play(crash_sfx)
        lifes -= 1
        inv_frames = time

    def lose(self):
        pygame.mixer.Sound.play(game_over_sfx)
        self.image = pygame.transform.flip(self.image, False, True)
        global game_over 
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
        global game_speed

        self.rect.x -= game_speed

        if self.rect.right < 0:
            self.kill()

jugador = Ovni((200,200),'assets/character/ufo.png')
asteroid_group = pygame.sprite.Group()
start_text = Message('Presione Z para comenzar', 400, 150, 'assets/fonts/font2.ttf', 40, 'white')


def galactic_travel():
    global running, start, dt, frequency, last_asteroid, score, bombs, lifes, inv_frames, pass_asteroid

    screen.blit(bg,(0,0))

    time = pygame.time.get_ticks()

    if start == False:

        start_text.draw_text()
        check = pygame.key.get_pressed()

        if check[pygame.K_z]:
            start = True
    
    score_show = Message(str(score), 30, 25, 'assets/fonts/font1.otf', 40, (166,212,242))
    score_show.draw_text()

    bomb_numb = Message(str(bombs), 770, 25, 'assets/fonts/font1.otf', 40, (127, 255, 212))
    bomb_numb.draw_text()

    lifes_numb = Message(str(lifes), 710, 25, 'assets/fonts/font1.otf', 40, (255, 49, 49))
    lifes_numb.draw_text()

    if start == True and game_over == False:
        
        pygame.mixer.music.unpause()
        jugador.score(score)

        #Generates more obstacles
        if time - last_asteroid > frequency:

            asteroid_pos = random.randint(0, 300)
            asteroid_type = random.randint(1,3)
            obstacle = Obstaculos('assets/blocks/asteroid1.png', 800, 0 + asteroid_pos, asteroid_type )
            asteroid_group.add(obstacle)
            last_asteroid = time

        for i in range(0, len(asteroid_group)):

            if jugador.rect.x > asteroid_group.sprites()[i].rect.left and jugador.rect.x < asteroid_group.sprites()[i].rect.right and pass_asteroid == False:  
       
                score += 1
                pass_asteroid = True

            if pass_asteroid == True and jugador.rect.x > asteroid_group.sprites()[i].rect.right:

                pass_asteroid = False
        
        asteroid_group.update()
        
    asteroid_group.draw(screen)
    jugador.posicion()

    if game_over == False:
        if pygame.sprite.spritecollide(jugador, asteroid_group, False) and time - inv_frames > 3000:
            jugador.collide(time)

        if lifes == 0 or jugador.rect.y > 420 or jugador.rect.y < -30:
            lifes = 0
            jugador.lose()
            pygame.mixer.music.stop()

        jugador.clear(pygame.key.get_pressed(), asteroid_group)

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    galactic_travel()

pygame.quit()