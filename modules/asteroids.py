from global_variables import *
import global_variables as gv
import math 
import random

pygame.init()

alto= 1080
ancho= 720

fondo_juego= pygame.image.load('../retro-galaxy/src/backgrounds/bg-asteroids.jpg')
jugador=pygame.image.load('../retro-galaxy/src/sprites/Asteroids/jugador.png')
asteroide_grande=pygame.image.load('../retro-galaxy/src/sprites/Asteroids/asteroidegrande.png')
asteroide_mediano=pygame.image.load('../retro-galaxy/src/sprites/Asteroids/asteroidemediano.png')
asteroide_mediano2=pygame.image.load('../retro-galaxy/src/sprites/Asteroids/asteroidemediano2.png')
asteroide_peqmed=pygame.image.load('../retro-galaxy/src/sprites/Asteroids/asteroidepeqmed.png')
asteroide_peq=pygame.image.load('../retro-galaxy/src/sprites/Asteroids/asteroidepeq.png')
estrella=pygame.image.load('../retro-galaxy/src/sprites/Asteroids/estrella.png')


fps=pygame.time.Clock()

finalizar= False
comenzar= True
vidas= 3
puntuacion= 0
puntuacion2=0

sonido_On= True
record= 0


rapidFire = False
rfStart = -1 

disparar = pygame.mixer.Sound('../retro-galaxy/src/sounds/Asteroids/fire.wav')
sonido_gran_impacto = pygame.mixer.Sound('../retro-galaxy/src/sounds/Asteroids/bangLarge.wav')
sonido_pequeño_impacto = pygame.mixer.Sound('../retro-galaxy/src/sounds/Asteroids/bangSmall.wav')
disparar.set_volume(.25)
sonido_gran_impacto.set_volume(.25)
sonido_pequeño_impacto.set_volume(.25)

