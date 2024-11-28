import pygame
from Constantes import *
from Menu import *
from Juego import *
from Rankings import *
from Configuraciones import *
from Terminado import *


#Inicializar los elementos
pygame.init()
pygame.display.set_caption("MI PRIMER JUEGO 313")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True

datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"usuario":"","volumen_musica":100,"aciertos":0,"tiempo":10}
ventana_actual = "menu"
pygame.mixer.init() #Inicializo mixer para manipular la musica
bandera_musica = False
bandera_contador = False
#Bucle repetitivo
while corriendo:
    #Gestion Eventos -> No lo manejamos aca
    #Actualizacion del juego -> No lo manejamos aca
    #Dibujar en pantalla -> No lo manejamos aca
    cola_eventos = pygame.event.get()

    
    if ventana_actual == "menu":
        if bandera_musica == False:           
            pygame.mixer.music.load("sonidos/Menu.mp3") #Cargo musica de fondo            
            pygame.mixer.music.play(-1)
            bandera_musica = True
            
        ventana_actual = mostrar_menu(pantalla,cola_eventos,datos_juego)

        if ventana_actual == "juego":
            pygame.mixer.music.stop()
            bandera_musica = False
    elif ventana_actual == "juego":
        
        if bandera_musica == False:            
            pygame.mixer.music.load("sonidos/musica.mp3") #Cargo musica de fondo            
            pygame.mixer.music.play(-1)#Se ejecuta constatemente
            bandera_musica = True
           
        if bandera_contador == False:
            reloj = pygame.time.Clock()
            inicio_tiempo = pygame.time.get_ticks()
            tiempo_restante = datos_juego["tiempo"]
            reloj.tick(FPS)
            bandera_contador = True       
            
        ventana_actual,bandera_contador = mostrar_juego(pantalla,cola_eventos,datos_juego,inicio_tiempo,bandera_contador)
        
    elif ventana_actual == "configuraciones":

        porcentaje_coma = datos_juego["volumen_musica"] / 100  #0.5 = 50%
        pygame.mixer.music.set_volume(porcentaje_coma)
        ventana_actual = mostrar_configuracion(pantalla,cola_eventos,datos_juego)

    elif ventana_actual == "rankings":
        #Cargar los rankings
        ventana_actual = mostrar_puntuaciones(pantalla,cola_eventos)

    elif ventana_actual == "terminando":
        if bandera_musica == True:
            pygame.mixer.music.stop()
            bandera_musica = False
        ventana_actual = mostrar_juego_terminado(pantalla,cola_eventos,datos_juego)

    elif ventana_actual == "salir":
        corriendo = False
            
    pygame.display.flip()
    

pygame.quit()
        