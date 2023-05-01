# ===== Inicialização =====
# Importa pacotes
from pygame import *
from botoes import *

# Classe da tela de instruções
class TelaDeInstrucoes:
    def __init__(self):

        # Carrega fonte
        fonte_jogo = font.Font ('game2/assets/fonts/SpaceMono-Regular.ttf', 20)

        # Cria regras
        self.instrucoes = fonte_jogo.render('Instruções', True, LARANJA)
        self.instrucoes_detalhe = fonte_jogo.render('----------', True, (0, 0, 0))
        self.regras = fonte_jogo.render('Assim que o jogo for iniciado surgirá uma tela', True, (0, 0, 0))
        self.regras1 = fonte_jogo.render('com uma pergunta e quatro opções de resposta.', True, (0, 0, 0))
        self.regras2 = fonte_jogo.render('O jogador deverá escolher a resposta correta', True, (0, 0, 0))
        self.regras3 = fonte_jogo.render('antes do tempo acabar, caso contrário o jogador', True, (0, 0, 0))
        self.regras4 = fonte_jogo.render('perderá e o jogo será finalizado.', True, (0, 0, 0))
        self.regras5 = fonte_jogo.render('Caso o jogador responda corretamente, ele poderá', True, (0, 0, 0))
        self.regras6 = fonte_jogo.render('continuar com as perguntas e a pontuação do jogo', True, (0, 0, 0))
        self.regras7 = fonte_jogo.render('será aumentada.', True, (0, 0, 0))
        self.regras8 = fonte_jogo.render('Ao progredir no jogo, o nível das questões irá', True, (0, 0, 0))
        self.regras9 = fonte_jogo.render('aumentar, fazendo com que as perguntas fiquem', True, (0, 0, 0))
        self.regras10 = fonte_jogo.render('mais difíceis e o tempo de resposta diminua.', True, (0, 0, 0))
        self.regras11 = fonte_jogo.render('Para ganhar o jogo, o jogador precisa responder', True, (0, 0, 0))
        self.regras12 = fonte_jogo.render('todas as perguntas corretamente sem errar nenhuma.', True, (0, 0, 0))
        self.regras13 = fonte_jogo.render('Boa sorte!', True, (0, 0, 0))

        # Cria dimensão do botão
        largura = 120
        altura = 60
        x = 1280/2 - largura/2
        y = 550

        # Cria botão de voltar
        self.botao_voltar = Botao(x, y, largura, altura, ROXO)

        # Cria texto do botão
        self.voltar = fonte_jogo.render('Voltar', True, (0, 0, 0))


    def desenha(self, window):
        # Desenha fundo
        window.fill((230, 226, 216))

        # Desenha regras
        window.blit(self.instrucoes, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 - 200))
        window.blit(self.instrucoes_detalhe, (1280/2 - self.instrucoes_detalhe.get_width()/2 - 220, 720/2 - self.instrucoes_detalhe.get_height()/2 - 185))
        window.blit(self.regras, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 - 150))
        window.blit(self.regras1, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 - 130))
        window.blit(self.regras2, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 - 100))
        window.blit(self.regras3, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 - 80))
        window.blit(self.regras4, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 - 60))
        window.blit(self.regras5, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 - 30))
        window.blit(self.regras6, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 - 10))
        window.blit(self.regras7, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 + 10))
        window.blit(self.regras8, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 + 40))
        window.blit(self.regras9, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 + 60))
        window.blit(self.regras10, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 + 80))
        window.blit(self.regras11, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 + 110))
        window.blit(self.regras12, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 + 130))
        window.blit(self.regras13, (1280/2 - self.instrucoes.get_width()/2 - 220, 720/2 - self.instrucoes.get_height()/2 + 160))

        # Desenha botão voltar
        self.botao_voltar.desenha(window, False)

        # Desenha texto dos botão
        window.blit(self.voltar, (1280/2 - self.voltar.get_width()/2, 720/2 - self.voltar.get_height()/2 + 220))

        # Atualiza a tela
        display.update()

    def atualiza(self):
        # Checa eventos
        for evento in event.get():
            if evento.type == QUIT:
                return 'sair'
            elif evento.type == MOUSEBUTTONUP:
                if evento.button == 1:
                    if self.botao_voltar.verifica_clique(evento.pos[0], evento.pos[1]):
                        return 'menu'
        return self