def Pantalla_Juego():
    screen.blit(fondo_juego,(0,0)) 
    fuente= pygame.font.SysFont('arial', 30)
    textoV= fuente.render('Vidas: ' + str(vidas), 1, (255,255,255))
    jugar_otra_vez= fuente.render('Pulsa Tab para jugar otra vez', 1, (255,255,255))
    puntaje= fuente.render('Puntuacion: ' + str(puntuacion), 1, (255,255,255))
    Record= fuente.render('Record: ' + str(record), 1, (255,255,255))
    Pausa= fuente.render('PAUSA (presiona Tab para reanudar)', 1, (255,255,255))
    Comenzar= fuente.render('Pulsa Enter para jugar', 1, (255,255,255))
    
    jugador.dib(screen )

        
    for b in disparoJugador:
        b.dib(screen )
    
    for a in asteroides:
        a.dib(screen )
        
    for s in estrellas: 
        s.dib(screen )
        
    if rapidFire:
        pygame.draw.rect(screen , (0, 0, 0), [ancho //2 - 51, 19, 102, 22])
        pygame.draw.rect(screen , (255, 255, 255), [ancho//2 - 50, 20, 100 - 100*(cont - rfStart)/500, 20])
    
    if comenzar:
        screen.blit(Comenzar,(alto//2 - Comenzar.get_width()//2, ancho//2 - Comenzar.get_height()//2))
    if finalizar and vidas!=0:
        screen.blit(Pausa,(alto//2 - Pausa.get_width()//2, ancho//2 - Pausa.get_height()//2))    
    if finalizar and vidas==0:
       screen.blit(jugar_otra_vez, (alto//2 - jugar_otra_vez.get_width()//2, ancho//2 - jugar_otra_vez.get_height()//2))    
    if not comenzar:
        screen.blit(puntaje, (alto - puntaje.get_width() - 25, 25))
        screen.blit(textoV, (25,25)) 
        screen.blit(Record, (ancho - Record.get_width() +25, 35 + puntaje.get_height()))   
    
    pygame.display.update()


class Jugador(object):
    def __init__(self):
        self.img= jugador
        self.w= self.img.get_width()
        self.h= self.img.get_height()
        self.x= alto//2
        self.y= ancho//2
        self.angulo= 0
        self.rotacion= pygame.transform.rotate(self.img, self.angulo)
        self.rotado= self.rotacion.get_rect()
        self.rotado.center= (self.x,self.y)
        self.coseno = math.cos(math.radians(self.angulo+90))
        self.seno = math.sin(math.radians(self.angulo+90))
        self.head=(self.x+self.coseno*self.w//2, self.y-self.seno*self.h//2)
        
    def dib(self, screen ):
        screen.blit(self.rotacion, self.rotado)

    def girarIzq(self):
        self.angulo+=5
        self.rotacion=pygame.transform.rotate(self.img,self.angulo)
        self.rotado=self.rotacion.get_rect()
        self.rotado.center=(self.x,self.y)
        self.coseno = math.cos(math.radians(self.angulo+90))
        self.seno = math.sin(math.radians(self.angulo+90))
        self.head=(self.x+self.coseno*self.w//2, self.y-self.seno*self.h//2)
        
    
    def girarDer(self):
        self.angulo-=5
        self.rotacion=pygame.transform.rotate(self.img,self.angulo)
        self.rotado=self.rotacion.get_rect()
        self.rotado.center=(self.x,self.y)
        self.coseno = math.cos(math.radians(self.angulo+90))
        self.seno = math.sin(math.radians(self.angulo+90))
        self.head=(self.x+self.coseno*self.w//2, self.y-self.seno*self.h//2)
    
    def MoverAdelante(self):
        self.x +=self.coseno* 6
        self.y -= self.seno*6
        self.rotacion=pygame.transform.rotate(self.img,self.angulo)
        self.rotado=self.rotacion.get_rect()
        self.rotado.center=(self.x,self.y)
        self.coseno = math.cos(math.radians(self.angulo+90))
        self.seno = math.sin(math.radians(self.angulo+90))
        self.head=(self.x+self.coseno*self.w//2, self.y-self.seno*self.h//2)
        
    def updatedLocation(self):
        if self.x > alto+50:
            self.x= 0
        elif self.x < 0 - self.w:
            self.x= alto
        elif self.y < -50:
            self.y= ancho
        elif self.y > ancho+50:
            self.y= 0
            

class disparo(object):
    def __init__(self):
        self.punto= jugador.head
        self.x, self.y= self.punto
        self.w= 4
        self.h= 4
        self.coseno= jugador.coseno
        self.seno= jugador.seno
        self.xv= self.coseno*10
        self.yv= self.seno*10
    
    def move(self):
        self.x += self.xv
        self.y -= self.yv
        
    def dib(self, screen ):
        pygame.draw.rect(screen , (255,255,255), [self.x, self.y, self.w, self.h]) 
        
    def checkOffScreen(self):
        if self.x < -50 or self.x > alto or self.y > ancho or self.y < -50:
            return True

class asteroide(object):
    def __init__(self,rank):
        self.rank=rank
        if self.rank==1:
            self.img=asteroide_peq
        elif self.rank==2:
            self.img=asteroide_peqmed
        elif self.rank==3:  
            self.img=asteroide_mediano2
        elif self.rank==4:
            self.img=asteroide_mediano
        else: 
            self.img=asteroide_grande
        
        self.w= 50 * rank
        self.h= 50 * rank 
        self.puntos = random.choice([(random.randrange(0, ancho - self.w), random.choice([-1 * self.h - 5, alto + 5])),(random.choice([-1 * self.w - 5, ancho + 5]), random.randrange(0, alto - self.h))])
        self.x,self.y=self.puntos 
        if self.x < ancho//2: 
            self.xdir=1
        else:
            self.xdir=-1
        if self.y<alto//2:
            self.ydir=1
        else: 
            self.ydir=-1
        self.xv=self.xdir* random.randrange(1,3)
        self.yv=self.ydir* random.randrange(1,3)

    def dib(self,screen ):
        screen.blit(self.img,(self.x,self.y))
        
#Parte 1 de avance 3     
class Estrella(object):
    def __init__(self):
        self.img = estrella
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.aparicion = random.choice([(random.randrange(0, ancho - self.w), random.choice([-1 * self.h - 5, alto + 5])),(random.choice([-1 * self.w - 5, ancho + 5]), random.randrange(0, alto - self.h))])
        self.x, self.y = self.aparicion
        if self.x < ancho//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < alto//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2

    def dib(self, screen ):
        screen.blit(self.img, (self.x, self.y))

    

            


jugador=Jugador()
disparoJugador= [] 
asteroides=[]
estrellas=[]
cont=0
p=0

def asteroids():
    global disparoJugador, asteroides, estrellas, cont, p,comenzar, finalizar, puntuacion2, puntuacion, vidas,rfStart, rapidFire, sonido_On, record 
    while comenzar:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    comenzar= False      
                     
        Pantalla_Juego()
            
    
    fps.tick(35)
    cont+=1
    if not finalizar:
        if cont % 50 == 0 :
            ran=random.choice([1,1,1,1,2,2,2,3,3,4,5])
            asteroides.append(asteroide(ran))
        if cont % 1000 == 0:
            estrellas.append(Estrella())
        jugador.updatedLocation()
        
        
        for b in disparoJugador:
            b.move()
            if b.checkOffScreen():
                disparoJugador.pop(disparoJugador.index(b))
        
        for a in asteroides:
            a.x+=a.xv
            a.y+=a.yv
            
            if(jugador.x >= a.x and jugador.x <= a.x + a.w) or (jugador.x + jugador.w >= a.x and jugador.x + jugador.w <= a.x + a.w):
                if(jugador.y >= a.y and jugador.y <= a.y + a.h) or (jugador.y + jugador.h >= a.y and jugador.y + jugador.h <= a.y + a.h):
                    vidas -= 1
                    asteroides.pop(asteroides.index(a))
                    if sonido_On:
                        sonido_gran_impacto.play()
                    break
        
            for b in disparoJugador:
                if (b.x >= a.x and b.x <= a.x + a.w )or (b.x + b.w >= a.x and b.x + b.w <= a.x + a.w):
                    if(b.y>=a.y and b.y <= a.y+a.h)or (b.y + b.h >= a.y and b.y + b.h <= a.y+ a.y): 
                        if a.rank==5:
                            if sonido_On:
                                sonido_gran_impacto.play()
                            puntuacion +=10
                            puntuacion2+=10
                            na1=asteroide(4)
                            na2=asteroide(4)
                            na1.x=a.x
                            na2.x=a.x
                            na1.y=a.y
                            na2.y=a.y
                            asteroides.append(na1)
                            asteroides.append(na2)
                         
                        if a.rank==4:
                            if sonido_On:
                               sonido_gran_impacto.play()
                            puntuacion +=20
                            puntuacion2+=20
                            na1=asteroide(3)
                            na2=asteroide(3)
                            na1.x=a.x
                            na2.x=a.x
                            na1.y=a.y
                            na2.y=a.y
                            asteroides.append(na1)
                            asteroides.append(na2)
                       
                            
                        if a.rank==3:
                            if sonido_On:
                                sonido_gran_impacto.play()
                            puntuacion +=30
                            puntuacion2+=30
                            na1=asteroide(2)
                            na2=asteroide(2)
                            na1.x=a.x
                            na2.x=a.x
                            na1.y=a.y
                            na2.y=a.y
                            asteroides.append(na1)
                            asteroides.append(na2)
                        
                        if a.rank==2:
                            if sonido_On:
                                sonido_pequeño_impacto.play()
                            puntuacion +=40
                            puntuacion2+=40
                            na1=asteroide(1)
                            na2=asteroide(1)
                            na1.x=a.x
                            na2.x=a.x
                            na1.y=a.y
                            na2.y=a.y
                            asteroides.append(na1)
                            asteroides.append(na2)
                           
                        else:
                            puntuacion+=50
                            puntuacion2+=50
                            if sonido_On:
                                sonido_pequeño_impacto.play()
                             
                        asteroides.pop(asteroides.index(a))
                        disparoJugador.pop(disparoJugador.index(b))
                        break
                        
                    
        for s in estrellas:
            s.x += s.xv
            s.y += s.yv
            if s.x < -100 - s.w or s.x > ancho + 100 or s.y > alto + 100 or s.y < -100 - s.h:
                estrellas.pop(estrellas.index(s))
                break
            for b in disparoJugador:
                if (b.x >= s.x and b.x <= s.x + s.w) or b.x + b.w >= s.x and b.x + b.w <= s.x + s.w:
                    if (b.y >= s.y and b.y <= s.y + s.h) or b.y + b.h >= s.y and b.y + b.h <= s.y + s.h:
                        rapidFire = True
                        rfStart = cont
                        estrellas.pop(estrellas.index(s))
                        disparoJugador.pop(disparoJugador.index(b))
                        break            
        if puntuacion2>=10000:
            vidas+=1
            puntuacion2=0                
        if vidas <= 0:
            finalizar= True
        
        if rfStart != -1:
            if cont - rfStart > 500:
                rapidFire = False
                rfStart = -1
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            jugador.girarIzq()
        if keys[pygame.K_RIGHT]:
            jugador.girarDer()
        if keys[pygame.K_UP]:
            jugador.MoverAdelante()
        if keys[pygame.K_SPACE]:
            if rapidFire:
                disparoJugador.append(disparo())
                if sonido_On:
                    disparar.play()  
                  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ejecutar=False   
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                p=1
                finalizar= True
                
                
            if event.key ==pygame.K_SPACE:
                if not finalizar:
                    if not rapidFire:
                        disparoJugador.append(disparo())
                        if sonido_On:
                            disparar.play()
                                
            if event.key == pygame.K_m:
                sonido_On = not sonido_On
            if p==1:
                if event.key==pygame.K_TAB:
                    p=0
                    finalizar= False
            if event.key == pygame.K_TAB:
                if finalizar:
                    finalizar= False
                    vidas= 3
                    asteroides.clear()
                    if puntuacion > record:
                        record= puntuacion
                    puntuacion= 0
                       
    Pantalla_Juego()         

while gv.running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gv.unning = False
    
    asteroids()
    
    pygame.display.update()