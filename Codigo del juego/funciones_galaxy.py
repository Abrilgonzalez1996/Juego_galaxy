import pygame, sqlite3
from button import *
from nave_e import *
from colores import *
from variables import *
from constantes import *

#Cambiar la pisicion del fondo
def update_background_position(y_fondo):
    y_fondo += 1
    if y_fondo >= SCREEN.get_height():
        y_fondo = 0
    return y_fondo

#Actualizar pantalla
def update_screen(img, x, y):
    SCREEN.blit(img, (x, y))

def draw_menu_play(start_menu):
    start_menu.draw_img(X_TITLE, Y_TITLE) #Dibujo el titulo Galaxy
    start_menu.button_play.draw_text(MARGIN_TEXT_X_ACCEPT, MARGIN_TEXT_Y, SIZE) #Dibujo el boton play
    start_menu.button_ranking.draw_text(MARGIN_TEXT_X_RANKING, MARGIN_TEXT_Y, SIZE) #Dibujo el boton ranking
    start_menu.button_quit.draw_text(MARGIN_TEXT_X_QUIT, MARGIN_TEXT_Y, SIZE) #Dibujo el boton quit
    top_score() #Busco el puntaje mas alto

def draw_menu_set_name(button_accept):
    draw_text(TITLE_SET_NAME, X_TITLE_SET_NAME, Y_TITLE_SET_NAME) #Dibujar el "Ingrese el nombre"
    pygame.draw.rect(SCREEN, WHITE, (X_RECT_NAME, Y_RECT_NAME, WIDCH_RECT_NAME, HEIGHT_RECT_NAME), FRAME_SET_NAME) #Dibuja el rectangulo para escribir
    button_accept.draw_text(X_MARGIN_ACCEPT, Y_MARGIN_ACCEPT, SIZE_TEXT_ACCEPT) #Dibuja el texto del boton aceptar

def draw_text(text, x, y): #Dibuja texto en la pantalla
    font = pygame.font.SysFont("serif", SIZE)
    text = font.render(text, True, WHITE)
    SCREEN.blit(text, (x, y)) 

def draw_cursor(time_current, time_speed, rect_line, speed_cursor): #Indica donde escribir para ingresar el nombre 
    if time_current - time_speed[0] >= speed_cursor:
            time_speed[0] = time_current
            time_speed[1] = not time_speed[1]
    if time_speed[1] == True:
        pygame.draw.rect(SCREEN, WHITE, rect_line) #Dibujo la linea
    return time_speed
    
def pressed_button_accept(pressed_mouse, button_aceptar, key): #Lectuta del boton que acepta el nombre ingresado
    retorno = False
    if pressed_mouse[0] == 1 or key[pygame.K_RETURN] == True:
        if button_aceptar.rect.collidepoint(pygame.mouse.get_pos()) or key[pygame.K_RETURN] == True:
            button_aceptar.style_button(True, 4, WHITE) #Cambia el estilo del boton cuando presionas 
    if (pressed_mouse[0] == 0  and key[pygame.K_RETURN] == False) and button_aceptar.pressed == True:
        button_aceptar.style_button(False, 0, WHITE) #Cambia el estilo del boton cuando soltas
        retorno = True
    return retorno

def recorrer_event(list_event, input_name, rect): #Indica los botones presionados, se llama cuando hay que ingresar texto
    for event in list_event:
        if event.type == pygame.KEYDOWN:
            if len(input_name) < 17:
                if event.key == pygame.K_BACKSPACE: #Se presiona el boton borrar
                    input_name = input_name[0:-1]
                    font = pygame.font.Font(None, SIZE_TEXTO)
                    surface = font.render(event.unicode, True, WHITE)
                    rect.x -= (surface.get_width() + 4) #Mueve el cursor mientras se escribe 
                elif event.key != pygame.K_RETURN: #Guarda el valor de todos los botones menos el enter
                    input_name += event.unicode
                    font = pygame.font.Font(None, SIZE_TEXTO)
                    surface = font.render(event.unicode, True, WHITE)
                    rect.x += (surface.get_width() + 4) #Mueve el cursor mientras se escribe 
    return input_name

