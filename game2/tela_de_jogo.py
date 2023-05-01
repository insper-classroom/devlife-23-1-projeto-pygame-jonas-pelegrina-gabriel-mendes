# ===== Inicialização =====
# Importa pacotes
from pygame import *
from botoes import *

# Classe da tela de instruções
class TelaJogo:
    def __init__(self):

        # Carrega fonte
        fonte_jogo = font.Font ('game2/assets/fonts/SpaceMono-Regular.ttf', 20)


        # Cria título da questão
        self.titulo = fonte_jogo.render('Título da pergunta', True, PRETO)

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


    def desenha(self, window):
        # Desenha fundo
        window.fill((230, 226, 216))

        # Desenha banner
        draw.rect(window, (238, 138, 111), (1280/2 - 500, 720/10, 1000, 100))

        # Desenha título da questão
        window.blit (self.titulo, (WIDTH/2 - 450, HEIGHT/10 - self.titulo.get_height()/2 + 50))

        # Desenha botões
        for botao in self.botoes_jogo:
            botao.desenha(window, False)

        # Atualiza a tela
        display.update()

    def atualiza(self):
        # Checa eventos
        for evento in event.get():
            if evento.type == QUIT:
                return 'sair'
        return self