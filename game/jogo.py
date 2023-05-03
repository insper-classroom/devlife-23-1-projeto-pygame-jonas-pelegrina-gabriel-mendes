# ===== Inicialização =====
# Importa pacotes
from pygame import *
from tela_de_inicio import *
from tela_de_instrucoes import *
from tela_de_jogo import *
from tela_venceu_jogo import *
from tela_fim_de_jogo import *
from perguntas_e_respostas import *

# Classe que representa o jogo como um todo
class Jogo:
    def __init__(self):
        # Inicia módulos do Pygame
        init()

        # ----- Gera tela principal
        self.window = display.set_mode((1280, 720))
        self.clock = time.Clock()
        display.set_caption('Quiz Hero')

        # Símbolo do Pygame
        display.set_icon(simbolo)


    def roda(self):
        """Roda o jogo"""
        # Inicia tela de início
        tela_atual = TelaDeInicio()

        # Loop principal
        rodando = True
        while rodando:
            tela_atual = tela_atual.atualiza()

            # Verifica se o jogador quer sair
            if tela_atual == 'sair':
                rodando = False
                quit()

            # Verifica se o jogador quer ir para a tela de jogo
            elif tela_atual == 'jogar':
                tela_atual = TelaJogo(perguntas)

            # Verifica se o jogador quer voltar para a tela inicia;
            elif tela_atual == 'menu':
                tela_atual = TelaDeInicio()
            
            # Verifica se o jogador quer ir para a tela de instruções
            elif tela_atual == 'instrucoes':
                tela_atual = TelaDeInstrucoes()

            # Verifica se o jogador ganhou o jogo
            elif tela_atual == 'venceu':
                tela_atual = TelaVenceuJogo()
            
            # Verifica se o jogador perdeu o jogo
            elif tela_atual == 'game_over':
                tela_atual = TelaFimDeJogo()

            else:
                tela_atual.desenha(self.window)
                self.clock.tick(60)

                # Atualiza a tela
                display.update()




if __name__ == '__main__':
    Jogo().roda()