# ===== Inicialização =====
# Importa pacotes
from pygame import *
from botoes import *


# Classe da tela de início
class TelaDeInicio:
    def __init__(self):
        # Carrega logo
        simbolo = image.load('assets/icon/logo.png')
        self.logo = transform.scale(simbolo, (201, 215))

        # Carrega fonte
        self.fonte_jogo = font.Font ('assets/fonts/SpaceMono-Regular.ttf', 20)
        
        # Cria dimensões dos botões
        self.botoes = []
        largura = 120
        altura = 60
        x = 1280/2 - largura/2
        y = 350
        
        # Cria botões
        self.botao_jogar = Botao(x, y, largura, altura, (211, 135, 244))
        self.botao_instrucoes = Botao(x, y + 100, largura, altura, (211, 135, 244))
        self.botao_sair = Botao(x, y + 200, largura, altura, (211, 135, 244))
        self.botoes.append(self.botao_jogar)
        self.botoes.append(self.botao_instrucoes)
        self.botoes.append(self.botao_sair)

        # Cria texto dos botões
        self.jogar = self.fonte_jogo.render('Jogar', True, (0, 0, 0))
        self.instrucoes = self.fonte_jogo.render('Instruções', True, (0, 0, 0))
        self.sair = self.fonte_jogo.render('Sair', True, (0, 0, 0))

    def desenha(self, window):
        # Desenha fundo
        window.fill((230,226,216))

        # Desenha logo
        window.blit(self.logo, (1280/2 - self.logo.get_width()/2, 720/2 - self.logo.get_height()/2 - 180))

        # Desenha botões
        for botao in self.botoes:
            botao.desenha(window, False)
        
        # Desenha textos do botões
        window.blit(self.jogar, (1280/2 - self.jogar.get_width()/2, 720/2 - self.jogar.get_height()/2 + 20))
        window.blit(self.instrucoes, (1280/2 - self.instrucoes.get_width()/2, 720/2 - self.instrucoes.get_height()/2 + 120))
        window.blit(self.sair, (1280/2 - self.sair.get_width()/2, 720/2 - self.sair.get_height()/2 + 220))

        # Atualiza a tela
        display.update()

    def atualiza(self):
        # Checa eventos
        for evento in event.get():
            if evento.type == QUIT:
                return 'sair'
            elif evento.type == MOUSEBUTTONUP:
                if evento.button == 1:
                    if self.botao_jogar.verifica_clique(evento.pos[0], evento.pos[1]):
                        return 'jogar'
                    elif self.botao_instrucoes.verifica_clique(evento.pos[0], evento.pos[1]):
                        return 'instrucoes'
                    elif self.botao_sair.verifica_clique(evento.pos[0], evento.pos[1]):
                        return 'sair'
        return self