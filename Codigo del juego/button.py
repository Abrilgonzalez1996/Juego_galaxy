from constantes import *
from estructura_generica import *

class button(Estructura):
    def __init__(self, text, width, height, x, y, speed, img, color, button_frame, letter) -> None:
        super().__init__(width, height, x, y, speed, img)
        self.color = color
        self.text = text
        self.frame = button_frame
        self.pressed = False
        self.color_letter = letter

    def draw_button(self):
        pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height), self.frame)

    def draw_text(self, x, y, size):
        self.draw_button()
        text = pygame.font.SysFont("serif", size).render(self.text, True, self.color_letter)
        SCREEN.blit(text, (self.x + x, self.y + y))

    def style_button(self, pressed, frame, color):
        #Le asigna nuevos valores al boton presionado
        self.pressed = pressed
        self.frame = frame
        self.color_letter = color