from Constantes import *
import random
import pygame
import json
import datetime
import csv
import time
import os

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words. 
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    
    for line in words:
        
        for word in line:
    
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
        


    
    
    
def mezclar_lista(lista:list) -> None:
    random.shuffle(lista)

bandera_musica = False
def cargar_musica(datos_juego:dict,boton_mute:dict):
    global bandera_musica
    if bandera_musica == False:
                    
        boton_mute["superficie"].fill(COLOR_ROJO)
        if bandera_musica == False:
            porcentaje_coma = datos_juego["volumen_musica"] / 100  #0.5 = 50%
            pygame.mixer.music.load("musica.mp3") #Cargo musica de fondo
            pygame.mixer.music.set_volume(porcentaje_coma)
            pygame.mixer.music.play(-1)#Se ejecuta constatemente
            bandera_musica = True

    elif bandera_musica == True:
                                    
        boton_mute["superficie"].fill(COLOR_AZUL)
        bandera_musica = False
        pygame.mixer.music.stop()


def contar_tiempo(inicio_tiempo:int, tiempo_total:int):
    tiempo_transcurrido = (pygame.time.get_ticks() - inicio_tiempo) // 1000
    tiempo_restante = tiempo_total - tiempo_transcurrido
    
    return tiempo_restante, inicio_tiempo



def reiniciar_estadisticas(datos_juegos:dict) -> None:
    datos_juegos["puntuacion"] = 0
    datos_juegos["vidas"] = CANTIDAD_VIDAS
    
def verificar_respuesta(datos_juego:dict,pregunta_actual:dict,respuesta:int,flag_extra_vida:bool,flag_x2:bool) -> bool:
    """
    funcion que verifica la respuesta, las banderas flag_x2 y extra vida
    retorna una booleano siendo True respuesta correcta y false incorrecta.

    """
    if pregunta_actual["respuesta_correcta"] == respuesta:
        datos_juego["aciertos"] += 1
        if flag_x2 == True:             #chequeo de bonus x2
            datos_juego["puntuacion"] += datos_juego["P_inicial"] *2
        else:
            datos_juego["puntuacion"] += datos_juego["P_inicial"]
        retorno = True
        if datos_juego["aciertos"] == 5:
            datos_juego["vidas"] += 1
            datos_juego["aciertos"] = 0
            
    else:
        #SIN PUNTOS NEGATIVOS
        if datos_juego["puntuacion"] > datos_juego["P_fallo"]:
            datos_juego["puntuacion"] -= datos_juego["P_fallo"]
        
        #CON PUNTOS NEGATIVOS
        #datos_juego["puntuacion"] -= PUNTUACION_ERROR
        if flag_extra_vida == False: #chequeo de extra vida
            datos_juego["vidas"] -= 1 
        datos_juego["aciertos"] = 0
        
        retorno = False
    
    return retorno
    
def generar_json(nombre_archivo:str,lista:list) -> bool: 
    "genera un archivo json con informacion del jugador"
    
    with open(nombre_archivo, 'r') as archivo: 
        lista_vieja = json.load(archivo)

    if lista != None:
        lista_vieja.extend(lista)
            
        if type(lista) == list and len(lista) > 0:
            with open(nombre_archivo,"w") as archivo:
                json.dump(lista_vieja,archivo,indent=4)
        

    for fil_i in range(len(lista_vieja)-1):
        
        for fil_j in range(fil_i+1,len(lista_vieja)):
            
            if lista_vieja[fil_i]["puntuacion"] < lista_vieja[fil_j]["puntuacion"]:
                
                aux_alumno = lista_vieja[fil_i]
                lista_vieja[fil_i] = lista_vieja[fil_j]
                lista_vieja[fil_j] = aux_alumno  

    return lista_vieja


# Cargar preguntas desde el archivo CSV
# def cargar_preguntas(nombre_archivo):
#     "carga las preguntas,respuestas e imagen correspondiente de un archivo csv"
#     preguntas = []
    
#     with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
#         lector = csv.DictReader(archivo)
#         for fila in lector:
#             preguntas.append({
#                 "pregunta": fila["Pregunta"],
#                 "respuesta_1": fila["Respuesta 1"],
#                 "respuesta_2": fila["Respuesta 2"],
#                 "respuesta_3": fila["Respuesta 3"],
#                 "respuesta_4": fila["Respuesta 4"],
#                 "respuesta_correcta": int(fila["Respuesta Correcta"]),
#                 "tiene_imagen": fila["Tiene Imagen"]
#             })
#     return 

def crear_diccionario_preguntas(lista_valores:list) -> dict:
    preguntas = {}
    preguntas["pregunta"] = lista_valores[0]
    preguntas["respuesta_1"] = lista_valores[1]
    preguntas["respuesta_2"] = lista_valores[2]
    preguntas["respuesta_3"] = lista_valores[3]
    preguntas["respuesta_4"] = lista_valores[4]
    preguntas["respuesta_correcta"] = int(lista_valores[5])
    preguntas["tiene_imagen"] = lista_valores[6]
    
    return preguntas

