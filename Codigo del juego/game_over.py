from menu import *
from button import *
from constantes import *
from funciones_galaxy import *

class Game_over(menu):
    def __init__(self, text_1, text_2, width_img, height_img, img, flag) -> None:
        super().__init__(text_1, text_2, width_img, height_img, img, flag)
        self.button_yes = button(text_1 , WIDTH_BUTTON_G, HEIGHT_BUTTON, X_BUTTON1_G, Y_BUTTON_G, None, None, WHITE, FRAME_BUTTON_G, WHITE)    
        self.button_no = button(text_2 , WIDTH_BUTTON_G, HEIGHT_BUTTON, X_BUTTON2_G, Y_BUTTON_G, None, None, WHITE, FRAME_BUTTON_G, WHITE)

    def pressed_button_game_over(self, pressed_mouse):
        if pressed_mouse[0] == 1: #Realiza alguna acción cuando se presiona el botón izquierdo del mouse       
            if self.button_yes.rect.collidepoint(pygame.mouse.get_pos()): #Realiza alguna acción cuando se presiona el botón "Play"                    
                self.button_yes.style_button(True, FRAME_BUTTON_PRESSED, BLACK)
            elif self.button_no.rect.collidepoint(pygame.mouse.get_pos()): #Realiza alguna acción cuando se presiona el botón "Ranking"            
                self.button_no.style_button(True, FRAME_BUTTON_PRESSED, BLACK)
        elif pressed_mouse[0] == 0 and (self.button_yes.pressed == True or self.button_no.pressed == True): #Realiza alguna acción cuando soltas el botón  
            if self.button_yes.pressed == True:
                self.button_yes.style_button(False, FRAME_BUTTON, WHITE)
                self.flag = False
                retorno =  True
            else:
                self.button_no.style_button(False, FRAME_BUTTON, WHITE)
                retorno = False
            return retorno