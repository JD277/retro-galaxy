#Libraries
import pygame
import random
import os
os.chdir('Desktop/Proyecto (Arcade)')

pygame.init()
screen = pygame.display.set_mode((800, 400))
name = pygame.display.set_caption("Galactic Travel")
clock = pygame.time.Clock()
bg = pygame.transform.scale(pygame.image.load('assets/background/travel-bg.jpeg'),(800,400))


#Game variables
running = True
dt = 0
game_speed = 2
frequency = 2100
last_asteroid = pygame.time.get_ticks() - frequency
start = False
game_over = False
score = 0

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

class Pajaro(pygame.sprite.Sprite):
    #Constructor function for the class
    def __init__(self, posicion, player_image):

        pygame.sprite.Sprite.__init__(self)

        self.pos_inicial = posicion
        self.aceleracion = 0.0
        self.velocidad = 0.0
        self.pressed = False
        self.image = pygame.transform.scale(pygame.image.load(player_image),(80,40))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos_inicial

        #Character hitbox
    

    
    def pajaro_movimiento(self, keys):

        if keys[pygame.K_z] == False:
            self.pressed = False

        if keys[pygame.K_z] and self.pressed == False:
          self.velocidad = -500
          self.pressed = True

    #Defines the movement of the playable character
    def posicion(self):

        self.pajaro_movimiento(pygame.key.get_pressed()) 

        if start == True:
           self.aceleracion = 1500

           self.rect.y += self.velocidad*dt + (self.aceleracion*dt**2)*0.5
           
           self.velocidad += self.aceleracion*dt

        screen.blit(self.image, self.rect)

    def lose(self):
        self.image = pygame.transform.flip(self.image, False, True)
        global game_over 
        game_over = True
        screen.blit(self.image, self.rect)

class Obstaculos(pygame.sprite.Sprite):
    def __init__(self, image, x, y, type):

        pygame.sprite.Sprite.__init__(self)

        if type == 1:
           self.image = pygame.transform.scale(pygame.image.load(image), (100, 100))
           self.rect = self.image.get_bounding_rect()
           self.rect.topleft = [x,y]

        if type == 2:
           self.image = pygame.transform.scale(pygame.image.load(image), (150, 150))
           self.rect = self.image.get_bounding_rect()
           self.rect.topleft = [x,y]

    def update(self):
        self.rect.x -= game_speed

        if self.rect.right < 0:
            self.kill()

jugador = Pajaro((200,200),'assets/character/ufo.png')
asteroid_group = pygame.sprite.Group()
start_text = Message('Presione Z para comenzar', 400, 150, 'assets/fonts/font2.ttf', 40, 'white')


def galactic_travel():
    global running, start, dt, frequency, last_asteroid, score

    screen.blit(bg,(0,0))

    time = pygame.time.get_ticks()

    if start == False:

        start_text.draw_text()
        check = pygame.key.get_pressed()

        if check[pygame.K_z]:
            start = True
    
    score_show = Message(str(score), 30, 25, 'assets/fonts/font1.otf', 40, (166,212,242))
    score_show.draw_text()

    if start == True and game_over == False:

        #Generates more obstacles
        if time - last_asteroid > frequency:
            asteroid_pos = random.randint(0, 300)
            asteroid_type = random.randint(1,2)
            obstacle = Obstaculos('assets/blocks/asteroid1.png', 800, 0 + asteroid_pos, asteroid_type )
            asteroid_group.add(obstacle)
            last_asteroid = time

        for i in range(0, len(asteroid_group)):
            if jugador.rect.x == asteroid_group.sprites()[i].rect.x :
                score += 1
        asteroid_group.update()

    if pygame.sprite.spritecollide(jugador, asteroid_group, False):
        jugador.lose()

    if game_over == False:
        jugador.posicion()

    asteroid_group.draw(screen)
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    galactic_travel()

pygame.quit()