import pygame
from button import *
from colores import * 
from constantes import *

class menu:
    def __init__(self, text_1, text_2, width_img, height_img, img, flag) -> None:
        self.img = pygame.transform.scale(img, (width_img, height_img))
        self.flag = flag
        self.button_play = button(text_1 , WIDTH_BUTTON, HEIGHT_BUTTON, X_BUTTON, Y_BUTTON1, None, None, WHITE, FRAME_BUTTON, WHITE)
        self.button_ranking = button(text_2 , WIDTH_BUTTON, HEIGHT_BUTTON, X_BUTTON, Y_BUTTON2, None, None, WHITE, FRAME_BUTTON, WHITE)
        self.button_quit = button("QUIT" , WIDTH_BUTTON, HEIGHT_BUTTON, X_BUTTON, Y_BUTTON3, None, None, WHITE, FRAME_BUTTON, WHITE)

    def draw_img(self, x, y):
        SCREEN.blit(self.img, (x, y)) 

    def pressed_button_menu(self, pressed_mouse, list_flag):
        if pressed_mouse[0] == 1: #Realiza alguna acción cuando se presiona el botón izquierdo del mouse       
            if self.button_play.rect.collidepoint(pygame.mouse.get_pos()): #Realiza alguna acción cuando se presiona el botón "Play"  
                self.button_play.style_button(True, FRAME_BUTTON_PRESSED, BLACK)              
            elif self.button_ranking.rect.collidepoint(pygame.mouse.get_pos()): #Realiza alguna acción cuando se presiona el botón "Ranking"
                self.button_ranking.style_button(True, FRAME_BUTTON_PRESSED, BLACK) 
            elif self.button_quit.rect.collidepoint(pygame.mouse.get_pos()): #Realiza alguna acción cuando se presiona el botón "Quit"
                self.button_quit.style_button(True, FRAME_BUTTON_PRESSED, BLACK)         
        if pressed_mouse[0] == 0: #Realiza alguna acción cuando soltas el botón  
            if self.button_play.pressed == True:
                list_flag[0] = True
                self.button_play.style_button(False, FRAME_BUTTON, WHITE) #El boton vuelve a su estado normal 
            elif self.button_ranking.pressed == True:
                list_flag[1] = True
                self.button_ranking.style_button(False, FRAME_BUTTON, WHITE) #El boton vuelve a su estado normal 
            elif self.button_quit.pressed == True:
                list_flag[2] = True
                self.button_quit.style_button(False, FRAME_BUTTON, WHITE) #El boton vuelve a su estado normal




