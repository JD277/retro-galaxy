import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Título del juego
pygame.display.set_caption("Space Invader")

# Colores
background_color = (0, 0, 0)  # Negro
text_color = (255, 255, 255)  # Blanco

# Fuente
font = pygame.font.Font(None, 36)

# Clase base para los personajes del juego
class Character:
    def __init__(self, image_path, x, y):
        try:
            self.image = pygame.image.load(image_path)
        except pygame.error as e:
            print(f"Error al cargar la imagen: {e}")
            sys.exit()
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

# Clase Jugador
class Player(Character):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)

    def move(self, x_change):
        self.x += x_change
        if self.x <= 0:
            self.x = 0
        elif self.x >= screen_width - self.image.get_width():
            self.x = screen_width - self.image.get_width()

# Clase Invasor
class Invader(Character):
    def __init__(self, image_path, x, y, x_change, y_change):
        super().__init__(image_path, x, y)
        self.x_change = x_change
        self.y_change = y_change

    def move(self):
        self.x += self.x_change
        if self.x <= 0 or self.x >= screen_width - self.image.get_width():
            self.x_change *= -1
            self.y += self.y_change

# Clase Bala
class Bullet(Character):
    def __init__(self, image_path, x, y, y_change):
        super().__init__(image_path, x, y)
        self.y_change = y_change
        self.state = "ready"  # "ready" o "fire"

    def fire(self, x, y):
        self.state = "fire"
        self.x = x
        self.y = y

    def move(self):
        if self.state == "fire":
            self.y += self.y_change
            if self.y <= 0 or self.y >= screen_height:
                self.state = "ready"

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

# Clase Obstáculo
class Obstacle:
    def __init__(self, x, y):
        self.rects = [pygame.Rect(x + i * 20, y + j * 20, 20, 20) for j in range(3) for i in range(5)]
        self.color = (0, 255, 0)  # Verde

    def draw(self, screen):
        for rect in self.rects:
            pygame.draw.rect(screen, self.color, rect)

    def hit(self, bullet_rect):
        for rect in self.rects:
            if rect.colliderect(bullet_rect):
                self.rects.remove(rect)
                return True
        return False

# Función para mostrar el texto
def show_text(screen, text, x, y):
    render = font.render(text, True, text_color)
    screen.blit(render, (x, y))

# Función para mostrar Game Over y reiniciar
def game_over():
    screen.fill(background_color)
    show_text(screen, "Game Over", screen_width // 2 - 70, screen_height // 2)
    show_text(screen, "Presiona 'R' para Reiniciar", screen_width // 2 - 150, screen_height // 2 + 50)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                    main_game()
                    
# Función para mostrar la pantalla de victoria y preguntar por mayor dificultad
def victory_screen():
    screen.fill(background_color)
    show_text(screen, "¡Victoria!", screen_width // 2 - 70, screen_height // 2)
    show_text(screen, "Presiona 'Y' para aumentar dificultad", screen_width // 2 - 200, screen_height // 2 + 50)
    show_text(screen, "Presiona 'N' para jugar de nuevo", screen_width // 2 - 150, screen_height // 2 + 100)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    waiting = False
                    main_game(difficulty_increase=True)
                if event.key == pygame.K_n:
                    waiting = False
                    main_game()

# Menú inicial
def main_menu():
    menu = True
    while menu:
        screen.fill(background_color)
        show_text(screen, "Space Invaders", 300, 200)
        show_text(screen, "Presiona 'J' para Jugar", 270, 300)
        show_text(screen, "Presiona 'Q' para Salir", 270, 350)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    menu = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Juego principal
def main_game():
    player = Player('../retro-galaxy/src/sprites/Space_invaders/jugador.png', screen_width // 2, screen_height - 70)
    invader_images = [
        '../retro-galaxy/src/sprites/Space_invaders/invasor1.png',
        '../retro-galaxy/src/sprites/Space_invaders/invasor2.png',
        '../retro-galaxy/src/sprites/Space_invaders/invasor3.png',
        '../retro-galaxy/src/sprites/Space_invaders/invasor4.png'
    ]
    invaders = [Invader(random.choice(invader_images), random.randint(0, screen_width - 64), random.randint(50, 150), 0.5, 30) for _ in range(10)]
    player_bullet = Bullet('../retro-galaxy/src/sprites/Space_invaders/bala.png', 0, screen_height - 70, -5)
    enemy_bullets = []
    obstacle_positions = [(200, screen_height - 150), (400, screen_height - 150), (600, screen_height - 150)]
    obstacles = [Obstacle(x, y) for x, y in obstacle_positions]
    score = 0

    invader_speed_increase = 0.05

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.x_change = -2
                if event.key == pygame.K_RIGHT:
                    player.x_change = 2
                if event.key == pygame.K_SPACE and player_bullet.state == "ready":
                    player_bullet.fire(player.x + player.image.get_width() // 2 - player_bullet.image.get_width() // 2, player.y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.x_change = 0

        player.move(player.x_change)
        player_bullet.move()

        # Movimiento de los invasores y disparos
        for invader in invaders:
            invader.move()
            if player_bullet.state == "fire" and invader.get_rect().colliderect(player_bullet.get_rect()):
                player_bullet.state = "ready"
                player_bullet.y = screen_height - 70
                invader.x = random.randint(0, screen_width - invader.image.get_width())
                invader.y = random.randint(50, 150)
                score += 1
                # Incrementar la velocidad de los invasores
                invader.x_change += invader_speed_increase

            if random.randint(0, 100) < 1 and len(enemy_bullets) < 5:
                enemy_bullet = Bullet('../retro-galaxy/src/sprites/Space_invaders/bala_enemiga.png', invader.x + invader.image.get_width() // 2 - player_bullet.image.get_width() // 2, invader.y, 3)
                enemy_bullets.append(enemy_bullet)

            # Comprobar colisión entre invasor y jugador
            if invader.get_rect().colliderect(player.get_rect()):
                game_over()

        # Agregar más invasores con el tiempo
        if len(invaders) < 10:
            invaders.append(Invader(random.choice(invader_images), random.randint(0, screen_width - 64), random.randint(50, 150), 0.5, 30))

        # Movimiento de las balas enemigas
        for bullet in enemy_bullets:
            bullet.move()
            if bullet.state == "ready":
                enemy_bullets.remove(bullet)
            if bullet.get_rect().colliderect(player.get_rect()):
                game_over()

        # Colisiones con obstáculos
        for obstacle in obstacles:
            if obstacle.hit(player_bullet.get_rect()):
                player_bullet.state = "ready"
            for bullet in enemy_bullets:
                if obstacle.hit(bullet.get_rect()):
                    enemy_bullets.remove(bullet)

        screen.fill(background_color)
        player.draw(screen)
        for invader in invaders:
            invader.draw(screen)
        if player_bullet.state == "fire":
            player_bullet.draw(screen)
        for bullet in enemy_bullets:
            bullet.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)
        show_text(screen, f"Puntos: {score}", 10, 10)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_menu()
    main_game()




