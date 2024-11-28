import pygame 
from Constantes import *
from Funciones import mostrar_texto, generar_json


pygame.init()

boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)

superficie_ranks = []
for i in range (10):
    superficie_rank= {}
    superficie_rank["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    superficie_rank["rectangulo"] = superficie_rank["superficie"].get_rect()
    
    superficie_ranks.append(superficie_rank)
    


def mostrar_puntuaciones(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]):
    retorno = "rankings"

    lista = generar_json("Partidas.json",None)

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
        
    
    pantalla.fill(COLOR_BLANCO)
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    mostrar_texto(boton_volver["superficie"],"VOLVER",(10,10),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(pantalla,f"ACA SE DEBE MOSTRAR EL TOP 10",(20,100),FUENTE_32,COLOR_NEGRO)
    
    
    for i in range(len(superficie_ranks)):
        superficie_ranks[i]["superficie"].fill(COLOR_AZUL)

    espacio_y = 150
    espacio_x = 20

    for i in range(len(superficie_ranks)):
        if espacio_y > 560:
            espacio_y = 150
            espacio_x = 320

            
        if i >= len(lista) :
            continue
            
        
        superficie_ranks[i]["rectangulo"] = pantalla.blit(superficie_ranks[i]["superficie"],(espacio_x,espacio_y))
        mostrar_texto(pantalla,f"top {i}: {lista[i]["usuario"]}",(espacio_x,espacio_y), FUENTE_22,COLOR_NEGRO )
            
        espacio_y += 100
        
    
  
    
    return retorno