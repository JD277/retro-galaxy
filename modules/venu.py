from global_variables import *
from interface import Interface
import pygame, math, copy
from pygame.locals import *
from Bordesitos import *


class Venus:
    def __init__(self):

        bg_image_path = "../retro-galaxy/src/backgrounds/venus-bg.jpg"
        game_icon_path = "../retro-galaxy/src/sprites/pacman.png"
        x = 0
        y = 0
        title = "Pac-Man"
        color_title = (255, 255, 255)
        color_text = (255, 255, 255)

        paragraph = [
            'Es uno de los juegos más populares y reconocibles de',
            'la historia de los videojuegos. En Pac-Man, el jugador',
            'controla a un personaje amarillo en forma de boca,',
            'Pac-Man, que se mueve a través de un laberinto comiendo',
            'puntos y evitando a cuatro fantasmas de colores',
            'El objetivo principal del juego es comer todos los puntos',
            '(pequeños círculos) que se encuentran en el laberinto,',
            'mientras se evita ser atrapado por los fantasmas. ',
            'Si Pac-Man es tocado por un fantasma, pierde una vida.',

        ]

        menu_icon = "../retro-galaxy/src/buttons/venus.png"

        self.dino = Interface(menu_icon, bg_image_path, game_icon_path, x, y, title, paragraph, color_title, color_text)


    def draw(self):
        if self.dino.gstate == True:

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] == True:
                self.dino.gstate = False

        elif self.dino.gstate == False:
            self.dino.draw()

venus = Venus()

