import pygame
from menu import *
from button import *
from nave_e import *
from nave_p import *
from colores import *
from variables import *
from explosion import *
from game_over import *
from meteorite import *
from constantes import *
from funciones_galaxy import *

#Fondo
y_fondo = 0
time_accumulator = 0
list_img_explosion = get_surface_sprite_sheet(COLUMN_IMG_EXPLO, ROW_IMG_EXPLO, IMG_EXPLOSION, WIDTH_EXPLOSION, HEIGHT_EXPLOSION)
running = True 
game_over = False
pause = False
return_time = 60
last_time = 100 
delay_time = 700
input_name = ""
start_play = False
y_button_atras = 300
list_flag = [False, False, False]
button_pause = button(None, WIDTH_BUTTON_PAUSE, HEIGHT_BUTTON_PAUSE, X_PAUSE, Y_PAUSE, None, IMG_BUTTON_PAUSE, None, FRAME_PAUSE, WHITE)
button_play = button(None, WIDTH_BUTTON_PLAY, HEIGHT_BUTTON_PAUSE, X_PLAY, Y_PLAY, None, IMG_BUTTON_PLAY, None, FRAME_PLAY, WHITE)
flag_pause = False
list_img_meteorite = get_surface_sprite_sheet(COLUMN_IMG_METEORITE, ROW_IMG_METEORITE, IMG_METEORITE, WIDTH_METEORITE, HEIGHT_METEORITE)
time_accumulator = 0
time_last = pygame.time.get_ticks()
button_back = button("BACK", WIDTH_BUTTON_BACK, HEIGHT_BUTTON_BACK, X_BACK, y_button_atras, None, None, BLUE, FRAME_BACK, WHITE)
button_accept = button("ACCEPT", WIDTH_BUTTON_ACCEPT, HEIGHT_BUTTON_ACCEPT, X_ACCEPT, Y_ACCEPT, None, None, BLUE, FRAME_ACCEPT, WHITE)
time_speed = [0, True]
retorno = ""
time_collision = 0
continuar = True
list_remove = []
time_last_bullet = 0
