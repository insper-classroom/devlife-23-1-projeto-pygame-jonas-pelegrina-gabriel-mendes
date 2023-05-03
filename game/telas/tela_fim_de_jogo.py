# ===== Inicialização =====
# Importa pacotes
from pygame import *
from botoes import *
from assets import *
from config import *

# Classe da tela de início
class TelaFimDeJogo:
    def __init__(self):
        # Carrega logo de derrota
        perdeu = image.load('assets/img/perdeu.png')
        self.perdeu = transform.scale(perdeu, (201, 215))

        # Carrega fonte
        self.fonte_jogo = font.Font ('assets/fonts/SpaceMono-Regular.ttf', 20)

        # Cria mensagem de fim de jogo
        self.mensagem = fonte_jogo.render('Você perdeu o jogo!', True, LARANJA)

        # Cria dimensões dos botões
        self.botoes = []
        largura = 200
        altura = 60
        x = WIDTH/2 - largura/2
        y = 400

        # Cria botões
        self.botao_jogar_novamente = Botao(x, y, largura, altura, LARANJA)
        self.botao_menu_principal = Botao(x, y + 80, largura, altura, LARANJA)
        self.botao_sair = Botao(WIDTH/2 - 120/2, y + 160, 120, altura, LARANJA)
        self.botoes.append(self.botao_jogar_novamente)
        self.botoes.append(self.botao_menu_principal)
        self.botoes.append(self.botao_sair)

        # Cria textos nos botões
        self.jogar_novamente = self.fonte_jogo.render('Jogar novamente', True, PRETO)
        self.menu_principal = self.fonte_jogo.render('Menu principal', True, PRETO)
        self.sair = self.fonte_jogo.render('Sair', True, PRETO)


    def desenha(self, window):
        """Desenha a tela de fim de jogo"""

        # Desenha fundo na tela
        window.fill(BEGE_FUNDO)

        # Desenha as mensagens na tela
        window.blit(self.mensagem, (WIDTH/2 - self.mensagem.get_width()/2, HEIGHT/2 - self.mensagem.get_height()/2 - 20))
        window.blit(self.perdeu, (WIDTH/2 - self.perdeu.get_width()/2, HEIGHT/2 - self.perdeu.get_height()/2 - 180))

        # Desenha botões
        for botao in self.botoes:
            botao.desenha(window, False)
            
        # Desenha textos do botões
        window.blit(self.jogar_novamente, (WIDTH/2 - self.jogar_novamente.get_width()/2, HEIGHT/2 - self.jogar_novamente.get_height()/2 + 70))
        window.blit(self.menu_principal, (WIDTH/2 - self.menu_principal.get_width()/2, HEIGHT/2 - self.menu_principal.get_height()/2 + 150))
        window.blit(self.sair, (WIDTH/2 - self.sair.get_width()/2, HEIGHT/2 - self.sair.get_height()/2 + 230))

        # Atualiza a tela
        display.update()

    def atualiza(self):
        """Atualiza a tela de fim de jogo"""
        # Check eventos
        for evento in event.get():
            if evento.type == QUIT:
                return 'sair'
            elif evento.type == MOUSEBUTTONUP:
                if evento.button == 1:
                    if self.botao_jogar_novamente.verifica_clique(evento.pos[0], evento.pos[1]):
                        return 'jogar'
                    elif self.botao_menu_principal.verifica_clique(evento.pos[0], evento.pos[1]):
                        return 'menu'
                    elif self.botao_sair.verifica_clique(evento.pos[0], evento.pos[1]):
                        return 'sair'
        return self