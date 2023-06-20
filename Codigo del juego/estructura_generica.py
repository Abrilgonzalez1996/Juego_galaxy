import pygame
class Estructura:
    def __init__(self, width, height, x, y, speed, img) -> None:
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.speed = speed
        self.img = img