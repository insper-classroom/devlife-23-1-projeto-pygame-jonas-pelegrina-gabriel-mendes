from pygame import *
from random import *

#  Inicia módulos do Pygame
init()
mixer.init()


# ----- Fontes
fonte_jogo = font.Font ('assets/fonts/SpaceMono-Regular.ttf', 20)

# ----- Imagens
simbolo = image.load('assets/icon/logo.png')
logo = transform.scale(simbolo, (201, 215))
retangulo_a = image.load('assets/img/retangulo_a.png')
retangulo_a = transform.scale(retangulo_a, (208, 120))