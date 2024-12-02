import pygame


pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
COLOR_MARRON = (139, 69, 19)
ANCHO = 800
ALTO = 800
VENTANA = (ANCHO,ALTO)
FPS = 60

TAMAÑO_PREGUNTA = (700,350)
TAMAÑO_RESPUESTA = (250,60)
TAMAÑO_RANKING = (325,100)
TAMAÑO_BOTON = (250,60)
CUADRO_TEXTO = (250,50)
TAMAÑO_BOTON_VOLUMEN = (110,60)
TAMAÑO_BOTON_VOLVER = (100,40)


ruta_fuente = "imagenes/MonsterHunter.ttf"
fuente = pygame.font.Font(ruta_fuente,30)
fuente_50 = pygame.font.Font(ruta_fuente,50)
FUENTE_50 = pygame.font.SysFont("Helvetica",40)
FUENTE_40 = pygame.font.SysFont("Helvetica",30)
FUENTE_32 = pygame.font.SysFont("Helvetica",22)
FUENTE_30 = pygame.font.SysFont("Helvetica",20)
FUENTE_25 = pygame.font.SysFont("Helvetica",15)
FUENTE_22 = pygame.font.SysFont("Helvetica",12)

CLICK_ACIERTO = pygame.mixer.Sound("sonidos/correcto.mp3")
CLICK_SONIDO = pygame.mixer.Sound("sonidos/click.mp3")
CLICK_ERROR = pygame.mixer.Sound("sonidos/incorrecto.mp3")

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 500
PUNTUACION_ERROR = 300

BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_RANKINGS = 2
BOTON_SALIR = 3

#CONSTANTES BONUS
CORDS_BONUS = 650, 650
DIM_BONUS = (100, 100)

