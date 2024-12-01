import pygame 
from Constantes import *
from Funciones import mostrar_texto, generar_json


pygame.init()

boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)
boton_volver["superficie"].set_colorkey(COLOR_AZUL)
boton_volver["imagen"] = pygame.image.load("imagenes/caja_texto.png")
boton_volver["imagen"] = pygame.transform.scale(boton_volver["imagen"],TAMAÑO_BOTON_VOLVER)

superficie_ranks = []
for i in range (10):
    superficie_rank= {}
    superficie_rank["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    superficie_rank["rectangulo"] = superficie_rank["superficie"].get_rect()
    superficie_rank["superficie"].set_colorkey(COLOR_AZUL)
    rank = pygame.image.load("imagenes/barra estadisticas.png")
    rank = pygame.transform.scale(rank,TAMAÑO_RANKING)
    superficie_rank["imagen"] = rank
    superficie_ranks.append(superficie_rank)

tabla_puntaje = pygame.image.load("imagenes/puntaje.png")
tabla_puntaje.set_alpha(192)
tabla_puntaje = pygame.transform.scale(tabla_puntaje,(340,150))
    


def mostrar_puntuaciones(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]):
    retorno = "rankings"
    fondo_ranking = pygame.image.load("imagenes/fondo ranking.jpg")
    fondo_ranking = pygame.transform.scale(fondo_ranking,VENTANA)
    rank_1 = pygame.image.load("imagenes/primero.png")
    rank_1 = pygame.transform.scale(rank_1,TAMAÑO_RANKING)
    rank_2 = pygame.image.load("imagenes/segundo.png")
    rank_2 = pygame.transform.scale(rank_2,TAMAÑO_RANKING)
    rank_3 = pygame.image.load("imagenes/tercero.png")
    rank_3 = pygame.transform.scale(rank_3,TAMAÑO_RANKING)

    lista = generar_json("Partidas.json",None)

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
        
    
    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(fondo_ranking,(0,0))
    pantalla.blit(boton_volver["imagen"],(10,10))
    pantalla.blit(tabla_puntaje,(215,17))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    mostrar_texto(boton_volver["superficie"],"VOLVER",(12,11),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(pantalla,f"RANKING",(290,70),fuente_50,COLOR_BLANCO)
    
    
    for i in range(len(superficie_ranks)):
        superficie_ranks[i]["superficie"].fill(COLOR_AZUL)

    espacio_y = 150
    espacio_x = 20

    for i in range(len(superficie_ranks)):
        if espacio_y > 660:
            espacio_y = 150
            espacio_x = 400

            
        if i >= len(lista) :
            continue
        if i == 0:
            pantalla.blit(rank_1,(espacio_x,espacio_y))
        elif i == 1:
            pantalla.blit(rank_2,(espacio_x,espacio_y))
        elif i == 2:
            pantalla.blit(rank_3,(espacio_x,espacio_y))
        else:     
            pantalla.blit(superficie_ranks[i]["imagen"],(espacio_x,espacio_y))


        

        mostrar_texto(pantalla,f"RANGO {i+1}: {lista[i]["usuario"]}",(espacio_x+5,espacio_y+20), FUENTE_22,COLOR_BLANCO)
        mostrar_texto(pantalla,f"fecha: {lista[i]["fecha y hora"]}",(espacio_x+5,espacio_y+45), FUENTE_22,COLOR_BLANCO)
        mostrar_texto(pantalla,f"Puntuacion: {lista[i]["puntuacion"]}",(espacio_x+5,espacio_y+70),FUENTE_22,COLOR_BLANCO)
            
        espacio_y += 110
        
    
  
    
    return retorno