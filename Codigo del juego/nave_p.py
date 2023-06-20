from balas import *
from constantes import *
from estructura_generica import *

pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)

class Nave_p(Estructura):
    def __init__(self, width, height, x, y, speed, img) -> None:
        super().__init__(width, height, x, y, speed, img)
        self.rect.centerx = WIDTH_PANTALLA // 2
        self.lives = 10
        self.visible = True

    def update_p(self, key):
        if key[pygame.K_RIGHT] and self.rect.x < WIDTH_PANTALLA - 50:
            self.rect.x += 5
        if key[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5
        if key[pygame.K_UP] and self.rect.y > HEIGHT_PANTALLA - 300:
            self.rect.y -= 5
        if key[pygame.K_DOWN] and self.rect.y < HEIGHT_PANTALLA - 60:
            self.rect.y += 5

    def button_space(self, key, list_bullet, sound_laser):
        if key[pygame.K_SPACE]:
                list_bullet = self.shoot(list_bullet, sound_laser)  

    def shoot(self, list_bullet, laser):
        bullet = Balas(WIDTH_BULLET, HEIGHT_BULLET, self.rect.centerx, self.rect.top, SPEED_BULLET_NAVE_P, IMG_BULLET)
        list_bullet.append(bullet)
        laser.play()
        return list_bullet

        