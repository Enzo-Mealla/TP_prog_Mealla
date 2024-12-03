import pygame
from Funciones import *
#from Preguntas import *  #anular esto
from Constantes import *


pygame.init()


carta_pregunta = {}
carta_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
carta_pregunta["rectangulo"] = carta_pregunta["superficie"].get_rect()
imagen_juego = pygame.image.load("imagenes/papel.png")
imagen_juego.get_rect()
carta_pregunta["imagen"] = pygame.transform.scale(imagen_juego,TAMAÑO_PREGUNTA)

cartas_respuestas = []

for i in range(4): #puse esto en 4
    carta_respuesta = {}
    carta_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    carta_respuesta["rectangulo"] = carta_respuesta["superficie"].get_rect()
    carta_respuesta["eliminada"] = False
    imagen_respuesta = pygame.image.load("imagenes/respuestas.png")
    carta_respuesta["imagen"] = pygame.transform.scale(imagen_respuesta,TAMAÑO_RESPUESTA)

    cartas_respuestas.append(carta_respuesta)





indice = 0 #Todo dato inmutable en la funcion que muestra esa ventana, lo tengo que definir como global

lista_preguntas = []
leer_csv_preguntas("preguntas.csv",lista_preguntas)
mezclar_lista(lista_preguntas)
bandera_respuesta = False #Todo dato inmutable en la funcion que muestra esa ventana, lo tengo que definir como global

#parte del bonus
font = pygame.font.Font(None, 36)
image1, images, image1_rect,sin_bonus,nombres_imagenes = cargar_imagenes_bonus()
x1, y1, button1_rect, button2_rect,button3_rect = calcular_posicion(image1_rect)
colors = {'button': (0, 200, 0), 'hover': (0, 255, 0), 'text': (255, 255, 255)}
    
x2 = x1 + (image1_rect.width - images[0].get_rect().width) // 2
y2 = y1 + (image1_rect.height - images[0].get_rect().height) // 2
current_image_index = 0
flag_extra_vida = False
flag_x2 = False