def leer_csv_preguntas(nombre_archivo:str,lista_preguntas:list) -> bool:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r",encoding="utf-8") as archivo: # -> encoding para que acepte acentos 
            #Falsa lectura -> Para evitar recorrer en el for de abajo, la cabecera
            archivo.readline()
            
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")
                preguntas = crear_diccionario_preguntas(lista_valores)
                lista_preguntas.append(preguntas)
        retorno = True
    else:
        retorno = False
        
    return retorno





# Cargar y redimensionar imágenes
def cargar_imagenes_bonus():
    """
    carga las imagenes, las redimensiona y las pone en una lista.
    retorna la imagen principal(selector), la secundaria (bonus),
    la escala y una lista con los nombres de las imagenes
    """
    image1 = pygame.image.load('imagenes/selector.png')
    image2 = pygame.image.load('imagenes/barril.png')
    image3 = pygame.image.load('imagenes/caca.png')
    image4 = pygame.image.load('imagenes/doble_chance.png')
    image5 = pygame.image.load('imagenes/x2.png')
    sin_bonus = pygame.image.load('imagenes/sin_bonus.png')
    nombres_imagenes = ["barril","caca","doble_chance","x2"]
    # Redimensionar la imagen 1
    image1 = pygame.transform.scale(image1, DIM_BONUS)
    image1_rect = image1.get_rect()
    

    # Redimensionar las demás imágenes
    new_width, new_height = image1_rect.width // 2, image1_rect.height // 2
    sin_bonus = pygame.transform.scale(sin_bonus, (new_width, new_height)) 
    images = [
        pygame.transform.scale(img, (new_width, new_height)) 
        for img in [image2, image3, image4, image5]
    ]

    return image1, images, image1_rect, sin_bonus,nombres_imagenes

# Calcular posiciones y dimensiones de los elementos
def calcular_posicion(image1_rect):
    """
    funcion que calcula la posicion y dimensiones de la imagen principal del bonus(selector)
    haciendo que los botones dependan de esa misma coordenada 
    los datos de retorno se utilizaran en la funcion dibujar_boton_bonus()
    """
    x1, y1 = CORDS_BONUS #variable globales
    button_width, button_height = image1_rect.width // 4, image1_rect.height // 6
    button1_rect = pygame.Rect(x1, y1 + image1_rect.height, button_width, button_height)
    button2_rect = pygame.Rect(x1 + image1_rect.width - button_width, y1 + image1_rect.height, button_width, button_height)
      # Botón 3 (centrado entre los botones 1 y 2)
    button3_x = (button1_rect.right + button2_rect.left) // 2 - button_width // 2
    button3_y = y1 + image1_rect.height  # Mismo eje vertical
    button3_rect = pygame.Rect(button3_x, button3_y, button_width, button_height)

    return x1, y1, button1_rect, button2_rect,button3_rect

# Dibujar botones
def dibujar_boton_bonus(pantalla, fuente, button_rect, text, button_color, text_color):
    """
    funcion que se encarga de dibujar los botones en pantalla

    """
    pygame.draw.rect(pantalla, button_color, button_rect)
    text_surface = fuente.render(text, True, text_color)
    pantalla.blit(
        text_surface,
        (button_rect.x + (button_rect.width - text_surface.get_width()) // 2,
         button_rect.y + (button_rect.height - text_surface.get_height()) // 2)
    )
    
def eliminar_dos_opciones(pregunta_actual, cartas_respuestas):
    """
    funcion que se activa una vez activado el boton de eliminar 2 opciones
    
    """
    #calcular el indice de la repuesta correcta
    respuesta_correcta = int(pregunta_actual["respuesta_correcta"]) - 1

    # Crear una lista de índices incorrectos
        
    indices_incorrectos = []
    for i in range(len(cartas_respuestas)):
        if i != respuesta_correcta:
            indices_incorrectos.append(i) 


    # Elegir una incorrecta al azar para mantener
    incorrecta_elegida = random.choice(indices_incorrectos)

    # Determinar cuáles eliminar
    opciones_a_eliminar = []
    for i in indices_incorrectos:
        if i != incorrecta_elegida:
            opciones_a_eliminar.append(i)

    # Marcar las respuestas eliminadas visualmente
    for i in opciones_a_eliminar:
        cartas_respuestas[i]["eliminada"] = True  # Flag opcional para identificar que fue eliminada

def funcion_poder(nombres_imagenes,current_image_index,cartas_respuestas,pregunta_actual,indice,flag_extra_vida,flag_x2):
    if nombres_imagenes[current_image_index] == "caca":
        indice +=1
        for carta in cartas_respuestas:   #restablece a false
            carta["eliminada"] = False  # Restablecer el flag
                            
                         
    elif nombres_imagenes[current_image_index] == "barril":
        print("se utilizo bomba")
                        
        eliminar_dos_opciones(pregunta_actual, cartas_respuestas)
                                                
    elif nombres_imagenes[current_image_index] == "doble_chance":
        print("se utilizo doble_chance")
        flag_extra_vida = True
                        
    elif nombres_imagenes[current_image_index] == "x2":
        print("se utilizo x2")
        flag_x2 = True
    return indice, flag_extra_vida, flag_x2













