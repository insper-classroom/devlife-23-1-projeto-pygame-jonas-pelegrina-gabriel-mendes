# ===== Inicialização =====
# Importa pacotes
from pygame import *
from botoes import *
from funcoes import *
from assets import *

# Classe da tela de instruções
class TelaJogo:
    def __init__(self, perguntas):
        # Carrega fonte
        self.fonte_jogo = font.Font ('assets/fonts/SpaceMono-Regular.ttf', 20)

        # Timer do jogo
        self.timer, self.texto = 30, '30'.rjust(3)
        time.set_timer(USEREVENT, 1000)

        # Sons e efeitos sonoros
        mixer.music.load('assets/sons/fundo.mp3')
        mixer.music.play(-1)
        self.success = success
        self.fail = fail
        self.win = win
        
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
        window.blit(self.titulo, (1280/2 - 450, 720/10 - self.titulo.get_height()/2 + 50))

        # Desenha botões na tela
        for botao in self.botoes_jogo:
            botao.desenha(window, False)

        # Desenha texto dos botões na tela
        for txt in range(len(self.textos)):
                linhas = quebra_alternativa(self.textos[txt], self.l)
                desenha_linhas_pygame(linhas, self.fonte_jogo, (0, 0, 0), self.posicao[txt][0], self.posicao[txt][1])

        # Desenha a pontuação na tela
        window.blit(self.pontuacao_do_jogador, (1280/2 - self.pontuacao_do_jogador.get_width()/2 + 400, 720/6 - self.pontuacao_do_jogador.get_height()))
        
        # Desenha o Texto/Dificuldade na tela
        window.blit(self.nivel_atual, (1280/2 - self.nivel_atual.get_width()/2 + 400, 720/5 - self.nivel_atual.get_height()/2))

        # Desenha o timer na tela
        window.blit(self.fonte_jogo.render(self.texto, True, (0, 0, 0)), (32, 48))

        # Atualiza a tela
        display.update()

    
    def sorteia_pergunta(self):
        # Nível de dificuldade atual
        self.nivel = define_nivel(self.pontuacao)

        # Sorteia nova questão
        self.questao_sorteada = questao_nivel(self.nivel, self.dicionario_classificado)

        # Atualiza título da questão
        self.titulo = self.fonte_jogo.render(self.questao_sorteada['titulo'], True, (0, 0, 0))

        # Cria texto dos botões na tela
        self.l = 13
        self.opcoes = self.questao_sorteada['opcoes']
        self.textos = ['A: ' + self.opcoes['A'], 'B: ' + self.opcoes['B'], 'C: ' + self.opcoes['C'], 'D: ' + self.opcoes['D']]
        self.posicao = [(370, 320), (620, 320), (370, 440), (620, 440)]

        # Atualiza a pontuação
        self.pontuacao_do_jogador = self.fonte_jogo.render("Pontuação: " + str(self.pontuacao), True, (255, 255, 255))

        # Cor do nível de dificuldade atual
        self.cor_nivel = define_cor_nivel(self.nivel)

        # Atualiza o Texto/Dificuldade na tela
        self.nivel_atual = self.fonte_jogo.render(self.nivel, True, (self.cor_nivel))

        # Atualiza a resposta correta
        self.resposta = self.questao_sorteada['correta']

        # Atualiza o índice da questão atual no banco de questão
        self.indice = (self.dicionario_classificado[self.nivel].index(self.questao_sorteada))

    def atualiza(self):
        # Checa eventos
        for evento in event.get():
            if evento.type == QUIT:
                return 'sair'
            
            elif evento.type == USEREVENT: 
                self.timer -= 1
                self.texto = str(self.timer).rjust(3) 
                if self.timer == 0:
                    mixer.music.pause()
                    self.fail.play()
                    return 'game_over'


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

                                # Define o nível de dificuldade
                                self.nivel = define_nivel(self.pontuacao)

                                # Verifica se o jogador ganhou
                                if self.nivel == 'Ganhou':
                                    mixer.music.pause()
                                    self.win.play()
                                    return 'venceu'

                                # Se não, sorteia nova questão
                                else:
                                    self.timer_texto = str(timer_nivel(self.nivel))
                                    self.timer, self.texto = timer_nivel(self.nivel), self.timer_texto.rjust(3)
                                    time.set_timer(USEREVENT, 1000)

                                    # Sorteia nova questão
                                    self.sorteia_pergunta()

                            # Se o jogador errar
                            else:
                                mixer.music.pause()
                                self.fail.play()
                                return 'game_over'  
        return self