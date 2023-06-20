import sys, pygame
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

pygame.init()
pygame.display.set_caption("Juego Galaxy")

#Sonido
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
LASER = pygame.mixer.Sound("C:/Juego_galaxy/disparo.ogg")
EXPLOSION = pygame.mixer.Sound("C:/Juego_galaxy/explosion.wav")
BACKGROUND_SOUND = pygame.mixer.Sound("C:/Juego_galaxy/musica.ogg")
BACKGROUND_SOUND.play(loops= -1)


while continuar:
    
    start_menu = menu("PLAY", "RANKING", WIDTH_TITLE, HEIGHT_TITLE, IMG_TITLE_GALAXY, True)
    game_over_menu = Game_over("YES", "NO", WIDTH_PANTALLA, HEIGHT_PANTALLA, IMG_GAME_OVER, False)
    nave_p = Nave_p(WIDTH_NAVE, HEIGHT_NAVE, NAVE_P_X, NAVE_P_Y, SPEED_P, IMG_NAVE_PRINCIPAL)
    rect_line = pygame.Rect(X_CURSOR, Y_CURSOR, WIDTH_CURSOR, HEIGHT_CURSOR)
    list_naves = []
    list_bullet = []
    list_bullet_e = []
    list_collision = []
    list_meteorite = []
    score = 0
    running = True

    while running:   
        
        time_current = pygame.time.get_ticks()
        key = pygame.key.get_pressed()
        list_event = pygame.event.get()
        time_accumulator += CLOCK.tick()
        pressed_mouse = pygame.mouse.get_pressed()
        event = pygame.event.poll()
        y_button_atras = 230

        #Eventos
        for event in list_event:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP and start_play == True:
                #Lectura de boton espacio
                if time_current - time_last_bullet >= SPEED_SHOT:
                    time_last_bullet = time_current
                    nave_p.button_space(key, list_bullet, LASER)

        y_fondo = update_background_position(y_fondo)

        #Muestro el fondo
        update_screen(IMG_GALAXY, X_FONDO, y_fondo)
        update_screen(IMG_GALAXY, X_FONDO, y_fondo - SCREEN.get_height())

        #Menu inicio
        if start_menu.flag == True:
            draw_menu_play(start_menu) #Dibujar menu
            start_menu.pressed_button_menu(pressed_mouse, list_flag) #Lectura de los botones del inicio
        
        if list_flag[0] == True: #Ingresar nombre
            start_menu.flag = False
            draw_menu_set_name(button_accept)
            input_name = recorrer_event(list_event, input_name, rect_line) #Leer las letras que aprieta
            if rect_line.x < 275:
                rect_line.x = 275
            draw_text(input_name, X_INPUT_NAME, Y_INPUT_NAME) #Dibujar el nombre mientras lo ingresa
            time_speed = draw_cursor(time_current, time_speed, rect_line, SPEED_CURSOR) #Dibujo el cursor
            validar = pressed_button_accept(pressed_mouse, button_accept, key) #Lee el boton accept para comenzar el juego
            if validar == True and len(input_name) > 0:
                start_play = True
                list_flag[0] = False
        elif list_flag[1] == True: #Mostrar ranking
            start_menu.flag = False
            show_ranking(y_button_atras, button_back) #Muestra los puntajes
            start_menu.flag = pressed_button_back(button_back, pressed_mouse, list_flag) #Lee el boton back para volver al menu
        elif list_flag[2] == True: #Salir del juego
            running = False     
            continuar = False

        #Menu game over
        if game_over_menu.flag == True:      
            menu_game_over(start_menu, game_over_menu)
            start_menu.flag = game_over_menu.pressed_button_game_over(pressed_mouse)
            if start_menu.flag == True:
                continuar = True
                running = False
            elif start_menu.flag == False:
                continuar = False
                running = False

        if flag_pause == True:
            SCREEN.blit(button_play.img, (button_play.rect.x, button_play.rect.y))
            if pressed_mouse[0] == 1:
            #Realiza alguna acción cuando se presiona el botón izquierdo del mouse
                if button_play.rect.collidepoint(pygame.mouse.get_pos()):   
                    flag_pause = False    

        #Inicio juego
        if start_play == True and flag_pause == False:

            SCREEN.blit(button_pause.img, (button_pause.rect.x, button_pause.rect.y)) #Muestro el boton pausa

            if pressed_mouse[0] == 1: #Realiza alguna acción cuando se presiona el botón izquierdo del mouse
                if button_pause.rect.collidepoint(pygame.mouse.get_pos()):   
                    flag_pause = True   #Pauseo el juego

            if nave_p.visible == True: #Muestro la nave principal si esta visible
                SCREEN.blit(nave_p.img, nave_p.rect)
            elif time_current - time_collision >= TIME_NOT_VISIBLE:
                nave_p.visible = True

            #Mover nave principal
            nave_p.update_p(key)
            
            #Crear naves enemigas
            if time_accumulator >= delay_time:
                x_nave_e = random.randint(2, 3)
                img = IMG_LIST_NAVES_E[random.randint(0, 4)]
                list_naves.append(nave_e(list_img_explosion, WIDTH_NAVE, HEIGHT_NAVE, Y_NAVE_E, x_nave_e, img)) #Hago una lista de naves
                time_accumulator = 0

            for e_list in list_naves:
                e_list.update_e() #Mover nave enemigas         
                update_screen(e_list.img, e_list.rect.x, e_list.rect.y) #Mostrar naves enemigas           
                e_list.shoot(list_bullet_e, time_current) #Disparar balas enemigas
                if e_list.rect.y > 800:
                    list_remove.append(e_list)

            for e_bullet in list_bullet:
                e_bullet.update_p() #Mover balas de la nave principal
                update_screen(e_bullet.img, e_bullet.rect.x, e_bullet.rect.y) #Actualizar pantalla
                for e_nave in list_naves:            
                    if e_bullet.rect.colliderect(e_nave.rect): #Chequear colisiones 
                        if time_current - last_time >= EXPLOSION_DELAY:
                            EXPLOSION.play() #Emite sonido de explosion
                            last_time = time_current
                        list_collision.append(e_nave)
                        if e_nave.flag_collision == False:
                            score += 10
                            list_remove.append(e_nave)
                            list_remove.append(e_bullet)
                list_remove.append(e_bullet) if e_bullet.rect.y < 0 else None

            texto = "Vidas: " + str(nave_p.lives) #Muestro la cantidad de vidas restantes
            draw_text(texto, 0, 0)
            draw_text(str(score), WIDTH_PANTALLA // 2, 0)

            for e_list in list_bullet_e:           
                e_list.update_e() #Mover balas de naves_e     
                if e_list.rect.colliderect(nave_p.rect): #Chequear colisiones de balas enemigas contra la nave principal
                    nave_p.lives -= 1 #Le resto una vida a la nave principal
                    time_collision = time_current #Guardo el tiempo del impacto para el efecto colision de la nave principal
                    list_remove.append(e_list)
                    nave_p.visible = False
                if e_list.rect.y > 800:
                    list_remove.append(e_list)           
                update_screen(e_list.img, e_list.rect.x, e_list.rect.y) #Actualizar pantalla
    
            if nave_p.lives < 1: #Cuando perdes todas las vidas
                game_over_menu.flag = True #Activo el menu game over
                start_play = False #Desactivo el juego
                list_data = data_base(input_name, score) #Ingreso a la base de datos el nuevo puntaje 
                input_name = ""

            if time_current - time_last >= SPEED_CREATE_METEORITE: #Creo meteoritos y hago una lista
                list_meteorite.append(meteorite(list_img_meteorite, WIDTH_METEORITE, HEIGHT_METEORITE, Y_METEORITE, SPEED_METEORITE, list_img_explosion)) 
                time_last = time_current

            for e_bala in list_bullet:
                for e_mete in list_meteorite:
                    if e_bala.rect.colliderect(e_mete.rect): #Chequeo colision de balas contra meteoritos
                        EXPLOSION.play()
                        e_mete.lives -= 1 #Le resto una vida al meteorito
                        if e_mete.lives == 0:
                            score += 50 #Explotar el meteorito suma 50 puntos
                            list_collision.append(e_mete)
                            list_remove.append(e_mete)
                        list_remove.append(e_bala)
            
            for e_list in list_meteorite:
                e_list.update(time_current) #Muevo meteoritos
                if e_list.rect.colliderect(nave_p.rect): #Chequeo colision del meteorito contra la nave principal
                    nave_p.visible = False
                    nave_p.lives -= 2 #La colision le resta dos vidas a la nave principal 
                    EXPLOSION.play()
                    time_collision = time_current #Guardo el tiempo del impacto para el efecto colision de la nave principal
                    list_meteorite.remove(e_list)
                if e_list.y > 800:
                    list_meteorite.remove(e_list)

            for e_list in list_collision:
                e_nave.explosion.update(e_list, time_current) #Se muestra los sprites de la explosion
                if e_nave.explosion.position == len(e_list.explosion.list_img) - 30:
                    list_collision.remove(e_list)

            # Eliminar naves enemigas y balas
            remove_list(list_remove, list_naves, list_bullet_e, list_bullet, list_meteorite)

            time_accumulator += CLOCK.tick(return_time)
        pygame.display.flip()
pygame.quit()