def show_ranking(y, button_back): #Muestro el puntaje guardado en la base de datos
    try:
        SCREEN.blit(IMG_TOP_10, (X_IMG_RANKING, 0))
        y = read_date_base(y) #Toma el valor de Y del ultimo score de referencia 
        button_back.y = y + 30 #Le sumo 30 a Y para que el boton quede simpre debajo del score 
        button_back.rect.y = y + 30
        button_back.draw_text(X_MARGIN_BACK, Y_MARGIN_BACK, SIZE_TEXT_BACK) 
    except:
        print("Base de datos vacia")
    else: 
        button_back.draw_text(X_MARGIN_BACK, Y_MARGIN_BACK, SIZE_TEXT_BACK) 

def read_date_base(y): #Leo la base de datos y la ordeno de manera descendente
    with sqlite3.connect("tabla_score.db") as conexion:
        cursor = conexion.execute("SELECT nombre, score FROM score ORDER BY score DESC")
        rows = cursor.fetchall()
        nombre = ""
        for i in range(len(rows)):
            nombre +=  str(i + 1) + "°  " + rows[i][0]
            score =  str(rows[i][1])
            draw_text(nombre, 300, y)
            draw_text(score, 500, y)
            y += 30
            nombre = ""
            score = ""
            if i == 9:
                break
    return y

def pressed_button_back(button_back, pressed_mouse, list_flag): #Lectura del boton atras cuando ingresar a ver el ranking
    if pressed_mouse[0] == 1:
        if button_back.rect.collidepoint(pygame.mouse.get_pos()):
            button_back.style_button(True, 4, WHITE)
    if pressed_mouse[0] == 0 and button_back.pressed == True:
        button_back.style_button(False, 0, WHITE)
        list_flag[1] = False
        return True

def menu_game_over(start_menu, game_over_menu):
    start_menu.flag = True
    game_over_menu.draw_img(0, 0)
    draw_text("CONTINUE?", X_TEXT_CONTINUE, Y_TEXT_CONTINUE)
    game_over_menu.button_yes.draw_text(X_BUTTON_YEZ, Y_BUTTON_YES_NO, SIZE)
    game_over_menu.button_no.draw_text(X_BUTTON_NO, Y_BUTTON_YES_NO, SIZE)

def get_surface_sprite_sheet(columns, rows, img, widgh, height):
    list = []
    fotograma_width = int(img.get_width() / columns)
    fotograma_height = int(img.get_height() / rows)
    x = 0
    for column in range(columns):
        for row in range(rows):
            x = fotograma_width * column
            y = fotograma_height * row
            surface_fotograma = img.subsurface(x, y, fotograma_width, fotograma_height)
            surface_fotograma = pygame.transform.scale(surface_fotograma, (widgh, height))
            list.append(surface_fotograma)
    return list

def remove_list(list_remove, list_naves, list_bullet_e, list_bullet, list_meteorite): #Elimino elementos de la lista
    for e_list in list_remove:
        if e_list in list_naves:
            list_naves.remove(e_list)
        if e_list in list_bullet_e:
            list_bullet_e.remove(e_list)
        if e_list in list_bullet:
            list_bullet.remove(e_list)
        if e_list in list_meteorite:
            list_meteorite.remove(e_list)

def data_base(nombre, score): #Creo una base de datos e ingreso nuevos puntajes
    with sqlite3.connect("tabla_score.db") as conexion:
        try:
            sentencia = ''' create  table score
            (
            id integer primary key autoincrement,
            nombre text,
            score real
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla score")                       
        except sqlite3.OperationalError:
            print("La tabla score ya existe")

        try:
            conexion.execute("insert into score(nombre, score) values (?,?)", (nombre, score)) #Insertar datos
            conexion.commit() # Actualiza los datos realmente en la tabla
        except:
            print("Error")


def top_score(): #Busco el puntaje mas alto
    try:
        with sqlite3.connect("tabla_score.db") as conexion:
            cursor = conexion.cursor()
            cursor = conexion.execute("SELECT nombre, score FROM score ORDER BY score DESC") #Ordenar de mayor a menor
            row = cursor.fetchone()
            nombre = str(row[0]).capitalize()
        draw_text("Top Score: " + nombre, X_NOMBRE, Y_NOMBRE)
        draw_text(str(row[1]), len(nombre) + X_SCORE, Y_SCORE)
    except:
        print("Base de datos vacia")




        
        
    








