# ===== Inicialização =====
#  Importa pacotes
from pygame import *
from config import *

def inicializa():
    #  Inicia módulos do Pygame
    init()
    mixer.init()


    # ----- Gera tela principal
    window = display.set_mode((WIDTH, HEIGHT))
    clock = time.Clock()
    display.set_caption('Jogo do Jonas')


    #  Símbolo do Pygame
    # programIcon = image.load('')
    # display.set_icon(programIcon)

    return window, clock

def atualiza_estado(clock):
# ----- Código principal

    for evento in event.get():
        # Verifica se o usuário quer fechar a janela
        if evento.type == QUIT:
            return False
        elif evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                return False
    clock.tick(FPS)
    


def desenha (window, clock):
    #  Preenche a janela d jogo
    window.fill (230, 226, 216)

    clock.tick(FPS)
    display.update()

def game_loop(window, clock):
    # Loop principal do jogo
    while atualiza_estado(clock):
        desenha(window, clock)

window, clock = inicializa()
game_loop(window, clock)


