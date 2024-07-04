from global_variables import *
import pygame, random, time, sys
import pygame.mixer


pygame.init()


# definicion de colores
black = (0, 0, 0)
white = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)

# parametros de pantalla
ancho = 1080
alto = 400
anchura= 110
altura= 110
anchura2= 150
altura2= 150

# Sonidos
sonido_pong = pygame.mixer.Sound("../retro-galaxy/src/sounds/Mars_Breaker/spong.wav")
canal_pong = pygame.mixer.Channel(0)
sonido1 = pygame.mixer.Sound("../retro-galaxy/src/sounds/Mars_Breaker/sonido1.wav")
canal_sonido1 = pygame.mixer.Channel(1)
sonido2 = pygame.mixer.Sound('../retro-galaxy/src/sounds/Mars_Breaker/sonido2.wav')
canal_sonido2 = pygame.mixer.Channel(2)

# Imagenes
fondo = pygame.image.load('../retro-galaxy/src/backgrounds/MBreaker/fondoIG.jpeg')
fondo = pygame.transform.scale(fondo, (1080, 720))
fondo2 = pygame.image.load('../retro-galaxy/src/backgrounds/MBreaker/fondo4.jpeg')
fondo2 = pygame.transform.scale(fondo2, (1080, 720))
interfaz = pygame.image.load('../retro-galaxy/src/backgrounds/MBreaker/OIG4.jpeg')
interfaz = pygame.transform.scale(interfaz, (1080, 720))
textura = pygame.image.load('../retro-galaxy/src/sprites/Mars/textura.jpg')
textura = pygame.transform.scale(textura, (80, 40))
button_img = pygame.image.load('../retro-galaxy/src/buttons/boto1.png')
button_img2 = pygame.transform.scale(button_img, (anchura,altura))
button_img3=pygame.transform.scale(button_img, (anchura2,altura2))
wasd = pygame.image.load('../retro-galaxy/src/sprites/Mars/wasd.png')
wasd = pygame.transform.scale(wasd, (300, 300))
flechas = pygame.image.load('../retro-galaxy/src/sprites/Mars/flechitas.png')
flechas = pygame.transform.scale(flechas, (250,200))

# Reloj
timer = pygame.time.Clock()
fps = 60

# fuente y textos
fuente = pygame.font.Font('freesansbold.ttf', 40)
fuente2 = pygame.font.Font('freesansbold.ttf', 30)
fuente3 = pygame.font.Font('freesansbold.ttf', 20)
fuente4 = pygame.font.Font('freesansbold.ttf', 18)
fuente5 = pygame.font.Font('freesansbold.ttf', 13)
texto = fuente.render("Game Over!", 0, white)
texto2 = fuente.render("Mars Breaker", 0, white)  
texto3 = fuente3.render("Iniciar", 0, white) 
texto4 = fuente3.render("Salir", 0, white) 
texto5 = fuente4.render("Reiniciar", 0, white)  
texto6 = fuente2.render("Seleccione un modo de juego", 0, white) 
texto7 = fuente4.render("Infinito", 0,white) 
texto8 = fuente4.render("Dos jugadores", 0, white)  
texto9 = fuente5.render("Cambiar modo", 0, white) 
texto10 = fuente2.render("Control jugador 1", 0, white)
texto11 = fuente2.render("Control jugador 2", 0, white)

# Variables globales
velocidad_paleta = 5
tamaño_bloque = (75, 30)



# Definicion de clases

class Iniciar:
    def __init__(self):
        self.rect =  pygame.Rect(500, 200, 85, 50)
                                
    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                canal_sonido2.stop()
                return False


    def dibujar(self):
        screen.blit(button_img2, (478,151))


    def sonidojuego(self):
        canal_sonido1.play(sonido1)


