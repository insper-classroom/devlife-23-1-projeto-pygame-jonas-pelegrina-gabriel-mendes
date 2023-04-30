# ===== Inicialização =====
# Importa pacotes
from pygame import *
from telas.tela_de_inicio import TelaDeInicio
from config import *
from assets import *

# Classe que representa o jogo como um todo
class Jogo:
    def __init__(self):
        # Inicia módulos do Pygame
        init()

        # ----- Gera tela principal
        window = display.set_mode((WIDTH, HEIGHT))
        clock = time.Clock()
        display.set_caption('Quiz Hero')

        # Símbolo do Pygame
        display.set_icon(simbolo)


    def roda(self):
        # Inicia tela de início
        tela_atual = TelaDeInicio(WIDTH, HEIGHT)

        # Loop principal
        rodando = True
        while rodando:
            tela_atual = tela_atual.atualiza()
            if tela_atual == 'sair':
                rodando = False
                quit()




if __name__ == '__main__':
    Jogo().roda()