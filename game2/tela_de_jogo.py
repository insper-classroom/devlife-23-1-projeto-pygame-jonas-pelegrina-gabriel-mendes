# ===== Inicialização =====
# Importa pacotes
from pygame import *
from botoes import *
from funcoes import *

# Classe da tela de instruções
class TelaJogo:
    def __init__(self, perguntas):

        # Timer do jogo
        self.timer, self.texto = 30, '30'.rjust(3)
        time.set_timer(USEREVENT, 1000)

        # Carrega fonte
        self.fonte_jogo = font.Font ('assets/fonts/SpaceMono-Regular.ttf', 20)

        # Sons e efeitos sonoros
        self.success = mixer.Sound('assets/sons/success.mp3')
        self.fail = mixer.Sound('assets/sons/fail.mp3')
        self.win = mixer.Sound('assets/sons/win.mp3')
        
        # Carrega perguntas
        self.dicionario_classificado = classifica_nivel(perguntas)

        # Inicia a pontuação
        self.pontuacao = 0

        # Cria botões de resposta
        self.botoes_jogo = []
        self.botao_a = Botao(350, 300, 220, 100, (211, 135, 244))
        self.botao_b = Botao(600, 300 ,220, 100, (211, 135, 244))
        self.botao_c = Botao(350, 420, 220, 100, (211, 135, 244))
        self.botao_d = Botao(600, 420, 220, 100, (211, 135, 244))
        self.botoes_jogo.append(self.botao_a)
        self.botoes_jogo.append(self.botao_b)
        self.botoes_jogo.append(self.botao_c)
        self.botoes_jogo.append(self.botao_d)

        self.sorteia_pergunta()

    def desenha(self, window):

        # Desenha fundo na tela
        window.fill((230, 226, 216))

        # Desenha banner na tela
        draw.rect(window, (238, 138, 111), (1280/2 - 500, 720/10, 1000, 100))

        # Desenha título da questão na tela
        window.blit (self.titulo, (1280/2 - 450, 720/10 - self.titulo.get_height()/2 + 50))

        # Desenha botões na tela
        for botao in self.botoes_jogo:
            botao.desenha(window, False)

        # Desenha texto dos botões na tela
        for txt in range(len(self.textos)):
                linhas = quebra_alternativa(self.textos[txt], self.l)
                desenha_linhas_pygame(linhas, self.fonte_jogo, (0, 0, 0), self.posicao[txt][0], self.posicao[txt][1])

        # Desenha a pontuação na tela
        window.blit (self.pontuacao_do_jogador, (1280/2 - self.pontuacao_do_jogador.get_width()/2 + 400, 720/6 - self.pontuacao_do_jogador.get_height()))
        
        # Desenha o Texto/Dificuldade na tela
        window.blit (self.nivel_atual, (1280/2 - self.nivel_atual.get_width()/2 + 400, 720/5 - self.nivel_atual.get_height()/2))

        # Atualiza a tela
        display.update()

    
    def sorteia_pergunta(self):
        # Sorteia nova questão
        self.questao_sorteada = sorteia_questao(self.dicionario_classificado, 'Fácil')

        # Atualiza título da questão
        self.titulo = self.fonte_jogo.render(self.questao_sorteada['titulo'], True, (0, 0, 0))

        # Cria texto dos botões na tela
        self.l = 13
        self.opcoes = self.questao_sorteada['opcoes']
        self.textos = ['A: ' + self.opcoes['A'], 'B: ' + self.opcoes['B'], 'C: ' + self.opcoes['C'], 'D: ' + self.opcoes['D']]
        self.posicao = [(370, 320), (620, 320), (370, 440), (620, 440)]

        # Atualiza a pontuação
        self.pontuacao_do_jogador = self.fonte_jogo.render("Pontuação: " + str(self.pontuacao), True, (255, 255, 255))

        # Atualiza o Texto/Dificuldade na tela
        self.nivel_atual = self.fonte_jogo.render(self.questao_sorteada['nivel'], True, (255, 255, 255))

        # Atualiza a resposta correta
        self.resposta = self.questao_sorteada['correta']

        # Atualiza o nível da questão
        self.nivel = self.questao_sorteada['nivel']

        # Atualiza o índice da questão atual no banco de questão
        self.indice = (self.dicionario_classificado[self.nivel].index(self.questao_sorteada))


    def atualiza(self):
        # Checa eventos
        for evento in event.get():
            if evento.type == QUIT:
                return 'sair'
            elif evento.type == MOUSEBUTTONUP:
                if evento.button == 1:
                    for resposta, botao in [('A', self.botao_a), ('B', self.botao_b), ('C', self.botao_c), ('D', self.botao_d)]:
                        if botao.verifica_clique(evento.pos[0], evento.pos[1]):
                            if resposta == self.resposta:
                                botao.desenha(window, True)
                                self.pontuacao += 1
                                self.success.play()

                                # Retira questão do dicionário
                                del (self.dicionario_classificado[self.nivel][self.indice])

                                # Sorteia nova questão
                                self.sorteia_pergunta()

                            else:
                                self.fail.play()
                                return 'game_over'


                            
                            
        return self