#Clase de los fantasmas y su comportamiento dentro del mapa
class Fantasmas:
    def __init__ (self, cord_x, cord_y, objetivo, velocidad, img, direct, muerto, caja, id):
        self.pos_x = cord_x
        self.pos_y = cord_y
        self.centro_x = self.pos_x + 22
        self.centro_y = self.pos_y + 22
        self.objetivo = objetivo
        self.velocidad = velocidad
        self.img = img
        self.direccion = direct
        self.muerto = muerto
        self.en_caja = caja
        self.id = id
        self.vueltas, self.in_caja = self.check_colisionf()
        self.rect = self.draw()

    def draw(self):
        if (not powerup and not self.muerto) or (fantasma_comido[self.id] and powerup and not self.muerto):
            pantalla.blit(self.img, (self.pos_x, self.pos_y))
        elif powerup and not self.muerto and not fantasma_comido[self.id]:
            pantalla.blit(asustado_img, (self.pos_x, self.pos_y))
        else:
            pantalla.blit(muerto_img, (self.pos_x, self.pos_y))
        ghost_rect = pygame.rect.Rect(
            (self.centro_x - 18, self.centro_y - 18), (36, 36))
        return ghost_rect
    
    def check_colisionf(self):
        num1 = ((Alto - 50) // 32)
        num2 = (Ancho // 30)
        num3 = 15
        self.vueltas = [False, False, False, False]
        if 0 < self.centro_x // 30 < 29:
            if nivel[(self.centro_y - num3) //
                     num1][self.centro_x // num2] == 9:
                self.vueltas[2] = True
            if nivel[self.centro_y //
                     num1][(self.centro_x - num3) // num2] < 3 \
                    or (nivel[self.centro_y //
                              num1][(self.centro_x - num3) // num2] == 9 and (
                    self.en_caja or self.muerto)):
                self.vueltas[1] = True
            if nivel[self.centro_y //
                     num1][(self.centro_x + num3) // num2] < 3 \
                    or (nivel[self.centro_y //
                              num1][(self.centro_x + num3) // num2] == 9 and (
                    self.en_caja or self.muerto)):
                self.vueltas[0] = True
            if nivel[(self.centro_y + num3) //
                     num1][self.centro_x // num2] < 3 \
                    or (nivel[(self.centro_y + num3) //
                              num1][self.centro_x // num2] == 9 and (
                    self.en_caja or self.muerto)):
                self.vueltas[3] = True
            if nivel[(self.centro_y - num3) //
                     num1][self.centro_x // num2] < 3 \
                    or (nivel[(self.centro_y - num3) //
                              num1][self.centro_x // num2] == 9 and (
                    self.en_caja or self.muerto)):
                self.vueltas[2] = True

            if self.direccion == 2 or self.direccion == 3:
                if 12 <= self.centro_x % num2 <= 18:
                    if nivel[(self.centro_y + num3) //
                             num1][self.centro_x // num2] < 3 \
                            or (nivel[(self.centro_y + num3) //
                                      num1][self.centro_x // num2] == 9 and (
                            self.en_caja or self.muerto)):
                        self.vueltas[3] = True
                    if nivel[(self.centro_y - num3) //
                             num1][self.centro_x // num2] < 3 \
                            or (nivel[(self.centro_y - num3) //
                                      num1][self.centro_x // num2] == 9 and (
                            self.en_caja or self.muerto)):
                        self.vueltas[2] = True
                if 12 <= self.centro_y % num1 <= 18:
                    if nivel[self.centro_y // num1][(
                        self.centro_x - num2) // num2] < 3 \
                            or (nivel[self.centro_y // num1][(
                                self.centro_x - num2) // num2] == 9 and (
                                self.en_caja or self.muerto)):
                        self.vueltas[1] = True
                    if nivel[self.centro_y // num1][(self.centro_x + num2) //
                                                    num2] < 3 or (nivel[self.centro_y //
                                                                        num1][(self.centro_x + num2) // num2] == 9 and (
                                                        self.en_caja or self.muerto)):
                        self.vueltas[0] = True

            if self.direccion == 0 or self.direccion == 1:
                if 12 <= self.centro_x % num2 <= 18:
                    if nivel[(self.centro_y + num3) //
                             num1][self.centro_x // num2] < 3 \
                            or (nivel[(self.centro_y + num3) //
                                      num1][self.centro_x // num2] == 9 and (
                            self.en_caja or self.muerto)):
                        self.vueltas[3] = True
                    if nivel[(self.centro_y - num3) //
                             num1][self.centro_x // num2] < 3 \
                            or (nivel[(self.centro_y - num3) //
                                      num1][self.centro_x // num2] == 9 and (
                            self.en_caja or self.muerto)):
                        self.vueltas[2] = True
                if 12 <= self.centro_y % num1 <= 18:
                    if nivel[self.centro_y // num1][(
                        self.centro_x - num3) // num2] < 3 \
                            or (nivel[self.centro_y // num1][(
                                self.centro_x - num3) // num2] == 9 and (
                            self.en_caja or self.muerto)):
                        self.vueltas[1] = True
                    if nivel[self.centro_y // num1][(
                        self.centro_x + num3) // num2] < 3 \
                            or (nivel[self.centro_y // num1][(
                                self.centro_x + num3) // num2] == 9 and (
                            self.en_caja or self.muerto)):
                        self.vueltas[0] = True
        else:
            self.vueltas[0] = True
            self.vueltas[1] = True
        if 350 < self.pos_x < 550 and 370 < self.pos_y < 480:
            self.en_caja = True
        else:
            self.en_caja = False
        return self.vueltas, self.en_caja
    
    def movimiento_amarillo(self):
        if self.direccion == 0:
            if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                self.pos_x += self.velocidad
            elif not self.vueltas[0]:
                if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
            elif self.vueltas[0]:
                if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                if self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                else:
                    self.pos_x += self.velocidad
        elif self.direccion == 1:
            if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                self.direccion = 3
            elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                self.pos_x -= self.velocidad
            elif not self.vueltas[1]:
                if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
            elif self.vueltas[1]:
                if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                if self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                else:
                    self.pos_x -= self.velocidad
        elif self.direccion == 2:
            if self.objetivo[0] < self.pos_x and self.vueltas[1]:
                self.direccion = 1
                self.pos_x -= self.velocidad
            elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                self.direccion = 2
                self.pos_y -= self.velocidad
            elif not self.vueltas[2]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
            elif self.vueltas[2]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                else:
                    self.pos_y -= self.velocidad
        elif self.direccion == 3:
            if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                self.pos_y += self.velocidad
            elif not self.vueltas[3]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
            elif self.vueltas[3]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                else:
                    self.pos_y += self.velocidad
        if self.pos_x < -30:
            self.pos_x = 900
        elif self.pos_x > 900:
            self.pos_x -= 30
        return self.pos_x, self.pos_y, self.direccion
    
    def movimiento_rojo(self):
        if self.direccion == 0:
            if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                self.pos_x += self.velocidad
            elif not self.vueltas[0]:
                if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
            elif self.vueltas[0]:
                self.pos_x += self.velocidad
        elif self.direccion == 1:
            if self.objetivo[0] < self.pos_x and self.vueltas[1]:
                self.pos_x -= self.velocidad
            elif not self.vueltas[1]:
                if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
            elif self.vueltas[1]:
                self.pos_x -= self.velocidad
        elif self.direccion == 2:
            if self.objetivo[1] < self.pos_y and self.vueltas[2]:
                self.direccion = 2
                self.pos_y -= self.velocidad
            elif not self.vueltas[2]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
            elif self.vueltas[2]:
                self.pos_y -= self.velocidad
        elif self.direccion == 3:
            if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                self.pos_y += self.velocidad
            elif not self.vueltas[3]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
            elif self.vueltas[3]:
                self.pos_y += self.velocidad
        if self.pos_x < -30:
            self.pos_x = 900
        elif self.pos_x > 900:
            self.pos_x -= 30
        return self.pos_x, self.pos_y, self.direccion
    
    def movimiento_azul(self):
        if self.direccion == 0:
            if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                self.pos_x += self.velocidad
            elif not self.vueltas[0]:
                if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
            elif self.vueltas[0]:
                self.pos_x += self.velocidad
        elif self.direccion == 1:
            if self.objetivo[0] < self.pos_x and self.vueltas[1]:
                self.pos_x -= self.velocidad
            elif not self.vueltas[1]:
                if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
            elif self.vueltas[1]:
                self.pos_x -= self.velocidad
        elif self.direccion == 2:
            if self.objetivo[1] < self.pos_y and self.vueltas[2]:
                self.direccion = 2
                self.pos_y -= self.velocidad
            elif not self.vueltas[2]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
            elif self.vueltas[2]:
                self.pos_y -= self.velocidad
        elif self.direccion == 3:
            if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                self.pos_y += self.velocidad
            elif not self.vueltas[3]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
            elif self.vueltas[3]:
                self.pos_y += self.velocidad
        if self.pos_x < -30:
            self.pos_x = 900
        elif self.pos_x > 900:
            self.pos_x -= 30
        return self.pos_x, self.pos_y, self.direccion
    
    def movimiento_rosa(self):
        if self.direccion == 0:
            if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                self.pos_x += self.velocidad
            elif not self.vueltas[0]:
                if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
            elif self.vueltas[0]:
                self.pos_x += self.velocidad
        elif self.direccion == 1:
            if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                self.direccion = 3
            elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                self.pos_x -= self.velocidad
            elif not self.vueltas[1]:
                if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
            elif self.vueltas[1]:
                self.pos_x -= self.velocidad
        elif self.direccion == 2:
            if self.objetivo[0] < self.pos_x and self.vueltas[1]:
                self.direccion = 1
                self.pos_x -= self.velocidad
            elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                self.direccion = 2
                self.pos_y -= self.velocidad
            elif not self.vueltas[2]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.objetivo[1] > self.pos_y and self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.vueltas[3]:
                    self.direccion = 3
                    self.pos_y += self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
            elif self.vueltas[2]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                else:
                    self.pos_y -= self.velocidad
        elif self.direccion == 3:
            if self.objetivo[1] > self.pos_y and self.vueltas[3]:
                self.pos_y += self.velocidad
            elif not self.vueltas[3]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.objetivo[1] < self.pos_y and self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[2]:
                    self.direccion = 2
                    self.pos_y -= self.velocidad
                elif self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                elif self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
            elif self.vueltas[3]:
                if self.objetivo[0] > self.pos_x and self.vueltas[0]:
                    self.direccion = 0
                    self.pos_x += self.velocidad
                elif self.objetivo[0] < self.pos_x and self.vueltas[1]:
                    self.direccion = 1
                    self.pos_x -= self.velocidad
                else:
                    self.pos_y += self.velocidad
        if self.pos_x < -30:
            self.pos_x = 900
        elif self.pos_x > 900:
            self.pos_x -= 30
        return self.pos_x, self.pos_y, self.direccion


#interfaz del juego
def dibujar_interfaz():
    score_texto = fuente.render(f'Score: {score}', True, '#00e6fc')
    pantalla.blit(score_texto, (10, 920))
    if powerup:
        pygame.draw.circle(pantalla, '#d52b1e', (140, 930), 15)
    for i in range(vidas):
        pantalla.blit(pygame.transform.scale(
            jugador_img[0], (30, 30)), (650 + i * 40, 915))
    if game_over:
        pygame.draw.rect(pantalla, '#00e6fc',
                         [265, 215, 370, 120], 0, 10)
        pygame.draw.rect(pantalla, "#0d1117",
                         [270, 220, 360, 110], 0, 10)
        gameover_text = fuente.render(
            'Game over! Presiona espacio para reintentar!', True, '#d52b1e')
        pantalla.blit(gameover_text, (290, 265))
    if game_won:
        pygame.draw.rect(pantalla, '#00e6fc',
                         [265, 215, 370, 120], 0, 10)
        pygame.draw.rect(pantalla, '#151515',
                         [270, 220, 360, 110], 0, 10)
        gameover_text = fuente.render(
            'Victory! Presiona espacio para volver a jugar!', True, '#00ff00')
        pantalla.blit(gameover_text, (307, 265))

#Checar colisiones
def check_colisiones(punt, power, power_cont, fantasma_comido):
    num1 = (Alto - 50) // 32
    num2 = Ancho // 30
    if 0 < player_x < 870:
        if nivel[centro_y // num1][centro_x // num2] == 1:
            nivel[centro_y // num1][centro_x // num2] = 0
            punt += 10
        if nivel[centro_y // num1][centro_x // num2] == 2:
            nivel[centro_y // num1][centro_x // num2] = 0
            punt += 50
            power = True
            power_cont = 0
            fantasma_comido = [False, False, False, False]
    return punt, power, power_cont, fantasma_comido

#Función para dibujar los bordes el mapa
def dibujar_bordes():
    num1 = ((Alto - 50) // 32)
    num2 = (Ancho // 30)
    for i in range (len (nivel)):
        for j in range (len(nivel[i])):
            if nivel[i][j] == 1:
                pygame.draw.circle(pantalla, '#faeb7f',
                                   (j * num2 + (0.5 * num2),
                                    i * num1 + (0.5 * num1)),
                                    4)
            if nivel[i][j] == 2 and not flicker:
                pygame.draw.circle(pantalla, '#faeb7f',
                                   (j * num2 + (0.5 * num2),
                                    i * num1 + (0.5 * num1)),
                                    10)
            if nivel[i][j] == 3:
                pygame.draw.line(pantalla, Color,
                                 (j * num2 + (0.5 * num2),
                                  i * num1),
                                  (j * num2 + (0.5 * num2),
                                   i * num1 + num1), 3)
            if nivel[i][j] == 4:
                pygame.draw.line(pantalla, Color,
                                 (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2,
                                  i * num1 + (0.5 * num1)), 3)
            if nivel[i][j] == 5:
                pygame.draw.arc(pantalla, Color,
                                [(j * num2 - (num2 * 0.4)) - 2,
                                 (i * num1 + (0.5 * num1)),
                                 num2, num1],
                                0, PI / 2, 3)
            if nivel[i][j] == 6: 
                pygame.draw.arc(pantalla, Color,
                                [(j * num2 + (num2 * 0.5)),
                                 (i * num1 + (0.5 * num1)),
                                 num2, num1], PI / 2, PI, 3)
            if nivel[i][j] == 7:
                pygame.draw.arc(pantalla, Color,
                                [(j * num2 + (num2 * 0.5)),
                                 (i * num1 - (0.4 * num1)),
                                 num2, num1], PI,
                                3 * PI / 2, 3)
            if nivel[i][j] == 8:
                pygame.draw.arc(pantalla, Color,
                                [(j * num2 - (num2 * 0.4)) - 2,
                                 (i * num1 - (0.4 * num1)),
                                 num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if nivel[i][j] == 9: 
                pygame.draw.line(pantalla, '#faeb7f',
                                 (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2,
                                  i * num1 + (0.5 * num1)), 3)
                
#Funcion para dibujar al jugador
def dibujar_jugador():
    if direccion == 0:
        pantalla.blit(jugador_img[cont // 5],
                      (player_x, player_y))
    elif direccion == 1:
        pantalla.blit(pygame.transform.flip(
            jugador_img[cont // 5], True, False),
            (player_x, player_y))
    elif direccion == 2:
        pantalla.blit(pygame.transform.rotate(
            jugador_img[cont // 5], 90),
            (player_x, player_y))
    elif direccion == 3:
        pantalla.blit(pygame.transform.rotate(
            jugador_img[cont // 5], 270),
            (player_x, player_y))
        
#Checar posición del jugador 
def check_posicion(centrox, centroy):
    vueltas = [False, False, False, False]
    num1 = (Alto - 50) // 32
    num2 = (Ancho // 30)
    num3 = 15
    if centrox // 30 < 29:
        if direccion == 0:
            if nivel[centroy // num1][(centrox - num3) // num2] < 3:
                vueltas[1] = True
        if direccion == 1:
            if nivel[centroy // num1][(centrox + num3) // num2] < 3:
                vueltas[0] = True
        if direccion == 2:
            if nivel[(centroy + num3) // num1][centrox // num2] < 3:
                vueltas[3] = True
        if direccion == 3:
            if nivel[(centroy - num3) // num1][centrox // num2] < 3:
                vueltas[2] = True
        
        if direccion == 2 or direccion == 3:
            if 12 <= centro_x % num2 <= 18:
                if nivel[(centroy + num3) // num1][centrox // num2] < 3:
                    vueltas[3] = True
                if nivel[(centroy - num3) // num1][centrox // num2] < 3:
                    vueltas[2] = True
            if 12 <= centroy % num1 <= 18:
                if nivel[centroy // num1][(centrox - num2) // num2] < 3:
                    vueltas[1] = True
                if nivel[centroy // num1][(centrox + num2) // num2] < 3:
                    vueltas[0] = True
        
        if direccion == 0 or direccion == 1:
            if 12 <= centrox % num2 <= 18:
                if nivel[(centroy + num1) // num1][centrox // num2] < 3:
                    vueltas[3] = True
                if nivel[(centroy - num1) // num1][centrox // num2] < 3:
                    vueltas[2] = True
            if 12 <= centroy % num1 <= 18:
                if nivel[centroy // num1][(centrox - num3) // num2] < 3:
                    vueltas[1] = True
                if nivel[centroy // num1][(centrox + num3) // num2] < 3:
                    vueltas[0] = True
    else:
        vueltas[0] = True
        vueltas[1] = True

    return vueltas

#Movimiento del jugador
def mover_jugador(play_x, play_y):
    if direccion == 0 and giros_permitidos[0]:
        play_x += velocidad_player
    elif direccion == 1 and giros_permitidos[1]:
        play_x -= velocidad_player
    if direccion == 2 and giros_permitidos[2]:
        play_y -= velocidad_player
    elif direccion == 3 and giros_permitidos[3]:
        play_y += velocidad_player
    return play_x, play_y

#Objetivos de los fantasmas para alcanzar a pacman
def get_objetivos(rojo_x, rojo_y, azul_x, azul_y,
                  rosa_x, rosa_y, amarillo_x, amarillo_y):
    if player_x < 450:
        runaway_x = 900
    else:
        runaway_x = 0
    if player_y < 450:
        runaway_y = 900
    else:
        runaway_y = 0
    return_objetivo = (380, 400)
    if powerup:
        if not FRojo.muerto and not fantasma_comido[0]:
            objetivo_rojo = (runaway_x, runaway_y)
        elif not FRojo.muerto and fantasma_comido[0]:
            if 340 < rojo_x < 560 and 340 < rojo_y < 500:
                objetivo_rojo = (400, 100)
            else:
                objetivo_rojo = (player_x, player_y)
        else:
            objetivo_rojo = return_objetivo
        if not FAzul.muerto and not fantasma_comido[1]:
            objetivo_azul = (runaway_x, player_y)
        elif not FAzul.muerto and fantasma_comido[1]:
            if 340 < azul_x < 560 and 340 < azul_y < 500:
                objetivo_azul = (400, 100)
            else:
                objetivo_azul = (player_x, player_y)
        else:
            objetivo_azul = return_objetivo
        if not FRosa.muerto:
            objetivo_rosa = (player_x, runaway_y)
        elif not FRosa.muerto and fantasma_comido[2]:
            if 340 < rosa_x < 560 and 340 < rosa_y < 500:
                objetivo_rosa = (400, 100)
            else:
                objetivo_rosa = (player_x, player_y)
        else:
            objetivo_rosa = return_objetivo
        if not FAmarillo.muerto and not fantasma_comido[3]:
            objetivo_amarillo = (450, 450)
        elif not FAmarillo.muerto and fantasma_comido[3]:
            if 340 < amarillo_x < 560 and 340 < amarillo_y < 500:
                objetivo_amarillo = (400, 100)
            else:
                objetivo_amarillo = (player_x, player_y)
        else:
            objetivo_amarillo = return_objetivo
    else:
        if not FRojo.muerto:
            if 340 < rojo_x < 560 and 340 < rojo_y < 500:
                objetivo_rojo = (400, 100)
            else:
                objetivo_rojo = (player_x, player_y)
        else:
            objetivo_rojo = return_objetivo
        if not FAzul.muerto:
            if 340 < azul_x < 560 and 340 < azul_y < 500:
                objetivo_azul = (400, 100)
            else:
                objetivo_azul = (player_x, player_y)
        else:
            objetivo_azul = return_objetivo
        if not FRosa.muerto:
            if 340 < rosa_x < 560 and 340 < rosa_y < 500:
                objetivo_rosa = (400, 100)
            else:
                objetivo_rosa = (player_x, player_y)
        else:
            objetivo_rosa = return_objetivo
        if not FAmarillo.muerto:
            if 340 < amarillo_x < 560 and 340 < amarillo_y < 500:
                objetivo_amarillo = (400, 100)
            else:
                objetivo_amarillo = (player_x, player_y)
        else:
            objetivo_amarillo = return_objetivo
    return [objetivo_rojo, objetivo_azul,
            objetivo_rosa, objetivo_amarillo]

#Main principal y bucle principal
if __name__ == '__main__':

    #paleta de colores
    Blanco = (255, 255, 255)
    Negro = (0, 0, 0)
    Rojo = (255, 0, 0)
    Azul = (0, 0, 255)
    Verde = (0, 255, 0)
    Color = '#0000cc'

    #pantalla y ventana del juego
    Ancho = 900
    Alto = 950
    pantalla = pygame.display.set_mode((Alto, Ancho))
    timer = pygame.time.Clock()
    fuente = pygame.font.Font('freesansbold.ttf', 20)
    #icono y nombre del juego
    pygame.display.set_caption('PAC-MAN')
    icono = pygame.image.load("imagenes/icon.png")
    pygame.display.set_icon(icono)
    nivel = copy.deepcopy(bordesitos)
    PI = math.pi
    fps = 60
    jugador_img = []
    for i in range(1, 5):
        jugador_img.append(pygame.transform.scale(pygame.image.load(
            f'Imagenes/IMGs/{i}.png'), (45, 45)))
    rojo_img = pygame.transform.scale(pygame.image.load(
        f'Imagenes/IMGs/rojo.png'), (45, 45))
    rosa_img = pygame.transform.scale(pygame.image.load(
        f'Imagenes/IMGs/rosa.png'), (45, 45))
    azul_img = pygame.transform.scale(pygame.image.load(
        f'Imagenes/IMGs/azul.png'), (45, 45))
    amarillo_img = pygame.transform.scale(pygame.image.load(
        f'Imagenes/IMGs/amarillo.png'), (45, 45))
    asustado_img = pygame.transform.scale(pygame.image.load(
        f'Imagenes/IMGs/powerup.png'), (45, 45))
    muerto_img = pygame.transform.scale(pygame.image.load(
        f'Imagenes/IMGs/muerto.png'), (45, 45))

    player_x = 450
    player_y = 663
    direccion = 0
    rojo_x = 56
    rojo_y = 58
    direccion_rojo = 0
    azul_x = 440
    azul_y = 388
    direccion_azul = 2
    rosa_x = 440
    rosa_y = 400
    direccion_rosa = 2
    amarillo_x = 440
    amarillo_y = 438
    direccion_amarillo = 2
    cont = 0
    flicker = False

    giros_permitidos = [False, False, False, False]
    direccion_comando = 0
    velocidad_player = 2
    score = 0
    powerup = False
    cont_power = 0
    fantasma_comido = [False, False, False, False]
    objetivos = [(player_x, player_y),
                 (player_x, player_y),
                 (player_x, player_y),
                 (player_x, player_y)]

    rojo_muerto = False
    azul_muerto = False
    rosa_muerto = False
    amarillo_muerto = False
    rojo_en_caja = False
    azul_en_caja = False
    amarillo_en_caja = False
    rosa_en_caja = False
    moving = False
    velocidad_fantasmas = [2, 2, 2, 2]
    startup_cont = 0
    vidas = 3
    game_over = False
    game_won = False

    run = True
    while run:
        timer.tick(fps)
        if cont < 19:
            cont += 1
            if cont > 3:
                flicker = False
        else:
            cont = 0
            flicker = True
        if powerup and cont_power < 600:
            cont_power +=1
        elif powerup and cont_power >= 600:
            cont_power = 0
            powerup = False
            fantasma_comido = [False, False, False, False]
        if startup_cont < 180 and not game_over and not game_won:
            moving = False
            startup_cont += 1
        else:
            moving = True

        pantalla.fill('#151515')
        dibujar_bordes()
        centro_x = player_x + 23
        centro_y = player_y + 24
        if powerup:
            velocidad_fantasmas = [1, 1, 1, 1]
        else:
            velocidad_fantasmas = [2, 2, 2, 2]
        if fantasma_comido[0]:
            velocidad_fantasmas[0] = 2
        if fantasma_comido[1]:
            velocidad_fantasmas[1] = 2
        if fantasma_comido[2]:
            velocidad_fantasmas[2] = 2
        if fantasma_comido[3]:
            velocidad_fantasmas[3] = 2
        if rojo_muerto:
            velocidad_fantasmas[0] = 4
        if azul_muerto:
            velocidad_fantasmas[1] = 4
        if rosa_muerto:
            velocidad_fantasmas[2] = 4
        if amarillo_muerto:
            velocidad_fantasmas[3] = 4

        game_won = True
        for i in range(len(nivel)):
            if 1 in nivel[i] or 2 in nivel[i]:
                game_won = False

        player_circle = pygame.draw.circle(pantalla, '#0d1117',
                                           (centro_x, centro_y), 20, 2)
        dibujar_jugador()
        FRojo = Fantasmas(rojo_x, rojo_y, objetivos[0],
                          velocidad_fantasmas[0], rojo_img,
                          direccion_rojo, rojo_muerto,
                          rojo_en_caja, 0)
        FAzul = Fantasmas(azul_x, azul_y, objetivos[1],
                          velocidad_fantasmas[1], azul_img,
                          direccion_azul, azul_muerto,
                          azul_en_caja, 1)
        FRosa = Fantasmas(rosa_x, rosa_y, objetivos[2],
                          velocidad_fantasmas[2], rosa_img,
                          direccion_rosa, rosa_muerto,
                          rosa_en_caja, 2)
        FAmarillo = Fantasmas(amarillo_x, amarillo_y, objetivos[3],
                              velocidad_fantasmas[3], amarillo_img,
                              direccion_amarillo, amarillo_muerto,
                              amarillo_en_caja, 3)
        dibujar_interfaz()
        objetivos = get_objetivos(rojo_x, rojo_y, azul_x, azul_y,
                                  rosa_x, rosa_y, amarillo_x, amarillo_y)

        giros_permitidos = check_posicion(centro_x, centro_y)
        if moving:
            player_x, player_y = mover_jugador(player_x, player_y)
            if not rojo_muerto and not FRojo.en_caja:
                rojo_x, rojo_y, direccion_rojo = FRojo.movimiento_rojo()
            else:
                rojo_x, rojo_y, direccion_rojo = FRojo.movimiento_amarillo()
            if not rosa_muerto and not FRosa.en_caja:
                rosa_x, rosa_y, direccion_rosa = FRosa.movimiento_rosa()
            else:
                rosa_x, rosa_y, direccion_rosa = FRosa.movimiento_amarillo()
            if not azul_muerto and not FAzul.en_caja:
                azul_x, azul_y, direccion_azul = FAzul.movimiento_azul()
            else:
                azul_x, azul_y, direccion_azul = FAzul.movimiento_amarillo()
            amarillo_x, amarillo_y, direccion_amarillo = FAmarillo.movimiento_amarillo()
        score, powerup, cont_power, fantasma_comido = check_colisiones(
            score, powerup,
            cont_power, fantasma_comido)

        if not powerup:
            if (player_circle.colliderect(
                FRojo.rect) and not FRojo.muerto) or \
                    (player_circle.colliderect(
                        FAzul.rect) and not FAzul.muerto) or \
                    (player_circle.colliderect(FRosa.rect) and not FRosa.muerto) or \
                    (player_circle.colliderect(FAmarillo.rect) and not FAmarillo.muerto):
                if vidas > 0:
                    vidas -= 1
                    startup_cont = 0
                    powerup = False
                    cont_power = 0
                    player_x = 450
                    player_y = 663
                    direccion = 0
                    direccion_comando = 0
                    rojo_x = 56
                    rojo_y = 58
                    direccion_rojo = 0
                    azul_x = 440
                    azul_y = 388
                    direccion_azul = 2
                    rosa_x = 440
                    rosa_y = 438
                    direccion_rosa = 2
                    amarillo_x = 440
                    amarillo_y = 438
                    direccion_amarillo = 2
                    fantasma_comido = [False, False,
                                   False, False]
                    rojo_muerto = False
                    azul_muerto = False
                    amarillo_muerto = False
                    rosa_muerto = False
                else:
                    game_over = True
                    moving = False
                    startup_cont = 0
        if powerup and player_circle.colliderect(FRojo.rect) and\
                fantasma_comido[0] and not FRojo.muerto:
            if vidas > 0:
                powerup = False
                cont_power = 0
                vidas -= 1
                startup_cont = 0
                player_x = 450
                player_y = 663
                direccion = 0
                direccion_comando = 0
                rojo_x = 56
                rojo_y = 58
                direccion_rojo = 0
                azul_x = 440
                azul_y = 388
                direccion_azul = 2
                rosa_x = 440
                rosa_y = 438
                direccion_rosa = 2
                amarillo_x = 440
                amarillo_y = 438
                direccion_amarillo = 2
                fantasma_comido = [False, False,
                               False, False]
                rojo_muerto = False
                azul_muerto = False
                amarillo_muerto = False
                rosa_muerto = False
            else:
                game_over = True
                moving = False
                startup_cont = 0
        if powerup and player_circle.colliderect(FAzul.rect) and\
                fantasma_comido[1] and not FAzul.muerto:
            if vidas > 0:
                powerup = False
                cont_power = 0
                vidas -= 1
                startup_cont = 0
                player_x = 450
                player_y = 663
                direccion = 0
                direccion_comando = 0
                rojo_x = 56
                rojo_y = 58
                direccion_rojo = 0
                azul_x = 440
                azul_y = 388
                direccion_azul = 2
                rosa_x = 440
                rosa_y = 438
                direccion_rosa = 2
                amarillo_x = 440
                amarillo_y = 438
                direccion_amarillo = 2
                fantasma_comido = [False, False,
                               False, False]
                rojo_muerto = False
                azul_muerto = False
                amarillo_muerto = False
                rosa_muerto = False
            else:
                game_over = True
                moving = False
                startup_counter = 0
        if powerup and player_circle.colliderect(FRosa.rect) and\
                fantasma_comido[2] and not FRosa.muerto:
            if vidas > 0:
                powerup = False
                cont_power = 0
                vidas -= 1
                startup_cont = 0
                player_x = 450
                player_y = 663
                direccion = 0
                direccion_comando = 0
                rojo_x = 56
                rojo_y = 58
                direccion_rojo = 0
                azul_x = 440
                azul_y = 388
                direccion_azul = 2
                rosa_x = 440
                rosa_y = 438
                direccion_rosa = 2
                amarillo_x = 440
                amarillo_y = 438
                direccion_amarillo = 2
                fantasma_comido = [False, False,
                               False, False]
                rojo_muerto = False
                azul_muerto = False
                amarillo_muerto = False
                rosa_muerto = False
            else:
                game_over = True
                moving = False
                startup_cont = 0
        if powerup and player_circle.colliderect(FAmarillo.rect) and\
                fantasma_comido[3] and not FAmarillo.muerto:
            if vidas > 0:
                powerup = False
                cont_power = 0
                vidas -= 1
                startup_cont = 0
                player_x = 450
                player_y = 663
                direccion = 0
                direccion_comando = 0
                rojo_x = 56
                rojo_y = 58
                direccion_rojo = 0
                azul_x = 440
                azul_y = 388
                direccion_azul = 2
                rosa_x = 440
                rosa_y = 438
                direccion_rosa = 2
                amarillo_x = 440
                amarillo_y = 438
                direccion_amarillo = 2
                fantasma_comido = [False, False,
                               False, False]
                rojo_muerto = False
                azul_muerto = False
                amarillo_muerto = False
                rosa_muerto = False
            else:
                game_over = True
                moving = False
                startup_counter = 0
        if powerup and player_circle.colliderect(FRojo.rect) and not\
                FRojo.muerto and not fantasma_comido[0]:
            rojo_muerto = True
            fantasma_comido[0] = True
            score += (2 ** fantasma_comido.count(True)) * 100
        if powerup and player_circle.colliderect(FAzul.rect) and not\
                FAzul.muerto and not fantasma_comido[1]:
            azul_muerto = True
            fantasma_comido[1] = True
            score += (2 ** fantasma_comido.count(True)) * 100
        if powerup and player_circle.colliderect(FRosa.rect) and not\
                FRosa.muerto and not fantasma_comido[2]:
            rosa_muerto = True
            fantasma_comido[2] = True
            score += (2 ** fantasma_comido.count(True)) * 100
        if powerup and player_circle.colliderect(FAmarillo.rect) and not\
                FAmarillo.muerto and not fantasma_comido[3]:
            amarillo_muerto = True
            fantasma_comido[3] = True
            score += (2 ** fantasma_comido.count(True)) * 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direccion_comando = 0
                if event.key == pygame.K_LEFT:
                    direccion_comando = 1
                if event.key == pygame.K_UP:
                    direccion_comando = 2
                if event.key == pygame.K_DOWN:
                    direccion_comando = 3
                if event.key == pygame.K_SPACE and\
                        (game_over or game_won):
                    powerup = False
                    cont_power = 0
                    vidas -= 1
                    startup_cont = 0
                    player_x = 450
                    player_y = 663
                    direccion = 0
                    direccion_comando = 0
                    rojo_x = 56
                    rojo_y = 58
                    direccion_rojo = 0
                    azul_x = 440
                    azul_y = 388
                    direccion_azul = 2
                    rosa_x = 440
                    rosa_y = 438
                    direccion_rosa = 2
                    amarillo_x = 440
                    amarillo_y = 438
                    direccion_amarillo = 2
                    fantasma_comido = [False, False,
                                   False, False]
                    rojo_muerto = False
                    azul_muerto = False
                    amarillo_muerto = False
                    rosa_muerto = False
                    score = 0
                    vidas = 3
                    nivel = copy.deepcopy(bordesitos)
                    game_over = False
                    game_won = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and\
                        direccion_comando == 0:
                    direccion_comando = direccion
                if event.key == pygame.K_LEFT and\
                        direccion_comando == 1:
                    direccion_comando = direccion
                if event.key == pygame.K_UP and\
                        direccion_comando == 2:
                    direccion_comando = direccion
                if event.key == pygame.K_DOWN and\
                        direccion_comando == 3:
                    direccion_comando = direccion

        if direccion_comando == 0 and giros_permitidos[0]:
            direccion = 0
        if direccion_comando == 1 and giros_permitidos[1]:
            direccion = 1
        if direccion_comando == 2 and giros_permitidos[2]:
            direccion = 2
        if direccion_comando == 3 and giros_permitidos[3]:
            direccion = 3

        if player_x > 900:
            player_x = -47
        elif player_x < -50:
            player_x = 897

        if FRojo.en_caja and rojo_muerto:
            rojo_muerto = False
        if FAzul.en_caja and azul_muerto:
            azul_muerto = False
        if FRosa.en_caja and rosa_muerto:
            rosa_muerto = False
        if FAmarillo.en_caja and amarillo_muerto:
            amarillo_muerto = False

        pygame.display.flip()
    pygame.quit()