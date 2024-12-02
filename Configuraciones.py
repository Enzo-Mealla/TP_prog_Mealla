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

imagen_barra = {}

imagen_barra_0 = pygame.image.load("imagenes/0%.png")
imagen_barra[0] = pygame.transform.scale(imagen_barra_0,(460,60))
imagen_barra_1 = pygame.image.load("imagenes/20%.png")
imagen_barra[1] = pygame.transform.scale(imagen_barra_1,(460,60))
imagen_barra_2 = pygame.image.load("imagenes/40%.png")
imagen_barra[2] = pygame.transform.scale(imagen_barra_2,(460,60))
imagen_barra_3 = pygame.image.load("imagenes/60%.png")
imagen_barra[3] = pygame.transform.scale(imagen_barra_3,(460,60))
imagen_barra_4 = pygame.image.load("imagenes/80%.png")
imagen_barra[4] = pygame.transform.scale(imagen_barra_4,(460,60))
imagen_barra_5 = pygame.image.load("imagenes/100%.png")
imagen_barra[5] = pygame.transform.scale(imagen_barra_5,(460,60))
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
                    datos_juego["volumen_musica"] += 20
                else:
                    CLICK_ERROR.play()
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] > 0:
                    CLICK_SONIDO.play()
                    datos_juego["volumen_musica"] -= 20
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

            elif boton_resta["resta_puntuacion"].collidepoint(evento.pos):
                if datos_juego["P_inicial"] > 100:
                    datos_juego["P_inicial"] -= 100
                    CLICK_SONIDO.play()
            elif boton_suma["suma_puntuacion"].collidepoint(evento.pos):
                if datos_juego["P_inicial"] < 1000:
                    datos_juego["P_inicial"] += 100
                    CLICK_SONIDO.play()

            elif boton_resta["resta_puntuacion_fallo"].collidepoint(evento.pos):
                if datos_juego["P_fallo"] > 100:
                    datos_juego["P_fallo"] -= 100
                    CLICK_SONIDO.play()
            elif boton_suma["suma_puntuacion_fallo"].collidepoint(evento.pos):
                if datos_juego["P_fallo"] < 1000:
                    datos_juego["P_fallo"] += 100
                    CLICK_SONIDO.play()

            elif boton_resta["resta_vida"].collidepoint(evento.pos):
                if datos_juego["vidas"] > 1:
                    datos_juego["vidas"] -= 1
                    CLICK_SONIDO.play()

            elif boton_suma["suma_vida"].collidepoint(evento.pos):
                if datos_juego["vidas"] < 5:
                    datos_juego["vidas"] += 1
                    CLICK_SONIDO.play()   
                     
            elif boton_resta["resta_tiempo"].collidepoint(evento.pos):
                if datos_juego["tiempo"] > 5:
                    datos_juego["tiempo"] -= 5
                    CLICK_SONIDO.play()  
            elif boton_suma["suma_tiempo"].collidepoint(evento.pos):
                if datos_juego["tiempo"] < 25:
                    datos_juego["tiempo"] += 5
                    CLICK_SONIDO.play()  



            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
                
    #Aca pueden usar el get_pressed()
    


    pantalla.fill(COLOR_BLANCO)

    
    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(20,200))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(370,200))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    boton_mute["rectangulo"] = pantalla.blit(boton_mute["superficie"],(500,200))


    boton_resta["resta_puntuacion"] = pantalla.blit(boton_resta["superficie"],(20,300))
    boton_suma["suma_puntuacion"] = pantalla.blit(boton_suma["superficie"],(420,300))

    boton_resta["resta_puntuacion_fallo"] = pantalla.blit(boton_resta["superficie"],(20,400))
    boton_suma["suma_puntuacion_fallo"] = pantalla.blit(boton_suma["superficie"],(420,400))

    boton_resta["resta_vida"] = pantalla.blit(boton_resta["superficie"],(20,500))
    boton_suma["suma_vida"] = pantalla.blit(boton_suma["superficie"],(420,500))

    boton_resta["resta_tiempo"] = pantalla.blit(boton_resta["superficie"],(20,600))
    boton_suma["suma_tiempo"] = pantalla.blit(boton_suma["superficie"],(420,600))


    mostrar_texto(boton_volver["superficie"],"VOLVER",(10,10),FUENTE_22,COLOR_BLANCO)

    mostrar_texto(boton_suma["superficie"],"VOL +",(5,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_resta["superficie"],"VOL -",(5,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_mute["superficie"],"M",(5,10),FUENTE_22,COLOR_NEGRO)



    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(200,200),FUENTE_50,COLOR_NEGRO)
    mostrar_texto(pantalla,f"P.A: {datos_juego["P_inicial"]} ",(200,300),FUENTE_50,COLOR_NEGRO)
    mostrar_texto(pantalla,f"P.F: {datos_juego["P_fallo"]} ",(200,400),FUENTE_50,COLOR_NEGRO)
    mostrar_texto(pantalla,f"vidas: {datos_juego["vidas"]} ",(200,500),FUENTE_50,COLOR_NEGRO)
    mostrar_texto(pantalla,f"Tiempo: {datos_juego["tiempo"]} ",(200,600),FUENTE_50,COLOR_NEGRO)

    for i in range(6):
        seleccion = 20 * i
        if datos_juego["volumen_musica"] == seleccion:
            pantalla.blit(imagen_barra[i],(20,200))



    return retorno
