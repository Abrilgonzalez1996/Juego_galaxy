from constantes import *
from estructura_generica import *

class Balas(Estructura):
    def __init__(self, width, height, x, y, speed, img) -> None:
        super().__init__(width, height, x, y, speed, img)
        self.rect.centerx = x

    def update_p(self):
        self.rect.y -= self.speed

    def update_e(self):
        self.rect.y += self.speed
    
