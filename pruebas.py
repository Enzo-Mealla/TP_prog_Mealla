# import json
import pygame
from Constantes import *
pygame.init

# def generar_json(nombre_archivo:str,lista:list) -> bool: 
#     "genera un archivo json con informacion del jugador"
#     retorno = True
#     with open(nombre_archivo, 'r') as archivo: 
#         lista_vieja = json.load(archivo)

#     print(lista_vieja)

#     #Recorremos las filas del alumno de la izquierda
#     for fil_i in range(len(lista_vieja)-1):
#         #Recorremos las filas de los alumnos de la derecha
#         for fil_j in range(fil_i+1,len(lista_vieja)):
#             #Comparo las notas
#             if lista_vieja[fil_i]["puntuacion"] < lista_vieja[fil_j]["puntuacion"]:
#                 #Ocurre un intercambio del alumno completo (fila completa)
#                 aux_alumno = lista_vieja[fil_i]
#                 lista_vieja[fil_i] = lista_vieja[fil_j]
#                 lista_vieja[fil_j] = aux_alumno

#     print("########################################################################################")
#     print(lista_vieja)

#     if lista != None:
#         lista_vieja.extend(lista)
            
#         if type(lista) == list and len(lista) > 0:
#             with open(nombre_archivo,"w") as archivo:
#                 json.dump(lista_vieja,archivo,indent=4)
#             retorno = True
#         else:
#             retorno = False
        
#     return lista_vieja

# lista = generar_json("Partidas.json",None)


# print("########################################################################################")

# print(len(lista))



carta_pregunta = {}
carta_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
carta_pregunta["rectangulo"] = carta_pregunta["superficie"].get_rect()
imagen_juego = pygame.image.load("imagenes/papel.png")
imagen_juego.get_rect()
carta_pregunta["imagen"] = pygame.transform.scale(imagen_juego,TAMAÑO_PREGUNTA)

cartas_respuestas = []


print(pygame.Surface(TAMAÑO_PREGUNTA))
print(imagen_juego)