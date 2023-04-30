from pygame import *
from random import *

#  Inicia módulos do Pygame
init()
mixer.init()


# ----- Fontes
fonte_jogo = font.Font ('game/assets/fonts/SpaceMono-Regular.ttf', 20)

# ----- Imagens
simbolo = image.load('game/assets/icon/logo.png')
logo = transform.scale(simbolo, (201, 215))
retangulo_a = image.load('game/assets/img/retangulo_a.png')
retangulo_b = image.load('game/assets/img/retangulo_b.png')
retangulo_c = image.load('game/assets/img/retangulo_c.png')
retangulo_d = image.load('game/assets/img/retangulo_d.png')

retangulo_a = transform.scale(retangulo_a, (208, 120))
retangulo_b = transform.scale(retangulo_b, (208, 120))
retangulo_c = transform.scale(retangulo_c, (208, 120))
retangulo_d = transform.scale(retangulo_d, (208, 120))

perdeu = image.load('game/assets/img/perdeu.png')
perdeu = transform.scale(perdeu, (201, 215))

ganhou = image.load('game/assets/img/ganhou.png')
ganhou = transform.scale(ganhou, (201, 215))


# ----- Sons e efeitos sonoros
mixer.music.load('game/assets/sons/fundo.mp3')
success = mixer.Sound('game/assets/sons/success.mp3')
fail = mixer.Sound('game/assets/sons/fail.mp3')
win = mixer.Sound('game/assets/sons/win.mp3')