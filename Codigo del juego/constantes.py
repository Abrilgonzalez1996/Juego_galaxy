import pygame

#Tiempo
TIME_NAVE = pygame.USEREVENT
TIME_SHOT_NAVE_E = pygame.USEREVENT + 2
CLOCK = pygame.time.Clock()

#Pantalla
WIDTH_PANTALLA = 800
HEIGHT_PANTALLA = 700
SCREEN = pygame.display.set_mode((WIDTH_PANTALLA, HEIGHT_PANTALLA))

#Fondo
X_FONDO = 0
WIDTH_TITLE = 600
HEIGHT_TITLE = 200
X_TITLE = 100
Y_TITLE = 50

#Cursor 
WIDTH_CURSOR = 1
HEIGHT_CURSOR = 31
X_CURSOR = 200
Y_CURSOR = 280

#Botones inicio
WIDTH_BUTTON = 200
HEIGHT_BUTTON = 70
X_BUTTON = 290  
Y_BUTTON1 = 325
Y_BUTTON2 = 425
Y_BUTTON3 = 525
FRAME_BUTTON = 4
FRAME_BUTTON_PRESSED = 0

#Margen botones inicio
SIZE = 30
MARGIN_TEXT_X_ACCEPT = 63
MARGIN_TEXT_Y = 15
MARGIN_TEXT_X_RANKING = 30
MARGIN_TEXT_X_QUIT = 63

#Menu ingresar nombre
TITLE_SET_NAME = "Enter your name: "
X_TITLE_SET_NAME = 280
Y_TITLE_SET_NAME = 180
X_RECT_NAME = 250
Y_RECT_NAME = 260
WIDCH_RECT_NAME = 280
HEIGHT_RECT_NAME = 70
FRAME_SET_NAME = 2
X_MARGIN_ACCEPT = 10
Y_MARGIN_ACCEPT = 3
SIZE_TEXT_ACCEPT = 20
X_INPUT_NAME = 275
Y_INPUT_NAME = 280

#Menu ranking
X_MARGIN_BACK = 20
Y_MARGIN_BACK = 3
SIZE_TEXT_BACK = 20
X_IMG_RANKING = 275
SIZE_TEXTO = 27

#Botones game over
WIDTH_BUTTON_G = 70
HEIGHT_BUTTON_G = 70
X_BUTTON1_G = 250 
X_BUTTON2_G = 450  
Y_BUTTON_G = 605
FRAME_BUTTON_G = 4
X_TEXT_CONTINUE = 300
Y_TEXT_CONTINUE = 500
Y_BUTTON_YES_NO = 15
X_BUTTON_YEZ = 7
X_BUTTON_NO = 13

#Boron pause
WIDTH_BUTTON_PAUSE = 50
HEIGHT_BUTTON_PAUSE = 25
X_PAUSE = 760  
Y_PAUSE = 0
FRAME_PAUSE = 0

#Boron play
WIDTH_BUTTON_PLAY = 300
HEIGHT_BUTTON_PLAY = 150
X_PLAY = 275  
Y_PLAY = 300
FRAME_PLAY = 0

#Boron back
WIDTH_BUTTON_BACK = 100
HEIGHT_BUTTON_BACK = 30
X_BACK = 380 
FRAME_BACK = 0

#Boron accept
WIDTH_BUTTON_ACCEPT = 100
HEIGHT_BUTTON_ACCEPT = 30
X_ACCEPT = 340  
Y_ACCEPT = 360
SPEED_BUTTON_ACCEPT = 0
FRAME_ACCEPT = 0

#Naves
WIDTH_NAVE = 50
HEIGHT_NAVE = 45
Y_NAVE_E = -20
SPEED_EXPLO_NAVE_E = 30
X_MARGIN_NAVE_E = 65
Y_MARGIN_NAVE_E = 65
INTERVAL_SHOT = 2000
WIDTH_BULLET = 15
HEIGHT_BULLET = 33
SPEED_BULLET_NAVE_P = 7 
TIME_NOT_VISIBLE = 100
NAVE_P_X = 400
NAVE_P_Y = 640
SPEED_P = 0
SPEED_CURSOR = 500
SPEED_SHOT = 400

#Meteoritos
WIDTH_METEORITE = 80
HEIGHT_METEORITE = 80
Y_METEORITE = -20
SPEED_METEORITE = 70
X_MARGIN_MET = 40
Y_MARGIN_MET = 40
SPEED_METEORITE_EXPLOSION = 30
COLUMN_IMG_METEORITE = 8
ROW_IMG_METEORITE = 8
SPEED_CREATE_METEORITE = 8000

#Explosion
WIDTH_EXPLOSION = 150
HEIGHT_EXPLOSION = 150
COLUMN_IMG_EXPLO = 8
ROW_IMG_EXPLO = 6

#Balas
WIDTH_BALA = 15
HEIGHT_BALA = 33

#Texto
X_NOMBRE = 150
Y_NOMBRE = 630
X_SCORE = 400
Y_SCORE = 630

#Imagenes
IMG_BULLET = pygame.image.load("C:/Juego_galaxy/imagen_bala.png")
IMG_GALAXY = pygame.transform.scale(pygame.image.load("C:/Juego_galaxy/fondo.png"), (WIDTH_PANTALLA, HEIGHT_PANTALLA))
IMG_NAVE1 = pygame.transform.scale(pygame.image.load("C:/Juego_galaxy/nave1.png"), (WIDTH_NAVE, HEIGHT_NAVE + 5))
IMG_NAVE2 = pygame.transform.scale(pygame.image.load("C:/Juego_galaxy/nave2.png"), (WIDTH_NAVE, HEIGHT_NAVE + 5))
IMG_NAVE3 = pygame.transform.scale(pygame.image.load("C:/Juego_galaxy/nave3.png"), (WIDTH_NAVE, HEIGHT_NAVE + 5))
IMG_NAVE4 = pygame.transform.scale(pygame.image.load("C:/Juego_galaxy/nave4.png"), (WIDTH_NAVE, HEIGHT_NAVE + 5))
IMG_NAVE5 = pygame.transform.scale(pygame.image.load("C:/Juego_galaxy/nave5.png"), (WIDTH_NAVE, HEIGHT_NAVE + 5))
IMG_NAVE_PRINCIPAL = pygame.transform.scale(pygame.image.load("C:/Juego_galaxy/nave.png"), (WIDTH_NAVE, HEIGHT_NAVE + 5))
IMG_EXPLOSION = pygame.image.load("C:/Juego_galaxy/explosion.png")
IMG_LIST_NAVES_E = [IMG_NAVE1, IMG_NAVE2, IMG_NAVE3, IMG_NAVE4, IMG_NAVE5]
IMG_TITLE_GALAXY = pygame.image.load("C:/Juego_galaxy/galaxy.png")
IMG_GAME_OVER = pygame.transform.scale(pygame.image.load("C:/Juego_galaxy/img_game_over.png"), (WIDTH_PANTALLA, HEIGHT_PANTALLA))
IMG_TOP_10 = pygame.transform.scale(pygame.image.load("C:/Juego_galaxy/TOP_10.png"), (300, 300))
IMG_BUTTON_PAUSE = pygame.transform.scale(pygame.image.load("C:/Juego_galaxy/button_pause.png"), (50, 25))
IMG_BUTTON_PLAY = pygame.transform.scale(pygame.image.load("C:/Juego_galaxy/button_play.png"), (275, 150))
IMG_METEORITE = pygame.image.load("C:/Juego_galaxy/meteorito.png")

EXPLOSION_DELAY = 800