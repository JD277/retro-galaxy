import pygame, sys, time, random
import threading
from Manzana import *
import time

display = pygame.display.set_mode((800,600))
fuente = pygame.font.Font(None, 30)
fuenteOver = pygame.font.Font(None, 50)
fps = pygame.time.Clock()
sound_fondo = pygame.mixer.Sound("../retro-galaxy/src/sounds/Planet_Snake/sonido_fondo.mp3")
sound_comer = pygame.mixer.Sound("../retro-galaxy/src/sounds/Planet_Snake/comer.mp3")
sound_gameover = pygame.mixer.Sound("../retro-galaxy/src/sounds/Planet_Snake/game_over.mp3")
sound_powerup = pygame.mixer.Sound("../retro-galaxy/src/sounds/Planet_Snake/powerup.mp3")
cola= pygame.image.load("../retro-galaxy/src/sprites/Planet_Snake/img/cola.png")
fondo = pygame.image.load('../retro-galaxy/src/backgrounds/PSnake/fondo2.jpg')
fondo = pygame.transform.scale(fondo, (1080, 720))
grande = pygame.image.load('../retro-galaxy/src/sprites/Planet_Snake/img/grande.png')
   
manzana = ComidaNormal()

rojo = manzana.getColor()
      

def comida():
   posicion2 = random.randint(0,59)*10
   posicion = random.randint(0,79)*10
   comida_pos = [posicion, posicion2]  
   return comida_pos


def regresar_Manzana():
    r=random.randint(0,10)
    if r > 6:
       manzana=ComidaNormal()
       return manzana
    
    if r > 3 and r <=6:
       manzana=ComidaMulti()
       return manzana

    if r <= 3:
       manzana = ComidaGrande()
       return manzana

     

def main():
    
    time.sleep(1.5)
    
    snake_pos = [100,50]
    snake_cuerp = [[100,50],[90,50],[80,50]]
  
    change = "RIGTH"
    run = True
    comida_pos = manzana.efecto()
    puntos = 0
    last_time = time.time()
    current_time=0
    cantidadM = len(comida_pos)
    m=regresar_Manzana()
    color=m.getColor()
    s=True
    t=15
    c = 0
    r2=display.blit(color,(1,1,1,1))
    sound_fondo.set_volume(0.60)
    sound_gameover.set_volume(0.15)
    sound_fondo.play(5)

    while run:
        pygame.display.flip()    
       
                    
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                current_time=time.time()-last_time
                if current_time>0.00000001:
                              
                 if event.key == pygame.K_RIGHT and change != "LEFT":      
                    change = "RIGTH"
                    current_time=0
                    last_time=time.time()

                   
                 if event.key == pygame.K_LEFT and change != "RIGTH":                    
                    change = "LEFT"  
                    current_time=0
                    last_time=time.time()

                                     
                 if event.key == pygame.K_UP and change != "DOWN":                       
                    change = "UP"                     
                    current_time=0
                    last_time=time.time()

                    
                 if event.key == pygame.K_DOWN and change != "UP":                                    
                    change = "DOWN"
                    current_time=0
                    last_time=time.time()

                            
                    
        if change == "RIGTH":
            snake_pos[0] += 10
                    
        if change == "LEFT":
            snake_pos[0] -= 10
                
        if change == "UP":
            snake_pos[1] -= 10
                       
        if change == "DOWN":
            snake_pos[1] += 10
            
           
        snake_cuerp.insert(0, list(snake_pos))
         
        if cantidadM == 1 and s == True:
             if c !=2:
              m=ComidaNormal()
              color = m.getColor()
              c=c+1
             else:
              m=regresar_Manzana()
              color = m.getColor()
              c=0
             
             s=False       
       
        
        r1 = display.blit(color,(snake_pos[0],snake_pos[1],t,t))
                  
                        
        if  snake_pos in comida_pos[0:] or cantidadM == 0 or pygame.Rect.colliderect(r1,r2) :
            s=True
                         
            if cantidadM == 0:
             t=m.getTamaño()
             comida_pos = m.efecto()     
             
            else:
             
             i=0
             for cos in comida_pos :
                  r1 = display.blit(color,(snake_pos[0],snake_pos[1],t,t))
                  r2= display.blit(color,(cos[0],cos[1],t,t))
                  
                  
                  if cos == snake_pos or  pygame.Rect.colliderect(r1,r2):
                
                     comida_pos.pop(i)
                     puntos += 100
                     sound_comer.play()

                  else:
                     i=i+1  
                   
        else:  
            snake_cuerp.pop() 
        
        
        cantidadM = len(comida_pos)
        l = len(comida_pos)
         
       
           
        if cantidadM > 1 :
           color = rojo
        
        display.blit(fondo,(0,0))
        
        for pos in snake_cuerp:
         
         display.blit(cola,(pos[0],pos[1],15,15))
         text = fuente.render(str(puntos),0,(200,200,200)) 
         display.blit(text, (20,20))
          

        for Cpos in comida_pos: 
         display.blit(color,(Cpos[0],Cpos[1],t,t))
         r2=display.blit(color,(Cpos[0],Cpos[1],t,t))

                   
        pygame.display.flip()
    
        fps.tick(15)
              
            
        if snake_pos[0] <= 0 or snake_pos[0] >= 800:
            run = False
            text = fuenteOver.render(str("GAME OVER"),0,(200,200,200))
            text2 = fuente.render(str("X Para continuar"),0,(200,200,200))
            display.blit(text, (300,50))
            display.blit(text2,(320,380))
            sound_gameover.play()
            sound_fondo.stop()
        if snake_pos[1] <= 0 or snake_pos[1] >= 600:
            run = False
            text = fuenteOver.render(str("GAME OVER"),0,(200,200,200))
            text2 = fuente.render(str("X Para continuar"),0,(200,200,200))
            display.blit(text, (300,50))
            display.blit(text2,(320,380))
            sound_gameover.play()
            sound_fondo.stop()
            

        pygame.display.flip()    
     
                
        if snake_pos in snake_cuerp [1:]:       
            run = False
            text = fuenteOver.render(str("GAME OVER"),0,(200,200,200))
            text2 = fuente.render(str("X Para continuar"),0,(200,200,200))
            display.blit(text, (300,50))
            display.blit(text2,(320,350))
            sound_gameover.play()
            sound_fondo.stop()
            
            pygame.display.flip()
            
         
        
        
                
        
    
    