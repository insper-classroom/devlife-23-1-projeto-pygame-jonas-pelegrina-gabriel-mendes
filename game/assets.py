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
retangulo_b = image.load('assets/img/retangulo_b.png')
retangulo_c = image.load('assets/img/retangulo_c.png')
retangulo_d = image.load('assets/img/retangulo_d.png')

retangulo_a = transform.scale(retangulo_a, (208, 120))
retangulo_b = transform.scale(retangulo_b, (208, 120))
retangulo_c = transform.scale(retangulo_c, (208, 120))
retangulo_d = transform.scale(retangulo_d, (208, 120))

perdeu = image.load('assets/img/perdeu.png')
perdeu = transform.scale(perdeu, (201, 215))

ganhou = image.load('assets/img/ganhou.png')
ganhou = transform.scale(ganhou, (201, 215))

# ----- Sons e efeitos sonoros
mixer.music.load('assets/sons/fundo.mp3')
success = mixer.Sound('assets/sons/success.mp3')
fail = mixer.Sound('assets/sons/fail.mp3')