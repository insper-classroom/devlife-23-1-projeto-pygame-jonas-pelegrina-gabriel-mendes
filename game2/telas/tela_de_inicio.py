# ===== Inicialização =====
# Importa pacotes
from pygame import *
from config import *
from assets import *
from botoes import *

# Classe da tela de início
class TelaDeInicio:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura


    def desenha(self, window):
        # Desenha fundo
        window.fill(BEGE_FUNDO)

        # Desenha logo
        window.blit(logo, (WIDTH/2 - logo.get_width()/2, HEIGHT/2 - logo.get_height()/2 - 180))

        # Cria dimensões dos botões
        botoes = []
        largura = 120
        altura = 60
        x = WIDTH/2 - largura/2
        y = 350
        
        # Cria botões
        botao_jogar = Botao(x, y, largura, altura, ROXO)
        botao_instrucoes = Botao(x, y + 100, largura, altura, ROXO)
        botao_sair = Botao(x, y + 200, largura, altura, ROXO)
        botoes.append(botao_jogar)
        botoes.append(botao_instrucoes)
        botoes.append(botao_sair)

        # Desenha botões
        for botao in botoes:
            botao.desenha(window, False)
        
        # Desenha textos do botões
        jogar = fonte_jogo.render('Jogar', True, (0, 0, 0))
        window.blit(jogar, (WIDTH/2 - jogar.get_width()/2, HEIGHT/2 - jogar.get_height()/2 + 20))
        instrucoes = fonte_jogo.render('Instruções', True, (0, 0, 0))
        window.blit(instrucoes, (WIDTH/2 - instrucoes.get_width()/2, HEIGHT/2 - instrucoes.get_height()/2 + 120))
        sair = fonte_jogo.render('Sair', True, (0, 0, 0))
        window.blit(sair, (WIDTH/2 - sair.get_width()/2, HEIGHT/2 - sair.get_height()/2 + 220))

        # Atualiza a tela
        display.update()

    def atualiza(self):
        # Checa eventos
        for evento in event.get():
            if evento.type == QUIT:
                return 'sair'
        return self

