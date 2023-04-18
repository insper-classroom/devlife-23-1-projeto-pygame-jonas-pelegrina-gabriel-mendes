# ===== Inicialização =====
#  Importa pacotes
from pygame import *
from config import *


#  Inicia módulos do Pygame
init()
mixer.init()

# ----- Gera tela principal
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()
display.set_caption('Jogo do Jonas')


#  Símbolo do Pygame
programIcon = image.load('')
display.set_icon(programIcon)


# ----- Código principal
rodando = True
while rodando:
    for evento in event.get():
        # Verifica se o usuário quer fechar a janela
        if evento.type == QUIT:
            rodando = False
        elif evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                rodando = False

    clock.tick(FPS)
    display.update()


# ===== Finalização =====
quit()


