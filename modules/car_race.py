import pygame
import random
import sys
import os
import global_variables
import Intefazsaturno


class Obstaculo(pygame.sprite.Sprite):
  def __init__(self, image, x, y):
    super().__init__()
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.speed = 10

  def update(self):
    self.rect.y += self.speed
    if self.rect.y> 800:
      self.rect.y =-100

class game_principal:
  def __init__(self):
    pygame.init()
    self.pantalla = pygame.display.set_mode((1080, 720))
    self.fps = 25
    self.reloj = pygame.time.Clock()
    self.carros = self.cargar_carros()
    self.carro = random.choice(self.carros)
    self.carro_rect = self.carro.get_rect()
    self.carro_rect.top = 500
    self.carro_rect.left = 220
    self.puntuacion = 0
    self.rojo = (255, 0, 0)
    self.tam = (5, 0, 180, 40)
    self.tam_punt = (230, 530 , 330, 40) 
    self.game_over_image = pygame.image.load("../retro-galaxy/src/sprites/Car-race/gamerover.png")
    self.Carriles = [260, 350, 435, 525]
    self.cont = 0
    self.velocidad = 0
    self.repitepista = 2
    self.mueve_pista = 0
    self.obstaculocont = 0
    self.obstaculomax = 3
    self.pistay = 0
    self.speed = 5
    self.largo = 100
    self.ancho = 10
    self.pistas = self.cargar_pistas()
    self.pista = random.choice(self.pistas)
    self.carretera = pygame.image.load('../retro-galaxy/src/backgrounds/Car-race/Carretera.png')
    self.obstaculos = pygame.sprite.Group()
    self.obstaculo_images = self.cargar_obstaculos()
    self.obst_posicion = [(220, -100), (330, -100), (410, -100), (505, -100)]
    self.tiempo_obstaculo = 4000
    self.fin = False
    self.running = True

  def cargar_carros(self):
    carros = []
    carros.append(pygame.image.load('../retro-galaxy/src/sprites/Car-race/Llamas1.png'))
    carros.append(pygame.image.load('../retro-galaxy/src/sprites/Car-race/car_pedro.png'))
    carros.append(pygame.image.load('../retro-galaxy/src/sprites/Car-race/car_bili.png'))
    carros.append(pygame.image.load('../retro-galaxy/src/sprites/Car-race/car_blue.png'))
    return carros

  def cargar_pistas(self):
    pistas = []
    pistas.append(pygame.image.load('../retro-galaxy/src/backgrounds/Car-race/Praderaprueba.png'))
    pistas.append(pygame.image.load('../retro-galaxy/src/backgrounds/Car-race/calor.png'))
    pistas.append(pygame.image.load('../retro-galaxy/src/backgrounds/Car-race/mar.png'))
    pistas.append(pygame.image.load('../retro-galaxy/src/backgrounds/Car-race/nieve.png'))
    return pistas

  def cargar_obstaculos(self):
    obstaculo_images = []
    obstaculo_images.append(pygame.image.load("../retro-galaxy/src/sprites/Car-race/Iguana.png"))
    obstaculo_images.append(pygame.image.load("../retro-galaxy/src/sprites/Car-race/Conorosado.png"))
    obstaculo_images.append(pygame.image.load("../retro-galaxy/src/sprites/Car-race/Charco.png"))
    return obstaculo_images

  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and self.cont> 0:
          self.cont -= 1
        elif event.key == pygame.K_RIGHT and self.cont<len(self.Carriles) - 1:
          self.cont += 1
        elif event.key == pygame.K_ESCAPE and self.fin == True:
              self.fin = False
              Intefazsaturno.saturno.cars.gstate = False

  def update_carro(self):
    self.carro_rect.centerx = self.Carriles[self.cont]
    self.carro_rect.top -= self.velocidad
    if self.carro_rect.top< 0:
      self.carro_rect.top = 0

  def dibujar_pista(self):
    if self.pista == self.pistas[0]:
      self.pantalla.blit(self.pistas[0], (0, 0))
    elif self.pista == self.pistas[1]:
      self.pantalla.blit(self.pistas[1], (0, 0))
    elif self.pista == self.pistas[2]:
      self.pantalla.blit(self.pistas[2], (0, 0))
    else:
      self.pantalla.blit(self.pistas[3], (0, 0))
    self.pistay += self.speed * 2
    if self.pistay>= self.largo * 2:
      self.pistay = 0
    for y in range(self.largo * -2, 800, self.largo * 2):
      self.pantalla.blit(self.carretera, (210, y + self.pistay, self.largo, self.ancho))

  def dibujar_carro(self):
    self.pantalla.blit(self.carro, self.carro_rect)

  def update_obstaculos(self):
    prox_obst = pygame.time.get_ticks()
    if prox_obst>self.tiempo_obstaculo:
      self.tiempo_obstaculo = prox_obst + 10000
      if self.obstaculocont<self.obstaculomax:
        obstaculo_type = random.randint(1, 3)
        x, y = random.choice(self.obst_posicion)
        if obstaculo_type == 1:
            self.obstaculos.add(Obstaculo(self.obstaculo_images[0], x, y))
        elif obstaculo_type == 2:
            self.obstaculos.add(Obstaculo(self.obstaculo_images[1], x, y))
        else:
            self.obstaculos.add(Obstaculo(self.obstaculo_images[2], x, y))
        self.obstaculocont += 1

  def detectar_colision(self):
    for obstaculo in self.obstaculos:
      if self.carro_rect.colliderect(obstaculo.rect):
        self.game_over()
      elif  obstaculo.rect.y > self.carro_rect.top:
        self.puntuacion += 1
          
  def game_over(self):
    self.running = False
    self.pantalla.blit(self.game_over_image, (120, 200))
    font = pygame.font.Font(None, 50)
    puntuaciontotal = font.render(f"Puntuación:{self.puntuacion}", 1, (255, 255, 255))
    punt_rect = puntuaciontotal.get_rect()
    punt_rect.centerx = 388
    punt_rect.centery = 550

    pygame.draw.rect(self.pantalla, self.rojo, self.tam_punt)
    self.pantalla.blit(puntuaciontotal, punt_rect)

    self.fin = True  
    pygame.display.flip()
    

  def run(self):
    
    while self.running and self.fin == False:
      
      global_variables.screen.fill((0,0,0))
      self.handle_events()
      self.update_carro()
      self.dibujar_pista()
      self.dibujar_carro()
      self.update_obstaculos()
      self.detectar_colision()
      self.obstaculos.update()
      self.obstaculos.draw(self.pantalla)
      font = pygame.font.Font(None, 36)
      text = font.render(f"Score: {self.puntuacion}", 1, (255, 255, 255))
      pygame.draw.rect(self.pantalla, self.rojo, self.tam)
      self.pantalla.blit(text, (12, 10))
      pygame.display.flip()
      self.reloj.tick(self.fps)

game = game_principal()





