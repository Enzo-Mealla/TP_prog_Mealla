import pygame
from Constantes import *
from Funciones import *
from Rankings import boton_volver

pygame.init()

fondo_configuracion =pygame.image.load("imagenes/fondo configuracion.jpg")
fondo_configuracion = pygame.transform.scale(fondo_configuracion,VENTANA)

boton_suma = {}
boton_suma["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_suma["rectangulo"] = boton_suma["superficie"].get_rect()
boton_suma["superficie"].fill(COLOR_ROJO)
boton_suma["superficie"].set_colorkey(COLOR_ROJO)

boton_resta = {}
boton_resta["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_resta["rectangulo"] = boton_resta["superficie"].get_rect()
boton_resta["superficie"].fill(COLOR_ROJO)
boton_resta["superficie"].set_colorkey(COLOR_ROJO)

boton_mute = {}
boton_mute["superficie"] = pygame.Surface((60,60))
boton_mute["rectangulo"] = boton_mute["superficie"].get_rect()
boton_mute["superficie"].fill(COLOR_AZUL)
boton_mute["superficie"].set_colorkey(COLOR_AZUL)
boton_unmute = pygame.image.load("imagenes/unmute.png")
boton_mute["imagen_on"] = pygame.transform.scale(boton_unmute,(60,60))
boton_mute_off = pygame.image.load("imagenes/mute.png")
boton_mute["imagen_off"] = pygame.transform.scale(boton_mute_off,(60,60))

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
                    
                elif datos_juego["volumen_musica"] == 0:
                    CLICK_SONIDO.play()
                    datos_juego["volumen_musica"] = sonido_anterior
                    sonido_anterior = 0

            elif boton_resta["resta_puntuacion"].collidepoint(evento.pos):
                if datos_juego["P_inicial"] > 100:
                    datos_juego["P_inicial"] -= 100
                    CLICK_SONIDO.play()
            elif boton_suma["suma_puntuacion"].collidepoint(evento.pos):
                if datos_juego["P_inicial"] < 500:
                    datos_juego["P_inicial"] += 100
                    CLICK_SONIDO.play()

            elif boton_resta["resta_puntuacion_fallo"].collidepoint(evento.pos):
                if datos_juego["P_fallo"] > 100:
                    datos_juego["P_fallo"] -= 100
                    CLICK_SONIDO.play()
            elif boton_suma["suma_puntuacion_fallo"].collidepoint(evento.pos):
                if datos_juego["P_fallo"] < 500:
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
    pantalla.blit(fondo_configuracion,(0,0))
    
    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(20,200))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(370,200))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["imagen"],(10,10))
    boton_mute["rectangulo"] = pantalla.blit(boton_mute["superficie"],(625,200))


    boton_resta["resta_puntuacion"] = pantalla.blit(boton_resta["superficie"],(20,300))
    boton_suma["suma_puntuacion"] = pantalla.blit(boton_suma["superficie"],(370,300))

    boton_resta["resta_puntuacion_fallo"] = pantalla.blit(boton_resta["superficie"],(20,400))
    boton_suma["suma_puntuacion_fallo"] = pantalla.blit(boton_suma["superficie"],(370,400))

    boton_resta["resta_vida"] = pantalla.blit(boton_resta["superficie"],(20,500))
    boton_suma["suma_vida"] = pantalla.blit(boton_suma["superficie"],(370,500))

    boton_resta["resta_tiempo"] = pantalla.blit(boton_resta["superficie"],(20,600))
    boton_suma["suma_tiempo"] = pantalla.blit(boton_suma["superficie"],(370,600))


    mostrar_texto(boton_volver["imagen"],"VOLVER",(12,11),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]}",(228,180),FUENTE_40,COLOR_CELESTE)
    mostrar_texto(pantalla,f"{datos_juego["P_inicial"]}",(228,280),FUENTE_40,COLOR_CELESTE)
    mostrar_texto(pantalla,f"{datos_juego["P_fallo"]}",(228,380),FUENTE_40,COLOR_CELESTE)
    mostrar_texto(pantalla,f"{datos_juego["vidas"]}",(239,480),FUENTE_40,COLOR_CELESTE)
    mostrar_texto(pantalla,f"{datos_juego["tiempo"]}",(234,580),FUENTE_40,COLOR_CELESTE)

    
    texto_configuracion= ["volumen","Puntos por acierto", "Puntos por fallo","vidas","tiempo"]
    y_configuracion = 210
    for i in range(len(texto_configuracion)):
        mostrar_texto(pantalla,f"{texto_configuracion[i]}",(485,y_configuracion),FUENTE_40,COLOR_CELESTE)
        y_configuracion += 100


    if datos_juego["volumen_musica"] == 0:
        pantalla.blit(boton_mute["imagen_off"],(625,200))
    else:
        pantalla.blit(boton_mute["imagen_on"],(625,200))

    

    for i in range(6):
        seleccion_i= 20 * i
        seleccion_s = 100 * i
        seleccion_t = 5 * i
        if datos_juego["volumen_musica"] == seleccion_i:
            pantalla.blit(imagen_barra[i],(20,200))
        if datos_juego["P_inicial"] == seleccion_s: 
            pantalla.blit(imagen_barra[i],(20,300))
        if datos_juego["P_fallo"] == seleccion_s:
            pantalla.blit(imagen_barra[i],(20,400))
        if datos_juego["vidas"] == i:
            pantalla.blit(imagen_barra[i],(20,500))
        if datos_juego["tiempo"] == seleccion_t:
            pantalla.blit(imagen_barra[i],(20,600))


    return retorno