def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict,inicio_tiempo,bandera_contador) -> str:
    global indice
    global bandera_respuesta  
    global current_image_index
    global flag_extra_vida
    global flag_x2
    global image1
    global images
    global image1_rect
    global sin_bonus
    global nombres_imagenes
    
    retorno = "juego"
    fondo = pygame.image.load("imagenes/fondo_juego.png")
    fondo = pygame.transform.scale(fondo,VENTANA)
    
    imagen_juego = pygame.image.load("imagenes/papel.png")
    carta_pregunta["imagen"] = pygame.transform.scale(imagen_juego,TAMAÑO_PREGUNTA)

    pregunta_actual = lista_preguntas[indice]
    if bandera_respuesta:
        pygame.time.delay(500)
        bandera_respuesta = False
    
    
    for i in range(len(cartas_respuestas)):
        cartas_respuestas[i]["superficie"].fill(COLOR_AZUL)
        cartas_respuestas[i]["superficie"].set_colorkey(COLOR_AZUL)

    for evento in cola_eventos:
         
        if evento.type == pygame.QUIT:
            retorno = "salir"  

        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    if cartas_respuestas[i]["eliminada"] == False:
                        respuesta_seleccionada = (i + 1)
                        
                        print(f"LE DIO CLICK A LA RESPUESTA : {respuesta_seleccionada}")
                        
                        if verificar_respuesta(datos_juego,pregunta_actual,respuesta_seleccionada,flag_extra_vida,flag_x2):
                            print("RESPUESTA CORRECTA")
                            #Ustedes van a manejar una imagen para esto
                            cartas_respuestas[i]["superficie"].fill(COLOR_VERDE)
                            cartas_respuestas[i]["superficie"].set_alpha(128)
                            CLICK_ACIERTO.play()
                        else:
                            
                            print("RESPUESTA INCORRECTA")
                            
                            #Ustedes van a manejar una imagen para esto
                            cartas_respuestas[i]["superficie"].fill(COLOR_ROJO)
                            cartas_respuestas[i]["superficie"].set_alpha(128)
                            if datos_juego["vidas"] == 0:
                                image1, images, image1_rect,sin_bonus,nombres_imagenes = cargar_imagenes_bonus()
                                
                                retorno = "terminando"
                            CLICK_ERROR.play()
                        
                        bandera_contador = False
                        if flag_extra_vida == False:
                            indice +=1
                        
                        if indice == len(lista_preguntas):
                            indice = 0
                            mezclar_lista(lista_preguntas)
                        
                        for carta in cartas_respuestas:   #restablece a false
                            carta["eliminada"] = False  # Restablecer el flag

                    flag_extra_vida = False
                    flag_x2 = False
                    bandera_respuesta = True
            if images:  # Solo permitir interacción si hay imágenes disponibles
            # Navegación en imágenes
                if button1_rect.collidepoint(evento.pos):
                    current_image_index = (current_image_index - 1) % len(images)
                elif button2_rect.collidepoint(evento.pos):
                 current_image_index = (current_image_index + 1) % len(images)
                elif button3_rect.collidepoint(evento.pos):
                    print(f"Imagen eliminada: {images[current_image_index]}")
                    print(f"Imagen eliminada: {nombres_imagenes[current_image_index]}")
                    indice,flag_extra_vida,flag_x2 = funcion_poder(nombres_imagenes,current_image_index,cartas_respuestas,pregunta_actual,indice,flag_extra_vida,flag_x2)
                        
                    images.pop(current_image_index)
                    nombres_imagenes.pop(current_image_index)
                    

                    # Ajustar el índice para evitar desbordamientos
                    if current_image_index >= len(images):
                        current_image_index = 0

                    if not images:
                        print("No hay más imágenes disponibles.")
    
    
    tiempo_restante, inicio_tiempo = contar_tiempo(inicio_tiempo, datos_juego["tiempo"]) 

    if tiempo_restante < 0:
        bandera_contador = False
        for carta in cartas_respuestas:   #restablece a false
            carta["eliminada"] = False  # Restablecer el flag

        if flag_extra_vida == False:
            indice +=1 #cambia pantalla preguntas
            datos_juego["vidas"] -= 1
            if datos_juego["vidas"] == 0:
                image1, images, image1_rect,sin_bonus,nombres_imagenes = cargar_imagenes_bonus()
                                
                retorno = "terminando"
        else:
            flag_extra_vida = False #se consume el extravida

    
    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(fondo,(0,0))
    
    
    


    mostrar_texto(carta_pregunta["imagen"],pregunta_actual["pregunta"],(20,20),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[0]["superficie"],pregunta_actual["respuesta_1"],(5,17),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[1]["superficie"],pregunta_actual["respuesta_2"],(5,17),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[2]["superficie"],pregunta_actual["respuesta_3"],(5,17),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[3]["superficie"],pregunta_actual["respuesta_4"],(5,17),FUENTE_22,COLOR_NEGRO)

    pantalla.blit(carta_pregunta["imagen"],(40,75)) 
    
    for i in range(len(cartas_respuestas)):
        if cartas_respuestas[i]["eliminada"] == False:
            pantalla.blit(carta_respuesta["imagen"],(1,735-70*i))
            cartas_respuestas[i]["rectangulo"] = pantalla.blit(cartas_respuestas[i]["superficie"],(1,735-70*i))#r totales
            cartas_respuestas[i]["superficie"].set_alpha(256) 
       

    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(550,540),fuente,COLOR_MARRON)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['vidas']}",(550,570),fuente,COLOR_MARRON)
    mostrar_texto(pantalla,f"TIEMPO: {tiempo_restante}",(550,600),fuente,COLOR_MARRON)
    # Dibujar la imagen central (image1) y la imagen actual seleccionada (image2)
    pantalla.blit(image1, (x1, y1))
    if images:
        pantalla.blit(images[current_image_index], (x2, y2))
    else:
        # Mostrar un mensaje indicando que no hay imágenes disponibles
       pantalla.blit(sin_bonus, (x2, y2))

    # Dibujar los botones
    dibujar_boton_bonus(pantalla, font, button1_rect, '<-', colors['button'], colors['text'])
    dibujar_boton_bonus(pantalla, font, button2_rect, '->', colors['button'], colors['text'])
    dibujar_boton_bonus(pantalla, font, button3_rect, 'O', colors['button'], colors['text'])
    




        # Cargar imagen si existe
    tiene_imagen = pregunta_actual["tiene_imagen"]
    imagen = None
    if tiene_imagen != "none":
        if tiene_imagen:
            try:
                nombre_imagen = f"imagenes/{pregunta_actual['tiene_imagen']}.png"  # Ruta de la imagen
                imagen = pygame.image.load(nombre_imagen)
                imagen = pygame.transform.scale(imagen, (250, 250))  # Ajustar tamaño
            except FileNotFoundError:
                print(f"No se encontró la imagen para la pregunta: {pregunta_actual['pregunta']}")

     # Mostrar la imagen si existe
    if imagen:
         pantalla.blit(imagen, (250, 150))
    
    return retorno, bandera_contador