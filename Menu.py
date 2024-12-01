import pygame
from Constantes import *
from Funciones import mostrar_texto
pygame.init()

lista_botones = []

for i in range(4):
    boton = {}

    boton["superficie"] = pygame.Surface(TAMAÑO_BOTON)
    boton["rectangulo"] = boton["superficie"].get_rect()
    #Ustedes no van a hacer el fill, ya que los botones deberian ser imagenes.
    imagen = pygame.image.load("imagenes/caja_texto.png")
    boton["imagen"] = pygame.transform.scale(imagen,TAMAÑO_BOTON)

    
    lista_botones.append(boton)


def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego) -> str:
    
    fondo = pygame.image.load("imagenes/Fondo_menu.png")
    fondo = pygame.transform.scale(fondo,VENTANA)
    

    #pygame.display.set_caption("MENU")
    retorno = "menu"
    
    #Gestion Eventos
    #Actualizacion del juego (Puede que este en los eventos)
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)):
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    if i == BOTON_JUGAR:
                        
                        retorno = "juego"
                    elif i == BOTON_CONFIG:
                        retorno = "configuraciones"
                    elif i == BOTON_RANKINGS:
                        retorno = "rankings"
                    elif i == BOTON_SALIR:
                        retorno = "salir"
                
    #Actualizacion del juego (Puede que este en los eventos)
    #Dibujar en pantalla
    
    
    pantalla.fill(COLOR_BLANCO)
    
    pantalla.blit(fondo,(0,0))
    
    
    lista_botones[BOTON_JUGAR]["rectangulo"] = pantalla.blit(lista_botones[BOTON_JUGAR]["imagen"],(0,115))
    
    lista_botones[BOTON_RANKINGS]["rectangulo"] = pantalla.blit(lista_botones[BOTON_RANKINGS]["imagen"],(0,195))

    lista_botones[BOTON_CONFIG]["rectangulo"] = pantalla.blit(lista_botones[BOTON_CONFIG]["imagen"],(0,275))
    
    lista_botones[BOTON_SALIR]["rectangulo"] = pantalla.blit(lista_botones[BOTON_SALIR]["imagen"],(0,355))
    
    mostrar_texto(lista_botones[BOTON_JUGAR]["imagen"],"JUGAR",(27,20),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_CONFIG]["imagen"],"CONFIGURAR",(27,20),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_RANKINGS]["imagen"],"RANKINGS",(27,20),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_SALIR]["imagen"],"SALIR",(27,20),FUENTE_30,COLOR_BLANCO)
    return retorno
    
    