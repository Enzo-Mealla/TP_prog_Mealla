import pygame
from Constantes import *
from Funciones import *
import json
import datetime
pygame.init()

caja_texto = {}
caja_texto["superficie"] = pygame.Surface(CUADRO_TEXTO)
caja_texto["rectangulo"] = caja_texto["superficie"].get_rect()
caja_texto["superficie"].fill(COLOR_AZUL)
caja_texto["superficie"].set_colorkey(COLOR_AZUL)
nombre = ""#Inmutable

fecha_hora_actual = datetime.datetime.now()
fecha_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S") 


def mostrar_juego_terminado(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global nombre
    retorno = "terminando"
    fondo_terminado = pygame.image.load("imagenes/fondo_terminado.jpg")
    fondo_terminado = pygame.transform.scale(fondo_terminado,VENTANA)
    tabla_puntaje = pygame.image.load("imagenes/barra estadisticas.jpg")
    tabla_puntaje = pygame.transform.scale(tabla_puntaje,(340,150))
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pass
        if evento.type == pygame.KEYDOWN:
            #letra_presionada = chr(evento.key)
            letra_presionada = pygame.key.name(evento.key)
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            
            if letra_presionada == "space":
                nombre += " "
                
            if letra_presionada == "backspace" and len(nombre) > 0:
                nombre = nombre[0:-1] #Me elimina automaticamente el último
                caja_texto["superficie"].fill(COLOR_AZUL)
            if len(nombre) >= 10:

                nombre = nombre[0:-1] 
                nombre = nombre[0:10]
                caja_texto["superficie"].fill(COLOR_AZUL)
            if len(letra_presionada) == 1:
                if bloc_mayus != 0:
                    nombre += letra_presionada.upper()
                else:
                    nombre += letra_presionada

            if letra_presionada == "return":
                
                datos_juego["usuario"] = nombre
                datos_juego["fecha y hora"] = fecha_formateada
                generar_json("Partidas.json",[datos_juego])
                reiniciar_estadisticas(datos_juego)
                caja_texto["superficie"].fill(COLOR_AZUL)
                nombre = ""
                retorno = "menu"
            
        elif evento.type == pygame.QUIT:
            retorno = "salir"
    

        
    
    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(fondo_terminado,(0,0))
    pantalla.blit(tabla_puntaje,(420,300))
    caja_texto["rectangulo"] = pantalla.blit(caja_texto["superficie"],(515,400))
    mostrar_texto(pantalla,f"Nombre:",(425,400),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(caja_texto["superficie"],f"{nombre}",(0,0),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(pantalla,"____________",(515,400),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(pantalla,f"Puntaje: {datos_juego["puntuacion"]} puntos",(425,330),FUENTE_30,COLOR_NEGRO)
    
    return retorno




