# ===== Inicialização =====
# Importa pacotes
from pygame import *
from assets import *
from botoes import *
from funcoes import *

# Classe da tela de início
class TelaJogo:
    def __init__(self, perguntas):


        self.dicionario_classificado = classifica_nivel(perguntas)
        self.questao_sorteada = sorteia_questao(self.dicionario_classificado, 'Fácil')


        # Cria título na tela
        self.titulo = fonte_jogo.render(self.questao_sorteada['titulo'], True, (0, 0, 0))

        # Cria botões
        self.botoes_jogo = []
        self.botao_a = Botao(350, 300, 220, 100, (211, 135, 244))
        self.botao_b = Botao(600, 300 ,220, 100, (211, 135, 244))
        self.botao_c = Botao(350, 420, 220, 100, (211, 135, 244))
        self.botao_d = Botao(600, 420, 220, 100, (211, 135, 244))
        self.botoes_jogo.append(self.botao_a)
        self.botoes_jogo.append(self.botao_b)
        self.botoes_jogo.append(self.botao_c)
        self.botoes_jogo.append(self.botao_d)
        
        # Cria texto das opções na tela
        self.l = 13
        self.opcoes = self.questao_sorteada['opcoes']

        self.textos = ['A: ' + self.opcoes['A'], 'B: ' + self.opcoes['B'], 'C: ' + self.opcoes['C'], 'D: ' + self.opcoes['D']]
        self.posicao = [(370, 320), (620, 320), (370, 440), (620, 440)]
        
        # Cria o Texto/Dificuldade na tela
        self.nivel_atual = fonte_jogo.render(self.questao_sorteada['nivel'], True, (255, 255, 255))

        # Cria Pontuação do jogador
        self.pontuacao_jogador = fonte_jogo.render("Pontuação: " + str(pontuacao), True, (255, 255, 255))


    def desenha(self, window):
        # Desenha o fundo
        draw.rect(window, (238, 138, 111), (1280/2 - 500, 720/10, 1000, 100))


        # Desenha o título na tela
        window.blit (self.titulo, (1280/2 - 450, 720/10 - self.titulo.get_height()/2 + 50))


        # Desenha os botões na tela
        for self.botao in self.botoes_jogo:
            self.botao.desenha(window, False)

        # Desenha textos das opções na tela
        for txt in range(len(self.textos)):
            self.linhas = quebra_alternativa(self.textos[txt], self.l)
            desenha_linhas_pygame(self.linhas, fonte_jogo, (0, 0, 0), self.posicao[txt][0], self.posicao[txt][1])
            
        # Desenha o Texto/Dificuldade na tela
        window.blit (self.nivel_atual, (1280/2 - self.nivel_atual.get_width()/2 + 400, 720/5 - self.nivel_atual.get_height()/2))

        # Desenha a Pontuação do jogador
        window.blit (self.pontuacao_jogador, (1280/2 - self.pontuacao_jogador.get_width()/2 + 400, 720/6 - self.pontuacao_jogador.get_height()))

        # Reposta correta
        self.resposta = self.questao_sorteada['correta']

        # Nível da questão
        self.nivel = self.questao_sorteada['nivel']

        # Índice da questão atual no banco de questão
        self.indice = (self.dicionario_classificado[self.nivel].index(self.questao_sorteada))

        # Atualiza a tela
        display.update()

    def atualiza(self):
        # Checa eventos
        for evento in event.get():
            if evento.type == QUIT:
                return 'sair'
        return self
    



