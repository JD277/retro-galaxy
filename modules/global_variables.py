import pygame 
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Retro Galaxy")
running = True
pygame.init()
class Message:
    def __init__(self, text, x, y, font, size, color,pos):
        self.text = text
        self.x = x
        self.y = y
        self.text_font = pygame.font.Font(font, size)
        self.text_surf = self.text_font.render(text, True, color)

        if pos == 1:
           self.text_rect = pygame.Surface.get_rect(self.text_surf, topleft = (x,y))

        if pos == 0:
            self.text_rect = pygame.Surface.get_rect(self.text_surf, center = (x,y))

    def draw_text(self):
        screen.blit(self.text_surf,self.text_rect)