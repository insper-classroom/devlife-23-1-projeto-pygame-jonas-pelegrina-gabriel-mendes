# ===== Inicialização =====
# Importa pacotes
from pygame import *
from config import *
from assets import *
from botoes import *

# Classe da tela de início
class TelaFimDeJogo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura


    def desenha(self, window):
        # Desenha fundo
        window.fill(BEGE_FUNDO)

        # Cria e desenha as mensagens na tela
        mensagem = fonte_jogo.render('Você perdeu o jogo!', True, LARANJA)
        window.blit(mensagem, (WIDTH/2 - mensagem.get_width()/2, HEIGHT/2 - mensagem.get_height()/2 - 40))
        window.blit(perdeu, (WIDTH/2 - logo.get_width()/2, HEIGHT/2 - logo.get_height()/2 - 180))
        pontuacao_final = fonte_jogo.render('Pontuação final: ' + str(pontuacao), True, LARANJA)
        window.blit(pontuacao_final, (WIDTH/2 - pontuacao_final.get_width()/2, HEIGHT/2 - pontuacao_final.get_height()/2 + 5))


        # Cria dimensões dos botões
        botoes = []
        largura = 200
        altura = 60
        x = WIDTH/2 - largura/2
        y = 400
            

        # Cria botões
        botao_jogar_novamente = Botao(x, y, largura, altura, LARANJA)
        botao_menu_principal = Botao(x, y + 80, largura, altura, LARANJA)
        botao_sair = Botao(WIDTH/2 - 120/2, y + 160, 120, altura, LARANJA)
        botoes.append(botao_jogar_novamente)
        botoes.append(botao_menu_principal)
        botoes.append(botao_sair)


        # Desenha botões
        for botao in botoes:
            botao.desenha(window, False)
            

        # Desenha textos do botões
        jogar_novamente = fonte_jogo.render('Jogar novamente', True, (0, 0, 0))
        window.blit(jogar_novamente, (WIDTH/2 - jogar_novamente.get_width()/2, HEIGHT/2 - jogar_novamente.get_height()/2 + 70))
        menu_principal = fonte_jogo.render('Menu principal', True, (0, 0, 0))
        window.blit(menu_principal, (WIDTH/2 - menu_principal.get_width()/2, HEIGHT/2 - menu_principal.get_height()/2 + 150))
        sair = fonte_jogo.render('Sair', True, (0, 0, 0))
        window.blit(sair, (WIDTH/2 - sair.get_width()/2, HEIGHT/2 - sair.get_height()/2 + 230))

        # Atualiza a tela
        display.update()

    def atualiza(self):
        # Checa eventos
        for evento in event.get():
            if evento.type == QUIT:
                return 'sair'
        return self