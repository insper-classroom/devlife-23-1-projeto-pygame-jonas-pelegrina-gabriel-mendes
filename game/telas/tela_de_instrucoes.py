# ===== Inicialização =====
# Importa pacotes
from pygame import *
from botoes import *
from config import *

# Classe da tela de instruções
class TelaDeInstrucoes:
    def __init__(self):
        # Carrega fonte
        self.fonte_jogo = font.Font ('assets/fonts/SpaceMono-Regular.ttf', 20)

        # Cria regras
        self.instrucoes = self.fonte_jogo.render('Instruções', True, LARANJA)
        self.instrucoes_detalhe = self.fonte_jogo.render('----------', True, PRETO)
        self.regras = self.fonte_jogo.render('Assim que o jogo for iniciado surgirá uma tela', True, PRETO)
        self.regras1 = self.fonte_jogo.render('com uma pergunta e quatro opções de resposta.', True, PRETO)
        self.regras2 = self.fonte_jogo.render('O jogador deverá escolher a resposta correta', True, PRETO)
        self.regras3 = self.fonte_jogo.render('antes do tempo acabar, caso contrário o jogador', True, PRETO)
        self.regras4 = self.fonte_jogo.render('perderá e o jogo será finalizado.', True, PRETO)
        self.regras5 = self.fonte_jogo.render('Caso o jogador responda corretamente, ele poderá', True, PRETO)
        self.regras6 = self.fonte_jogo.render('continuar com as perguntas e a pontuação do jogo', True, PRETO)
        self.regras7 = self.fonte_jogo.render('será aumentada.', True, PRETO)
        self.regras8 = self.fonte_jogo.render('Ao progredir no jogo, o nível das questões irá', True, PRETO)
        self.regras9 = self.fonte_jogo.render('aumentar, fazendo com que as perguntas fiquem', True, PRETO)
        self.regras10 = self.fonte_jogo.render('mais difíceis e o tempo de resposta diminua.', True, PRETO)
        self.regras11 = self.fonte_jogo.render('Para ganhar o jogo, o jogador precisa responder', True, PRETO)
        self.regras12 = self.fonte_jogo.render('todas as perguntas corretamente sem errar nenhuma.', True, PRETO)
        self.regras13 = self.fonte_jogo.render('Boa sorte!', True, PRETO)

        # Cria dimensão do botão
        largura = 120
        altura = 60
        x = WIDTH/2 - largura/2
        y = 550

        # Cria botão de voltar
        self.botao_voltar = Botao(x, y, largura, altura, ROXO)

        # Cria texto do botão
        self.voltar = self.fonte_jogo.render('Voltar', True, PRETO)


    def desenha(self, window):     
        """Desenha a tela de instruções"""    
        # Desenha fundo
        window.fill(BEGE_FUNDO)

        # Desenha regras
        window.blit(self.instrucoes, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 - 200))
        window.blit(self.instrucoes_detalhe, (WIDTH/2 - self.instrucoes_detalhe.get_width()/2 - 220, HEIGHT/2 - self.instrucoes_detalhe.get_height()/2 - 185))
        window.blit(self.regras, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 - 150))
        window.blit(self.regras1, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 - 130))
        window.blit(self.regras2, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 - 100))
        window.blit(self.regras3, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 - 80))
        window.blit(self.regras4, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 - 60))
        window.blit(self.regras5, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 - 30))
        window.blit(self.regras6, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 - 10))
        window.blit(self.regras7, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 + 10))
        window.blit(self.regras8, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 + 40))
        window.blit(self.regras9, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 + 60))
        window.blit(self.regras10, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 + 80))
        window.blit(self.regras11, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 + 110))
        window.blit(self.regras12, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 + 130))
        window.blit(self.regras13, (WIDTH/2 - self.instrucoes.get_width()/2 - 220, HEIGHT/2 - self.instrucoes.get_height()/2 + 160))

        # Desenha botão voltar
        self.botao_voltar.desenha(window, False)

        # Desenha texto dos botão
        window.blit(self.voltar, (WIDTH/2 - self.voltar.get_width()/2, HEIGHT/2 - self.voltar.get_height()/2 + 220))

        # Atualiza a tela
        display.update()

    def atualiza(self):
        """Atualiza a tela de instruções"""
        # Check eventos
        for evento in event.get():
            if evento.type == QUIT:
                return 'sair'
            if evento.type == MOUSEBUTTONUP:
                if evento.button == 1:
                    if self.botao_voltar.verifica_clique(evento.pos[0], evento.pos[1]):
                        return 'menu'
        return self