class Salir(Iniciar):
    def __init__(self, x, y, a, l):
        super().__init__()
        self.rect = pygame.Rect(x, y, a, l)

    def volver(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True

    def dibujar(self):
        screen.blit(button_img2, (478,300))


class Reiniciar:
    def __init__(self):
        self.rect = pygame.Rect(490, 135, 340, 50)

    def reinicia(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True

    def dibujar(self):
        screen.blit(button_img2, (475,90))


class Paleta:
    def __init__(self, x, y, a, l):
        self.rect = pygame.Rect(x, y, a, l)

    def mover(self, direccion, modo, teclas):
        if modo == 1:
            velocidad = 3
            if direccion == "izquierda" and self.rect.left > 0:
                self.rect.x -= velocidad
            if direccion == "derecha" and self.rect.right < ancho:
                self.rect.x += velocidad
        elif modo == 2:
            if direccion == "izquierda" and self.rect.left > 0:
                self.rect.x -= velocidad_paleta
            if direccion == "derecha" and self.rect.right < ancho // 2 or direccion == "derecha" and teclas[pygame.K_RIGHT]:
                self.rect.x += velocidad_paleta
            if direccion == "arriba" and self.rect.top > 0:
                self.rect.y -= velocidad_paleta
            if direccion == "abajo" and self.rect.bottom < alto:
                self.rect.y += velocidad_paleta

    def dibujar(self):
        pygame.draw.rect(screen, white, self.rect)


class Bola:
    def __init__(self, velocidad):
        self.rect = pygame.Rect(ancho // 2 - 10, alto // 2 - 10, 20, 20)
        self.velocidad = velocidad
        self.score = 0
        self.score2 = 0

    def mover(self, modo):
        self.rect.x += self.velocidad[0]
        self.rect.y += self.velocidad[1]

        if modo == 1:
            if self.rect.left <= 0 or self.rect.right >= ancho:
                self.velocidad[0] = -self.velocidad[0]
            if self.rect.top <= 0:
                self.velocidad[1] = -self.velocidad[1]
        else:
            if self.rect.left <= 0:
                self.reinicia()
                self.score2 += 1

            elif self.rect.right >= ancho:
                self.reinicia()
                self.score += 1

            if self.rect.top <= 0:
                self.velocidad[1] = -self.velocidad[1]

            if self.rect.bottom >= alto:
                self.velocidad[1] = -self.velocidad[1]

    def reinicia(self):
        time.sleep(0.2)
        self.rect = pygame.Rect(ancho // 2 - 10, alto // 2 - 10, 20, 20)
        self.velocidad = [5, -5]
        if (random.randint(1, 2) == 1):
            self.velocidad[0] *= -1
            self.velocidad[1] *= -1

    def dibujar(self):
        pygame.draw.ellipse(screen, white, self.rect)

    def colision_paleta(self, paleta, paleta2):
        if self.rect.colliderect(paleta.rect):
            self.velocidad[1] *= -1
            self.velocidad[0] *= -1
            self.velocidad[1] += 1
            self.velocidad[0] += 1
            canal_pong.play(sonido_pong)

        elif self.rect.colliderect(paleta2.rect):
            self.velocidad[1] *= -1
            self.velocidad[0] *= -1
            self.velocidad[1] -= 1
            self.velocidad[0] -= 1
            canal_pong.play(sonido_pong)

    def colision_paleta1(self, paleta):
        if self.rect.colliderect(paleta.rect):
            canal_pong.play(sonido_pong)
            self.velocidad[1] = -self.velocidad[1]

    def colision_bloque(self, bloque):
        if self.rect.colliderect(bloque.rect):
            self.velocidad[1] = -self.velocidad[1]
            return True
        return False


class Bloque:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, tamaño_bloque[0], tamaño_bloque[1])

    def dibujar(self):
        pygame.draw.rect(screen, azul, self.rect)
        screen.blit(textura, self.rect)


class Modo1:
    def __init__(self):
        self.rect = pygame.Rect(350, 190, 60, 50)

    def selector(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True

    def dibujar(self):
        screen.blit(button_img2, (325,140))


class Modo2(Modo1):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(700, 190, 130, 60)

    def dibujar(self):
        screen.blit(button_img3, (688, 120))


# Definicion de funciones

def agregar_bloques(fila, cantidad_bloques):
    bloques = []
    espacios = ancho // tamaño_bloque[0]
    posiciones = random.sample(range(espacios), cantidad_bloques)

    for pos in posiciones:
        x = pos * tamaño_bloque[0]
        y = fila * tamaño_bloque[1]
        bloques.append(Bloque(x, y))
    return bloques


def pantallainicial(boton1, boton2):
    screen.blit(interfaz, (0, 0))
    screen.blit(texto2, (400, 0))
    boton1.dibujar()
    boton2.dibujar()
    screen.blit(texto3, (boton1))
    screen.blit(texto4, (boton2))
    mostrarL()
    pygame.display.flip()

def pantallaseleccion(boton4, boton5):
    screen.blit(interfaz, (0, 0))
    screen.blit(texto6, ((350), 0))
    boton4.dibujar()
    boton5.dibujar()
    screen.blit(texto7, (boton4))
    screen.blit(texto8, (boton5))
    mostrarL()
    pygame.display.flip()

def mostrarL():
    pygame.draw.line(screen, 'white',(0,430),(1080,430),5)
    screen.blit(wasd,(250, 400))
    screen.blit(flechas, (740, 450))
    screen.blit(texto10, (50, 450))
    screen.blit(texto11, (550, 450))
    pygame.display.flip()



# Instancia de objetos
paleta = Paleta((ancho // 40 - 15), (alto // 20 - 10), 20, 80)
paleta2 = Paleta((ancho - 30), (alto // 20 - 10), 20, 80)
bola = Bola([5, -5])
bola2 = Bola([2, -2])
paleta3 = Paleta(ancho // 2 - 50, alto - 50, 100, 10)
boton1 = Iniciar()
boton2 = Salir(505, 350, 85, 50)
boton3 = Reiniciar()
boton4 = Modo1()
boton5 = Modo2()
boton6 = Salir(480, 350, 85, 50)

# Variables de control
inicio = True
reinicio = False
salida = True
modoI = False
modoD = False
bloques = []
jugar = True
fase = True
finalizar = False

def juego():
    global paleta, paleta2, paleta3, bola, bola2, bloques,boton4,boton5, inicio, reinicio, salida, modoD, modoI,jugar, fase

    
    canal_sonido2.play(sonido2)
    while jugar:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finalizar = True
                jugar = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fase:
                    inicia = boton1.click(event)
                    salida = boton2.click(event)
                    if inicia == False:
                        boton1.sonidojuego()
                        fase = False
                    if salida == False:
                        finalizar = True
                        jugar = False
                if inicio:
                    modoI = boton4.selector(event)
                    modoD = boton5.selector(event)
                    if modoD == True or modoI == True:
                        inicio = False
        
        # Control de pantalla inicial
        if fase:
            pantallainicial(boton1, boton2)
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_ESCAPE] and inicio == False:
                finalizar = True
                jugar = False

            # Control de seleccion de modo
        elif inicio:
            pantallaseleccion(boton4,boton5)
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_ESCAPE]:
                fase = True
            

        else:
            # Modo infinito
            if modoI == True:
                screen.blit(fondo2, (0, 0))
                teclas = pygame.key.get_pressed()
                if teclas[pygame.K_LEFT]:
                    paleta3.mover('izquierda', 1, teclas)
                if teclas[pygame.K_a]:
                    paleta3.mover('izquierda', 1, teclas)  
                if teclas[pygame.K_RIGHT]:
                    paleta3.mover('derecha', 1, teclas)
                if teclas[pygame.K_d]:
                    paleta3.mover('derecha',1, teclas)
                if teclas[pygame.K_ESCAPE]:
                    fase = True
                    inicio = True
                    paleta3 = Paleta(ancho // 2 - 50, alto - 50, 100, 10)
                    bola2 = Bola([2, -2])
                    bloques = []
                    bloques = [bloque for bloque in bloques if not bola2.colision_bloque(bloque)]
                    if not bloques:
                        cantidad_bloques = random.randint(5, 10)
                        bloques = agregar_bloques(0, cantidad_bloques)

                bola2.mover(1)
                bola2.colision_paleta1(paleta3)

                bloques = [bloque for bloque in bloques if not bola2.colision_bloque(bloque)]

                if not bloques:
                    cantidad_bloques = random.randint(5, 10)
                    bloques = agregar_bloques(0, cantidad_bloques)
                

                if bola2.rect.bottom >= alto:
                    boton6.dibujar()
                    boton3.dibujar()
                    screen.blit(texto5, (boton3))
                    screen.blit(texto9, (boton6))
                    bola2.velocidad[0] = 0
                    bola2.velocidad[1] = 0
                    screen.blit(texto, (400, 50))
                    reinicio = boton3.reinicia(event)
                    menu = boton6.volver(event)
                    canal_sonido1.play(sonido1)

                    if reinicio == True:
                        paleta3 = Paleta(ancho // 2 - 50, alto - 50, 100, 10)
                        bola2 = Bola([2, -2])
                        bloques = []
                        bloques = [bloque for bloque in bloques if not bola2.colision_bloque(bloque)]
                        if not bloques:
                            cantidad_bloques = random.randint(5, 10)
                            bloques = agregar_bloques(0, cantidad_bloques)
                    elif menu == True:
                        inicio = True
                        paleta3 = Paleta(ancho // 2 - 50, alto - 50, 100, 10)
                        bola2 = Bola([2, -2])
                        bloques = []
                        bloques = [bloque for bloque in bloques if not bola2.colision_bloque(bloque)]
                        if not bloques:
                            cantidad_bloques = random.randint(5, 10)
                            bloques = agregar_bloques(0, cantidad_bloques)

                paleta3.dibujar()
                bola2.dibujar()
                pygame.draw.line(screen, 'white',(0,430),(1080,430),5)
                screen.blit(wasd,(250, 400))
                screen.blit(flechas, (740, 450))
                screen.blit(texto10, (50, 450))
                screen.blit(texto11, (550, 450))
                for bloque in bloques:
                    bloque.dibujar()

            # Modo de dos jugadores
            if modoD == True:
                timer.tick(fps)
                screen.blit(fondo, (0, 0))
                teclas = pygame.key.get_pressed()
                if teclas[pygame.K_a]:
                    paleta.mover("izquierda", 2, teclas)
                if teclas[pygame.K_d]:
                    paleta.mover("derecha", 2, teclas)
                if teclas[pygame.K_w]:
                    paleta.mover("arriba", 2, teclas)
                if teclas[pygame.K_s]:
                    paleta.mover("abajo", 2, teclas)
                if teclas[pygame.K_LEFT]:
                    paleta2.mover("izquierda", 2, teclas)
                if teclas[pygame.K_RIGHT]:
                    paleta2.mover("derecha", 2, teclas)
                if teclas[pygame.K_UP]:
                    paleta2.mover("arriba", 2, teclas)
                if teclas[pygame.K_DOWN]:
                    paleta2.mover("abajo", 2, teclas)
                if teclas[pygame.K_ESCAPE]:
                    fase = True
                    inicio = True
                    paleta = Paleta((ancho // 40 - 15), (alto // 20 - 10), 20, 80)
                    paleta2 = Paleta((ancho - 30), (alto // 20 - 10), 20, 80)
                    bola = Bola([5, -5])


                puntaje = fuente2.render("P1: " + str(bola.score), True, white)
                puntaje2 = fuente2.render("P2: " + str(bola.score2), True, white)
                screen.blit(puntaje, (0,0))
                screen.blit(puntaje2, (700, 0))

                bola.mover(2)
                bola.colision_paleta(paleta, paleta2)

                if bola.score >= 5:
                    boton6.dibujar()
                    boton3.dibujar()
                    screen.blit(texto5, (boton3))
                    screen.blit(texto9, (boton6))
                    bola.velocidad[0] = 0
                    bola.velocidad[1] = 0
                    screen.blit(texto, (400, 0))
                    reinicio = boton3.reinicia(event)
                    menu = boton6.volver(event)
                    canal_sonido1.play(sonido1)
                    if reinicio == True:
                        paleta = Paleta((ancho // 40 - 15), (alto // 20 - 10), 20, 80)
                        paleta2 = Paleta((ancho - 30), (alto // 20 - 10), 20, 80)
                        bola = Bola([5, -5])
                    elif menu == True:
                        inicio = True
                        paleta = Paleta((ancho // 40 - 15), (alto // 20 - 10), 20, 80)
                        paleta2 = Paleta((ancho - 30), (alto // 20 - 10), 20, 80)
                        bola = Bola([5, -5])

                if bola.score2 >= 5:
                    boton6.dibujar()
                    boton3.dibujar()
                    screen.blit(texto5, (boton3))
                    screen.blit(texto9, (boton6))
                    bola.velocidad[0] = 0
                    bola.velocidad[1] = 0
                    screen.blit(texto, (400, 0))
                    reinicio = boton3.reinicia(event)
                    menu = boton6.volver(event)
                    canal_sonido1.play(sonido1)

                    if reinicio == True:
                        paleta = Paleta((ancho // 40 - 15), (alto // 20 - 10), 20, 80)
                        paleta2 = Paleta((ancho - 30), (alto // 20 - 10), 20, 80)
                        bola = Bola([5, -5])
                    elif menu == True:
                        inicio = True
                        paleta = Paleta((ancho // 40 - 15), (alto // 20 - 10), 20, 80)
                        paleta2 = Paleta((ancho - 30), (alto // 20 - 10), 20, 80)
                        bola = Bola([5, -5])

                paleta.dibujar()
                paleta2.dibujar()
                bola.dibujar()
                pygame.draw.line(screen, 'white',(0,430),(1080,430),5)
                screen.blit(wasd,(250, 400))
                screen.blit(flechas, (740, 450))
                screen.blit(texto10, (50, 450))
                screen.blit(texto11, (550, 450))
                

        pygame.display.flip()
