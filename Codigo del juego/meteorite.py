import random
from explosion import *
from constantes import *
from estructura_generica import *
from colores import *

class meteorite(Estructura):
    def __init__(self, list_sprites, width, high, y, speed, list_img_explosion) -> None:
        self.list_meteorite = list_sprites
        self.position = 0
        self.time = pygame.time.get_ticks()
        self.explosion = Explosion(list_img_explosion, SPEED_METEORITE_EXPLOSION, X_MARGIN_MET, Y_MARGIN_MET)
        self.lives = 2
        super().__init__(width, high, random.randrange(WIDTH_PANTALLA - width), y, speed, None)

    def update(self, time_now):
        self.rect.y += 4
        if time_now - self.time > self.speed:
            self.time = time_now
            self.position += 1
            if self.position == len(self.list_meteorite):
                self.position = 0
        self.dibujar()
    
    def dibujar(self):
        SCREEN.blit(self.list_meteorite[self.position], (self.rect.x, self.rect.y))

    
        