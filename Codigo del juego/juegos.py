import pygame
import Poligonos 
import math
pygame.init() 
pantalla = pygame.display.set_mode((800, 710))
pygame.display.set_caption("Tetris") #Le pone un titulo a la pantalla
running = True 
timer_segundo = pygame.USEREVENT
pygame.time.set_timer(timer_segundo, 150) #1000 es un segundo
x_L = 500
y_L = 200
x_rectangulo = 200
y_rectangulo = 100
x_cuadrado = 200
y_cuadrado = 300
color_lineas = (255, 255, 255) 
x_T = 400
y_T= 100
x_s = 200 
y_s = 25
cuadrado = Poligonos.Poligonos(x_cuadrado, y_cuadrado, 50, 50, pantalla, (255, 255, 0))
l = Poligonos.Poligonos(x_L, y_L, 25, 100, pantalla, (255, 255, 0))
t = Poligonos.Poligonos(x_T, y_T, 25, 25, pantalla, (255, 255, 0))
s = Poligonos.Poligonos(x_s, y_s, 25, 25, pantalla, (255, 255, 0))
rectangulo = Poligonos.Poligonos(x_rectangulo, y_rectangulo, 125, 25, pantalla, (255, 255, 0))
angle = 0

    # Dibujar líneas horizontales
for y in range(1, 705, 25):
        pygame.draw.line(pantalla, color_lineas, (200, y), (575, y))
    # Dibujar líneas verticales
for x in range(200, 600, 25):
    pygame.draw.line(pantalla, color_lineas, (x, 0), (x, 700))

while running:
    lista_evento = pygame.event.get()
    for evento in lista_evento:
        if evento.type == pygame.QUIT:
            running = False
        if evento.type == timer_segundo:
            y_L += 0
            y_cuadrado += 0
            y_T += 0
            y_rectangulo += 0
            y_s += 0
            cuadrado.y = y_cuadrado
            cuadrado.dibujar_cuadrado()
            l.y = y_L
            l.dibujar_l()
            t.y = y_T
            t.dibujar_t()
            rectangulo.y = y_rectangulo
            rectangulo.dibujar_rectangulo()
            s.y = y_s
            
        s.x = x_s
        s.y = y_s
        s.dibujar_s()

    pygame.display.flip()                                                                                                                                                                           

pygame.quit()
