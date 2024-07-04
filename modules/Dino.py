from global_variables import *
import global_variables as gv 
import random

from pygame import K_ESCAPE, KEYDOWN

pygame.init()
pygame.mixer.init()

# Globales Constantes

PANTALLA_ALTO = 720
PANTALLA_ANCHO = 1080

CORRER = [pygame.image.load("../retro-galaxy/src/sprites/Dino/dino/DinoRun1.png"),
          pygame.image.load("../retro-galaxy/src/sprites/Dino/dino/DinoRun2.png")]
SALTAR = pygame.image.load("../retro-galaxy/src/sprites/Dino/dino/DinoJump.png")
AGACHARSE = [pygame.image.load("../retro-galaxy/src/sprites/Dino/dino/DinoDuck1.png"),
             pygame.image.load("../retro-galaxy/src/sprites/Dino/dino/DinoDuck2.png")]

CACTUS_PEQUEÑO = [pygame.image.load("../retro-galaxy/src/sprites/Dino/cactus/SmallCactus1.png"),
                  pygame.image.load("../retro-galaxy/src/sprites/Dino/cactus/SmallCactus2.png"),
                  pygame.image.load("../retro-galaxy/src/sprites/Dino/cactus/SmallCactus3.png")]
CACTUS_GRANDE = [pygame.image.load("../retro-galaxy/src/sprites/Dino/cactus/LargeCactus1.png"),
                 pygame.image.load("../retro-galaxy/src/sprites/Dino/cactus/LargeCactus2.png"),
                 pygame.image.load("../retro-galaxy/src/sprites/Dino/cactus/LargeCactus3.png")]

BIRD = [pygame.image.load("../retro-galaxy/src/sprites/Dino/bird/Bird1.png"),
        pygame.image.load("../retro-galaxy/src/sprites/Dino/bird/Bird2.png")]

NUBE = pygame.image.load("../retro-galaxy/src/sprites/Dino/Cloud.png")

PISTA = pygame.image.load("../retro-galaxy/src/sprites/Dino/Track.png")

GAME_OVER = pygame.image.load("../retro-galaxy/src/sprites/Dino/GameOver.png")
fondo = pygame.image.load("../retro-galaxy/src/backgrounds/Dino/fondo.png")
fondo = pygame.transform.scale(fondo, (800, 400))

arriba = pygame.image.load("../retro-galaxy/src/buttons/arriba.png")
flecha1 = arriba.convert_alpha()
flecha1 = pygame.transform.scale(flecha1, (90, 90))
abajo = pygame.image.load("../retro-galaxy/src/buttons/abajo.png")
flecha2 = abajo.convert_alpha()
flecha2 = pygame.transform.scale(flecha2, (90, 90))

font = pygame.font.SysFont('Impact', 50)
BFont = pygame.font.SysFont('Impact', 40)

fps = 30

death = pygame.mixer.Sound("../retro-galaxy/src/sounds/Dino/game-over.mp3")

sound_played = False

mainClock = pygame.time.Clock()


class Dinosaurio:
    X_POS = 15
    Y_POS = 209
    Y_POS_AGACHADO = 228
    JUMP_VEL = 8.5

    def __init__(self):
        self.agachado_img = AGACHARSE
        self.correr_img = CORRER
        self.saltar_img = SALTAR

        self.dino_agachado = False
        self.dino_correr = True
        self.dino_saltar = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.correr_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_agachado:
            self.agachado()
        if self.dino_correr:
            self.correr()
        if self.dino_saltar:
            self.saltar()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_saltar:
            self.dino_agachado = False
            self.dino_correr = False
            self.dino_saltar = True
        elif userInput[pygame.K_DOWN] and not self.dino_saltar:
            self.dino_agachado = True
            self.dino_correr = False
            self.dino_saltar = False
        elif not (self.dino_saltar or userInput[pygame.K_DOWN]):
            self.dino_agachado = False
            self.dino_correr = True
            self.dino_saltar = False

    def agachado (self):
        self.image = self.agachado_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_AGACHADO
        self.step_index += 1

    def correr(self):
        self.image = self.correr_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def saltar(self):
        self.image = self.saltar_img
        if self.dino_saltar:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_saltar = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Nube:
    
    def __init__(self):
        self.x = PANTALLA_ANCHO + random.randint(800 , 1000)
        self.y = random.randint(20 , 70)
        self.image = NUBE
        self.ancho = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.ancho:
            self.x = PANTALLA_ANCHO + random.randint(2500 , 3000)
            self.y = random.randint(20 , 70)

    def draw(self , screen):
        screen.blit(self.image, (self.x, self.y))


