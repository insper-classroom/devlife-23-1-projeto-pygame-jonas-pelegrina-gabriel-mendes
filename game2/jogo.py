# ===== Inicialização =====
# Importa pacotes
from pygame import *
from telas.tela_de_inicio import *
from telas.tela_de_instrucoes import *

from telas.tela_venceu_jogo import *
from telas.tela_fim_de_jogo import *
from config import *
from assets import *

# Classe que representa o jogo como um todo
class Jogo:
    def __init__(self):
        # Inicia módulos do Pygame
        init()

        # ----- Gera tela principal
        self.window = display.set_mode((WIDTH, HEIGHT))
        self.clock = time.Clock()
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
            else:
                tela_atual.desenha(self.window)
                self.clock.tick(FPS)




if __name__ == '__main__':
    Jogo().roda()