from abc import ABC, abstractmethod
import random
import pygame, sys, time, random
import threading

from pygame import Color

roja = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/roja.png')
morada = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/Moradam.png')
amarilla = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/amarilla.png')
grande = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/grande.png')

class Manzana(ABC):

    def __init__(self):
       self.x = random.randint(0,49)*10
       self.y = random.randint(0,49)*10
       self.color = roja
       self.tamaño = 0



    @abstractmethod
    def efecto(self):
        pass

   
    def setTamaño(self, t):
       self.tamaño=t

    def getTamaño (self):
       return self.tamaño  

    def setColor(self,color):
       self.color = color

    def getColor(self):
       return self.color
    
    def setPos(self,pos):
       self.pos = pos

    def getPos(self):
    
     return self.pos


class ComidaMulti(Manzana):
    def __init__(self):
     super().__init__()
     super().setColor(amarilla)
     super().setTamaño(20)
     
    def getTamaño(self):
        return super().getTamaño()

    def getColor(self):
       return super().getColor()
    
    def efecto(self):
        posicion = random.randint(0,78)*10
        posicion2 = random.randint(0,58)*10
        comida_pos = [[posicion,posicion2]]
        comida_pos2 = [posicion,posicion2]
        
        i=0
        while len(comida_pos)!=5:
           posicion = random.randint(0,78)*10
           posicion2 = random.randint(0,58)*10
           comida_pos2 = [posicion,posicion2]

           comida_pos.insert(0,comida_pos2)
           i=i+1
           
        return comida_pos
    
    

class ComidaNormal(Manzana):
    def __init__(self):
     super().__init__()
     super().setColor(roja)
     super().setTamaño(20)

    def getTamaño(self):
        return super().getTamaño()

    def getColor(self):
       return super().getColor()
         
    
    def efecto(self):      
      posicion = random.randint(0,78)*10
      posicion2 = random.randint(0,58)*10
      comida_pos = [[posicion,posicion2]]
      
      return comida_pos
 


class ComidaGrande(Manzana):
    def __init__(self):
     super().__init__()
     super().setColor(morada)
     super().setTamaño(20)
    
    
    def getColor(self):
       return super().getColor()
    
    
    def getTamaño(self):
       return super().getTamaño()
    
    
    
    def efecto(self):
      posicion = random.randint(0,78)*10
      posicion2 = random.randint(0,58)*10
      comida_pos = [[posicion,posicion2]]
      
      return comida_pos



#color = Color((255,165,0))
#comidita = ComidaNormal(color,pos=1)
#comidita.efecto()
   