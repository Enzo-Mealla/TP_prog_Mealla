# import json
import pygame
from Constantes import *
pygame.init
import os

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



# carta_pregunta = {}
# carta_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
# carta_pregunta["rectangulo"] = carta_pregunta["superficie"].get_rect()
# imagen_juego = pygame.image.load("imagenes/papel.png")
# imagen_juego.get_rect()
# carta_pregunta["imagen"] = pygame.transform.scale(imagen_juego,TAMAÑO_PREGUNTA)

# cartas_respuestas = []


# print(pygame.Surface(TAMAÑO_PREGUNTA))
# print(imagen_juego)


def mostrar_diccionario(diccionario) -> None:
    for clave,valor in diccionario.items():
        print(f"{clave.title().replace("_"," ")} : {valor}")

def mostrar_lista_diccionarios(lista:list) -> bool:
    retorno = False
    for elemento in lista:
        retorno = True
        mostrar_diccionario(elemento)
        print("")
        
    return retorno

def crear_diccionario_alumno(lista_valores:list) -> dict:
    preguntas = {}
    preguntas["pregunta"] = lista_valores[0]
    preguntas["respuesta_1"] = lista_valores[1]
    preguntas["respuesta_2"] = lista_valores[2]
    preguntas["respuesta_3"] = lista_valores[3]
    preguntas["respuesta_4"] = lista_valores[4]
    preguntas["respusta_correcta"] = lista_valores[5]
    preguntas["imagen_juego"] = lista_valores[6]
    
    return preguntas

def leer_csv_alumnos(nombre_archivo:str,lista_alumnos:list) -> bool:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r") as archivo:
            #Falsa lectura -> Para evitar recorrer en el for de abajo, la cabecera
            archivo.readline()
            
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")
                mi_alumno = crear_diccionario_alumno(lista_valores)
                lista_alumnos.append(mi_alumno)
        retorno = True
    else:
        retorno = False
        
    return retorno


lista_alumnos = []  
leer_csv_alumnos("preguntas.csv",lista_alumnos)
mostrar_lista_diccionarios(lista_alumnos)    