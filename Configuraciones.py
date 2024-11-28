import pygame
from Constantes import *
from Funciones import *


pygame.init()

boton_suma = {}
boton_suma["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_suma["rectangulo"] = boton_suma["superficie"].get_rect()
boton_suma["superficie"].fill(COLOR_ROJO)

boton_resta = {}
boton_resta["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_resta["rectangulo"] = boton_resta["superficie"].get_rect()
boton_resta["superficie"].fill(COLOR_ROJO)

boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)

boton_mute = {}
boton_mute["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_mute["rectangulo"] = boton_mute["superficie"].get_rect()
boton_mute["superficie"].fill(COLOR_AZUL)

sonido_anterior = 0
def mostrar_configuracion(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "configuraciones"
    
    global sonido_anterior
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] < 100:
                    CLICK_SONIDO.play()
                    datos_juego["volumen_musica"] += 5
                else:
                    CLICK_ERROR.play()
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] > 0:
                    CLICK_SONIDO.play()
                    datos_juego["volumen_musica"] -= 5
                else:
                    CLICK_ERROR.play()

            elif boton_mute["rectangulo"].collidepoint(evento.pos):
                
                if datos_juego["volumen_musica"] > 0:
                    CLICK_SONIDO.play()
                    sonido_anterior = datos_juego["volumen_musica"]
                    datos_juego["volumen_musica"] = 0
                    boton_mute["superficie"].fill(COLOR_ROJO)
                elif datos_juego["volumen_musica"] == 0:
                    CLICK_SONIDO.play()
                    datos_juego["volumen_musica"] = sonido_anterior
                    boton_mute["superficie"].fill(COLOR_AZUL)
                    sonido_anterior = 0


            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
                
    #Aca pueden usar el get_pressed()
    


    pantalla.fill(COLOR_BLANCO)
    
    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(20,200))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(420,200))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    boton_mute["rectangulo"] = pantalla.blit(boton_mute["superficie"],(500,200))


    mostrar_texto(boton_volver["superficie"],"VOLVER",(10,10),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(boton_suma["superficie"],"VOL +",(5,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_resta["superficie"],"VOL -",(5,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_mute["superficie"],"M",(5,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(200,200),FUENTE_50,COLOR_NEGRO)
    
    return retorno
