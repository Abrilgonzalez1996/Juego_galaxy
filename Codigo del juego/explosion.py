from constantes import *
from estructura_generica import *

class Explosion:
    def __init__(self, list_sprites, speed, x_margin, y_margin) -> None:
        self.list_img = list_sprites    
        self.position = -1
        self.img = self.list_img[self.position]
        self.rect = self.img.get_rect()
        self.last_time = pygame.time.get_ticks()
        self.speed = speed
        self.x_margin = x_margin
        self.y_margin = y_margin
    
    def update(self, objet, time_now):
        if time_now - self.last_time > self.speed:
            self.last_time = time_now
            self.position += 1
        if len(self.list_img) - 30 == self.position:
            objet.flag_collision = False
        self.dibujar(objet.rect)

    def dibujar(self, rect):
        self.img = self.list_img[self.position]        
        SCREEN.blit(self.img, (rect.x - self.x_margin, rect.y - self.y_margin))       
        