class Obstaculo:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = PANTALLA_ANCHO

    def update (self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstaculos.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)


class CactusPequeño(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0 , 2)
        super().__init__(image, self.type)
        self.rect.y = 238


class CactusGrande(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 215


class Bird(Obstaculo):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 120
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1

def Pantalla():
    screen.fill((0, 0, 0))

def death_sound():
    global sound_played
    if not sound_played:
        death.play()
        sound_played = True

def main():
    global game_speed, x_pos_bg, y_pos_bg, puntos, obstaculos, sound_played
    run = True
    sound_played = False
    clock = pygame.time.Clock()
    player = Dinosaurio()
    nube = Nube()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 185
    puntos = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    fonts = pygame.font.SysFont('arial black', 25)
    obstaculos = []
    muertes = 0

    def Puntuacion():
        global puntos, game_speed
        if not muertes > 0:
            puntos += 1
            if puntos % 100 == 0:
                game_speed += 1

        text = font.render("Puntos: " + str(puntos), True, ( 255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        screen.blit(text, textRect)


    def Piso():
        global x_pos_bg, y_pos_bg
        image_ancho = PISTA.get_width()
        screen.blit(PISTA, (x_pos_bg, y_pos_bg))
        screen.blit(PISTA, (image_ancho + x_pos_bg, y_pos_bg))
        if x_pos_bg  <= - image_ancho:
            screen.blit(PISTA, (image_ancho + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
       
        text = fonts.render("Utiliza estas teclas para jugar: ", True, ( 255, 0, 7))
        textRect = text.get_rect()
        textRect.center = (560, 440)
        
        userInput = pygame.key.get_pressed()

        if muertes == 0:
           Pantalla()
           screen.blit(flecha1 , (500, 470))
           screen.blit(flecha2, (500, 570))
           screen.blit(text, textRect)
           player.draw(screen)
           if len(obstaculos) == 0:
                if random.randint(0, 2) == 0:
                   obstaculos.append(CactusPequeño(CACTUS_PEQUEÑO))
                elif random.randint(0, 2) == 1:
                    obstaculos.append(CactusGrande(CACTUS_GRANDE))
                elif random.randint(0, 2) == 2:
                    obstaculos.append(Bird(BIRD))

           for obstaculo in obstaculos:
                obstaculo.draw(screen)
                obstaculo.update()
                if player.dino_rect.colliderect(obstaculo.rect):
                    pygame.time.delay(1000)
                    muertes += 1
                    death_sound()
                    sound_played = True
            
           player.update(userInput)

           Piso()
           nube.draw(screen)
           nube.update()
           Puntuacion()
            
        clock.tick(30)
        pygame.display.update()

        if muertes > 0:

            screen.fill((0, 0, 0))
            text = font.render("Press Enter to Restart", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (PANTALLA_ANCHO // 2, PANTALLA_ALTO // 2)

            score = font.render("Your Score: " + str(puntos), True, (255, 255, 255))
            scoreRect = score.get_rect()
            scoreRect.center = (PANTALLA_ANCHO // 2, PANTALLA_ALTO // 2 + 100)
            screen.blit(text, textRect)
            screen.blit(score, scoreRect)
            screen.blit(GAME_OVER, (PANTALLA_ANCHO // 2 - 180, PANTALLA_ALTO // 2 - 200))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                main()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False

    Pantalla()