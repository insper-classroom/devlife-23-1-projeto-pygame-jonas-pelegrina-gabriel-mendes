# ===== Inicialização =====
# Importa pacotes
from pygame import *
from config import *
from assets import *
from botoes import *
from game2.funcoes import *

# Classe da tela de início
class TelaJogo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def desenha(self, window):
        # Desenha o fundo
        draw.rect(window, LARANJA, (WIDTH/2 - 500, HEIGHT/10, 1000, 100))


        # Desenha o título na tela
        titulo = fonte_jogo.render(questao_sorteada['titulo'], True, PRETO)
        window.blit (titulo, (WIDTH/2 - 450, HEIGHT/10 - titulo.get_height()/2 + 50))

        # Cria botões
        botoes_jogo = []
        botao_a = Botao(350, 300, 220, 100, ROXO)
        botao_b = Botao(600, 300 ,220, 100, ROXO)
        botao_c = Botao(350, 420, 220, 100, ROXO)
        botao_d = Botao(600, 420, 220, 100, ROXO)
        botoes_jogo.append(botao_a)
        botoes_jogo.append(botao_b)
        botoes_jogo.append(botao_c)
        botoes_jogo.append(botao_d)

        # Desenha os botões na tela
        for botao in botoes_jogo:
            botao.desenha(window, False)

        # Cria e desenha texto das opções na tela
        l = 13
        opcoes = questao_sorteada['opcoes']

        textos = ['A: ' + opcoes['A'], 'B: ' + opcoes['B'], 'C: ' + opcoes['C'], 'D: ' + opcoes['D']]
        posicao = [(370, 320), (620, 320), (370, 440), (620, 440)]
            
        for txt in range(len(textos)):
            linhas = quebra_alternativa(textos[txt], l)
            desenha_linhas_pygame(linhas, fonte_jogo, PRETO, posicao[txt][0], posicao[txt][1])
            
        # Desenha o Texto/Dificuldade na tela
        nivel_atual = fonte_jogo.render(questao_sorteada['nivel'], True, BRANCO)
        window.blit (nivel_atual, (WIDTH/2 - nivel_atual.get_width()/2 + 400, HEIGHT/5 - nivel_atual.get_height()/2))

        # Pontuação	do jogador
        pontuacao_jogador = fonte_jogo.render("Pontuação: " + str(pontuacao), True, BRANCO)
        window.blit (pontuacao_jogador, (WIDTH/2 - pontuacao_jogador.get_width()/2 + 400, HEIGHT/6 - pontuacao_jogador.get_height()))

        # Timer do jogo
        window.blit(fonte_jogo.render(texto, True, (0, 0, 0)), (32, 48))

        # Reposta correta
        resposta = questao_sorteada['correta']

        # Nível da questão
        nivel = questao_sorteada['nivel']

        # Índice da questão atual no banco de questão
        indice = (dicionario_classificado[nivel].index(questao_sorteada))

        # Atualiza a tela
        display.update()

    def atualiza(self):
        # Checa eventos
        for evento in event.get():
            if evento.type == QUIT:
                return 'sair'
        return self