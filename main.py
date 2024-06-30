import pygame
import random

# Inicialización de Pygame
pygame.init()

# Definición de colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (192, 192, 192)
ROJO = (255, 0, 0)
GRIS_OSCURO = (169, 169, 169)

# Tamaño de la pantalla y de las casillas (
ANCHO_PANTALLA = 400
ALTO_PANTALLA = 500
TAMANO_TABLERO = 300
TAMANO_CASILLA = TAMANO_TABLERO // 18  # El tablero es de 12x12
MARGEN = 3

# Constantes para los diferentes modos de juego
MODOS_JUEGO = {
    "Cadete": (10, 10),
    "Soldado": (12, 16),
    "Capitan": (15, 24),
    "Coronel terrícola": (20, 35)
}

class Casilla:
    def __init__(self):
        self.visible = False                # Indica si la casilla es visible o no para el usuario
        self.tiene_mina = False              # Indica si hay colocada una mina en esa posición
        self.mina_marcada = False            # Indica si el jugador marcó una mina en esa posición
        self.num_minas_adyacentes = 0        # Numero de minas en las casillas adyacentes, para pintar el numero

class Buscaminas:
    def __init__(self, tam, num_minas):
        self.tamano = tam                   # Tamaño del tablero (cuadrado)
        self.tablero = []                   # Matriz de casillas
        self.pendientes = tam * tam         # Numero de celdas que quedan por visualizarse
        self.estado = ""                    # "P" = Perdido / "G" = Ganado / "" = En juego
        self.x_error = None                 # Fila de la casilla que produjo el error (al perder)
        self.y_error = None                 # Columna de la casilla que produjo el error (al perder)
        self.minas_restantes = num_minas    # Número de minas restantes

        # Inicialización del tablero con casillas vacías
        for fila in range(tam):
            f = []
            for col in range(tam):
                f.append(Casilla())
            self.tablero.append(f)

        # Colocación de las minas aleatoriamente
        num = 0
        while num < num_minas:
            rndx = random.randint(0, tam - 1)
            rndy = random.randint(0, tam - 1)
            if not self.tablero[rndx][rndy].tiene_mina:
                self.tablero[rndx][rndy].tiene_mina = True
                fila_ini = max(rndx - 1, 0)
                fila_fin = min(rndx + 1, tam - 1)
                col_ini = max(rndy - 1, 0)
                col_fin = min(rndy + 1, tam - 1)
                for i in range(fila_ini, fila_fin + 1):
                    for j in range(col_ini, col_fin + 1):
                        if i != rndx or j != rndy:
                            self.tablero[i][j].num_minas_adyacentes += 1
                num += 1

    def descubrir_casilla(self, fila, col):
        if fila < 0 or col < 0 or fila >= self.tamano or col >= self.tamano:
            return
        casilla = self.tablero[fila][col]
        if not casilla.visible and not casilla.mina_marcada:
            casilla.visible = True
            self.pendientes -= 1
            if casilla.tiene_mina:
                self.x_error = fila
                self.y_error = col
                self.estado = "P"  # Estado perdido
            elif casilla.num_minas_adyacentes == 0:
                self.__descubrir_casillas_vacias(fila, col)

    def __descubrir_casillas_vacias(self, fila, col):
        for i in range(max(0, fila - 1), min(self.tamano, fila + 2)):
            for j in range(max(0, col - 1), min(self.tamano, col + 2)):
                if not self.tablero[i][j].visible:
                    self.descubrir_casilla(i, j)

    def alternar_marcado_mina(self, fila, col):
        if fila < 0 or col < 0 or fila >= self.tamano or col >= self.tamano:
            return
        casilla = self.tablero[fila][col]
        if not casilla.visible:
            if casilla.mina_marcada:
                casilla.mina_marcada = False
                self.minas_restantes += 1
            else:
                if self.minas_restantes > 0:  # Verificar si quedan minas restantes por marcar
                    casilla.mina_marcada = True
                    self.minas_restantes -= 1

        # Verificar si se han marcado todas las minas correctamente para ganar
        todas_marcadas_correctamente = True
        for fila in range(self.tamano):
            for col in range(self.tamano):
                casilla_actual = self.tablero[fila][col]
                if casilla_actual.tiene_mina and not casilla_actual.mina_marcada:
                    todas_marcadas_correctamente = False
                    break
            if not todas_marcadas_correctamente:
                break

        if todas_marcadas_correctamente:
            self.estado = "G"  # Estado de ganar

    def dibujar(self, pantalla, num_derrotas=0):
        for fila in range(self.tamano):
            for col in range(self.tamano):
                casilla = self.tablero[fila][col]
                x = col * (TAMANO_CASILLA + MARGEN)
                y = fila * (TAMANO_CASILLA + MARGEN) + 50  # Ajuste para dejar espacio para la barra de estado de minas
                rect = pygame.Rect(x, y, TAMANO_CASILLA, TAMANO_CASILLA)
                casilla.rect = rect  # Almacenamos el rectángulo para la detección de clics
                if not casilla.visible:
                    pygame.draw.rect(pantalla, GRIS, rect)
                    if casilla.mina_marcada:
                        pygame.draw.line(pantalla, NEGRO, rect.topleft, rect.bottomright, 3)
                        pygame.draw.line(pantalla, NEGRO, rect.bottomleft, rect.topright, 3)
                else:
                    pygame.draw.rect(pantalla, BLANCO, rect)
                    if casilla.tiene_mina:
                        pygame.draw.circle(pantalla, ROJO, rect.center, TAMANO_CASILLA // 4)
                    elif casilla.num_minas_adyacentes > 0:
                        font = pygame.font.SysFont(None, 24)
                        texto = font.render(str(casilla.num_minas_adyacentes), True, NEGRO)
                        pantalla.blit(texto, rect.topleft)

        # Dibujar la barra de estado de minas restantes y numero de derrotas
        pygame.draw.rect(pantalla, GRIS_OSCURO, (0, 0, ANCHO_PANTALLA, 50))
        font = pygame.font.SysFont(None, 20)  # Reducir el tamaño de la fuente para ajustarse al espacio
        texto = font.render(f"Minas restantes: {self.minas_restantes} | Número de derrotas: {num_derrotas}", True,
                            BLANCO)
        pantalla.blit(texto, (10, 10))
        if self.estado == "G":
            mostrar_mensaje_ganar(pantalla)


def mostrar_mensaje_ganar(pantalla, modo_juego=None, nivel_actual=None, num_derrotas=None):
    fuente = pygame.font.SysFont(None, 30)
    texto = fuente.render("¡Salvaste a la Tierra, eres un héroe!", True, BLANCO)

    if modo_juego == "arcade" and nivel_actual is not None and num_derrotas is not None:
        if nivel_actual == 4:
            texto = fuente.render(
                f"Felicidades, haz salvado a la Tierra de todas las minas, y tan sólo te llevó {num_derrotas} intentos",
                True, BLANCO)
        rect_continuar = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 300, 200, 40)
        rect_menu_principal = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 360, 200, 40)
    else:
        rect_menu_principal = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 300, 200, 40)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    x, y = evento.pos
                    if modo_juego == "arcade":
                        if rect_continuar.collidepoint(x, y):
                            return "siguiente_nivel"
                        elif rect_menu_principal.collidepoint(x, y):
                            return "menu_principal"
                    else:
                        if rect_menu_principal.collidepoint(x, y):
                            return "menu_principal"

        pantalla.fill(GRIS_OSCURO)
        pantalla.blit(texto, (ANCHO_PANTALLA // 2 - texto.get_width() // 2, 200))

        if modo_juego == "arcade":
            pygame.draw.rect(pantalla, GRIS, rect_continuar)
            pygame.draw.rect(pantalla, GRIS, rect_menu_principal)

            texto_continuar = fuente.render("Continuar", True, BLANCO)
            texto_menu_principal = fuente.render("Menú principal", True, BLANCO)

            pantalla.blit(texto_continuar, (rect_continuar.centerx - texto_continuar.get_width() // 2,
                                            rect_continuar.centery - texto_continuar.get_height() // 2))
            pantalla.blit(texto_menu_principal, (rect_menu_principal.centerx - texto_menu_principal.get_width() // 2,
                                                 rect_menu_principal.centery - texto_menu_principal.get_height() // 2))
        else:
            pygame.draw.rect(pantalla, GRIS, rect_menu_principal)
            texto_menu_principal = fuente.render("Menú principal", True, BLANCO)
            pantalla.blit(texto_menu_principal, (rect_menu_principal.centerx - texto_menu_principal.get_width() // 2,
                                                 rect_menu_principal.centery - texto_menu_principal.get_height() // 2))

        pygame.display.flip()
def mostrar_ventana_emergente(pantalla):
    fuente = pygame.font.SysFont(None, 30)
    texto1 = fuente.render("¡Oh no, explotaste!", True, ROJO)
    texto2 = fuente.render("¿Quieres intentarlo de nuevo?", True, BLANCO)

    rect_opcion1 = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 300, 200, 40)
    rect_opcion2 = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 360, 200, 40)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    x, y = evento.pos
                    if rect_opcion1.collidepoint(x, y):
                        return True  # Reiniciar juego
                    elif rect_opcion2.collidepoint(x, y):
                        return "menu_principal" # Salir

        pantalla.fill(GRIS_OSCURO)
        pantalla.blit(texto1, (ANCHO_PANTALLA // 2 - texto1.get_width() // 2, 200))
        pantalla.blit(texto2, (ANCHO_PANTALLA // 2 - texto2.get_width() // 2, 250))

        pygame.draw.rect(pantalla, GRIS, rect_opcion1)
        pygame.draw.rect(pantalla, GRIS, rect_opcion2)

        font = pygame.font.SysFont(None, 20)
        texto_opcion1 = font.render("Sí", True, BLANCO)
        texto_opcion2 = font.render("No", True, BLANCO)
        pantalla.blit(texto_opcion1, (rect_opcion1.centerx - texto_opcion1.get_width() // 2, rect_opcion1.centery - texto_opcion1.get_height() // 2))
        pantalla.blit(texto_opcion2, (rect_opcion2.centerx - texto_opcion2.get_width() // 2, rect_opcion2.centery - texto_opcion2.get_height() // 2))

        pygame.display.flip()

def menu_principal(pantalla):
    fuente = pygame.font.SysFont(None, 30)  # Reducir el tamaño de la fuente para ajustarse al espacio
    titulo = fuente.render("Buscaminas Terrícolas", True, BLANCO)
    boton_nuevo = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 200, 200, 40)
    boton_salir = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 300, 200, 40)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    x, y = evento.pos
                    if boton_nuevo.collidepoint(x, y):
                        return "nuevo"
                    elif boton_salir.collidepoint(x, y):
                        pygame.quit()
                        quit()

        pantalla.fill(GRIS_OSCURO)
        pantalla.blit(titulo, (ANCHO_PANTALLA // 2 - titulo.get_width() // 2, 100))

        pygame.draw.rect(pantalla, GRIS, boton_nuevo)
        pygame.draw.rect(pantalla, GRIS, boton_salir)

        font = pygame.font.SysFont(None, 20)  # Reducir el tamaño de la fuente para ajustarse al espacio
        texto_nuevo = font.render("Nuevo juego", True, BLANCO)
        texto_salir = font.render("Salir", True, BLANCO)
        pantalla.blit(texto_nuevo, (boton_nuevo.centerx - texto_nuevo.get_width() // 2, boton_nuevo.centery - texto_nuevo.get_height() // 2))
        pantalla.blit(texto_salir, (boton_salir.centerx - texto_salir.get_width() // 2, boton_salir.centery - texto_salir.get_height() // 2))

        pygame.display.flip()

def menu_modos_juego(pantalla):
    fuente = pygame.font.SysFont(None, 30)  # Reducir el tamaño de la fuente para ajustarse al espacio
    titulo = fuente.render("Seleccione el modo de juego", True, BLANCO)
    boton_arcade = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 300, 200, 40)
    boton_libre = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 360, 200, 40)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    x, y = evento.pos
                    if boton_arcade.collidepoint(x, y):
                        return "arcade"
                    elif boton_libre.collidepoint(x, y):
                        return "libre"

        pantalla.fill(GRIS_OSCURO)
        pantalla.blit(titulo, (ANCHO_PANTALLA // 2 - titulo.get_width() // 2, 100))

        pygame.draw.rect(pantalla, GRIS, boton_arcade)
        pygame.draw.rect(pantalla, GRIS, boton_libre)

        font = pygame.font.SysFont(None, 20)  # Reducir el tamaño de la fuente para ajustarse al espacio
        texto_arcade = font.render("Arcade", True, BLANCO)
        texto_libre = font.render("Juego Libre", True, BLANCO)
        pantalla.blit(texto_arcade, (boton_arcade.centerx - texto_arcade.get_width() // 2, boton_arcade.centery - texto_arcade.get_height() // 2))
        pantalla.blit(texto_libre, (boton_libre.centerx - texto_libre.get_width() // 2, boton_libre.centery - texto_libre.get_height() // 2))

        pygame.display.flip()

def menu_juego_libre(pantalla):
    fuente = pygame.font.SysFont(None, 30)  # Reducir el tamaño de la fuente para ajustarse al espacio
    titulo = fuente.render("Seleccione el nivel de dificultad", True, BLANCO)
    boton_cadete = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 250, 200, 40)
    boton_soldado = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 300, 200, 40)
    boton_capitan = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 350, 200, 40)
    boton_coronel = pygame.Rect(ANCHO_PANTALLA // 2 - 100, 400, 200, 40)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    x, y = evento.pos
                    if boton_cadete.collidepoint(x, y):
                        return "Cadete"
                    elif boton_soldado.collidepoint(x, y):
                        return "Soldado"
                    elif boton_capitan.collidepoint(x, y):
                        return "Capitan"
                    elif boton_coronel.collidepoint(x, y):
                        return "Coronel terrícola"

        pantalla.fill(GRIS_OSCURO)
        pantalla.blit(titulo, (ANCHO_PANTALLA // 2 - titulo.get_width() // 2, 100))

        pygame.draw.rect(pantalla, GRIS, boton_cadete)
        pygame.draw.rect(pantalla, GRIS, boton_soldado)
        pygame.draw.rect(pantalla, GRIS, boton_capitan)
        pygame.draw.rect(pantalla, GRIS, boton_coronel)

        font = pygame.font.SysFont(None, 20)  # Reducir el tamaño de la fuente para ajustarse al espacio
        texto_cadete = font.render("Cadete", True, BLANCO)
        texto_soldado = font.render("Soldado", True, BLANCO)
        texto_capitan = font.render("Capitan", True, BLANCO)
        texto_coronel = font.render("Coronel terrícola", True, BLANCO)

        pantalla.blit(texto_cadete, (boton_cadete.centerx - texto_cadete.get_width() // 2, boton_cadete.centery - texto_cadete.get_height() // 2))
        pantalla.blit(texto_soldado, (boton_soldado.centerx - texto_soldado.get_width() // 2, boton_soldado.centery - texto_soldado.get_height() // 2))
        pantalla.blit(texto_capitan, (boton_capitan.centerx - texto_capitan.get_width() // 2, boton_capitan.centery - texto_capitan.get_height() // 2))
        pantalla.blit(texto_coronel, (boton_coronel.centerx - texto_coronel.get_width() // 2, boton_coronel.centery - texto_coronel.get_height() // 2))

        pygame.display.flip()


def main():
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Buscaminas")

    while True:
        # Mostrar menú principal
        opcion_menu = menu_principal(pantalla)

        if opcion_menu == "nuevo":
            # Mostrar menú de modos de juego
            modo_juego = menu_modos_juego(pantalla)

            if modo_juego == "arcade":
                nivel_actual = 1
                max_niveles = 3
                num_derrotas = 0
                while nivel_actual <= max_niveles:
                    dificultad = list(MODOS_JUEGO.keys())[nivel_actual - 1]
                    tamano, num_minas = MODOS_JUEGO[dificultad]
                    juego = Buscaminas(tamano, num_minas)

                    jugando = True
                    while jugando:
                        for evento in pygame.event.get():
                            if evento.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            elif evento.type == pygame.MOUSEBUTTONDOWN:
                                x, y = evento.pos
                                col = x // (TAMANO_CASILLA + MARGEN)
                                fila = (y - 50) // (TAMANO_CASILLA + MARGEN)

                                if 0 <= fila < tamano and 0 <= col < tamano:
                                    if evento.button == 1:
                                        juego.descubrir_casilla(fila, col)
                                    elif evento.button == 3:
                                        juego.alternar_marcado_mina(fila, col)

                        pantalla.fill(GRIS_OSCURO)
                        juego.dibujar(pantalla, num_derrotas)
                        pygame.display.flip()

                        if juego.estado == "P":
                            reintentar = mostrar_ventana_emergente(pantalla)
                            num_derrotas += 1
                            if reintentar == True:
                                juego = Buscaminas(tamano, num_minas)
                            elif reintentar == "menu_principal":
                                jugando = False
                                nivel_actual = max_niveles + 1  # Esto fuerza la salida del bucle arcade
                                break
                        elif juego.estado == "G":
                            resultado = mostrar_mensaje_ganar(pantalla, modo_juego, nivel_actual, num_derrotas)
                            if resultado == "siguiente_nivel":
                                nivel_actual += 1
                                jugando = False
                            elif resultado == "menu_principal":
                                jugando = False
                                break

            elif modo_juego == "libre":
                dificultad = menu_juego_libre(pantalla)
                tamano, num_minas = MODOS_JUEGO[dificultad]
                juego = Buscaminas(tamano, num_minas)
                num_derrotas = 0

                jugando = True
                while jugando:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif evento.type == pygame.MOUSEBUTTONDOWN:
                            x, y = evento.pos
                            col = x // (TAMANO_CASILLA + MARGEN)
                            fila = (y - 50) // (TAMANO_CASILLA + MARGEN)

                            if 0 <= fila < tamano and 0 <= col < tamano:
                                if evento.button == 1:
                                    juego.descubrir_casilla(fila, col)
                                elif evento.button == 3:
                                    juego.alternar_marcado_mina(fila, col)

                    pantalla.fill(GRIS_OSCURO)
                    juego.dibujar(pantalla, num_derrotas)
                    pygame.display.flip()

                    if juego.estado == "P":
                        reintentar = mostrar_ventana_emergente(pantalla)
                        num_derrotas += 1
                        if reintentar == True:
                            juego = Buscaminas(tamano, num_minas)
                        elif reintentar == "menu_principal":
                            jugando = False
                            break
                    elif juego.estado == "G":
                        resultado = mostrar_mensaje_ganar(pantalla)
                        if resultado == "menu_principal":
                            jugando = False
                            break

        elif opcion_menu == "salir":
            pygame.quit()
            quit()

            # Mostrar mensaje de felicitación
            pantalla.fill(NEGRO)
            mostrar_mensaje_ganar(pantalla, modo_juego, nivel_actual, num_derrotas)
            pygame.display.flip()
            pygame.time.delay(3000)

if __name__ == "__main__":
    main()