# ===== Inicialização =====
# Importa pacotes
from pygame import *
from assets import *
from botoes import *

# Classe da tela de início
class TelaVenceuJogo:
    def __init__(self):

        # Carrega logo de vitória
        ganhou = image.load('game/assets/img/ganhou.png')
        self.ganhou = transform.scale(ganhou, (201, 215))

        # Carrega fonte
        self.fonte_jogo = font.Font ('game2/assets/fonts/SpaceMono-Regular.ttf', 20)

        # Cria mensagem de fim de jogo
        self.mensagem = fonte_jogo.render('Parabéns, você venceu o jogo!', True, (238, 138, 111))
        
        # Cria pontuação final
        self.pontuacao_final = fonte_jogo.render('Pontuação final: ' + str(0), True, (238, 138, 111))

        # Cria dimensões dos botões
        self.botoes = []
        largura = 200
        altura = 60
        x = 1280/2 - largura/2
        y = 400

        # Cria botões
        self.botao_jogar_novamente = Botao(x, y, largura, altura, (211, 135, 244))
        self.botao_menu_principal = Botao(x, y + 80, largura, altura, (211, 135, 244))
        self.botao_sair = Botao(1280/2 - 120/2, y + 160, 120, altura, (211, 135, 244))
        self.botoes.append(self.botao_jogar_novamente)
        self.botoes.append(self.botao_menu_principal)
        self.botoes.append(self.botao_sair)

        # Cria textos nos botões
        self.jogar_novamente = self.fonte_jogo.render('Jogar novamente', True, (0, 0, 0))
        self.menu_principal = self.fonte_jogo.render('Menu principal', True, (0, 0, 0))
        self.sair = self.fonte_jogo.render('Sair', True, (0, 0, 0))


    def desenha(self, window):

        # Desenha fundo na tela
        window.fill((230, 226, 216))

        # Desenha as mensagens na tela
        window.blit(self.mensagem, (1280/2 - self.mensagem.get_width()/2, 720/2 - self.mensagem.get_height()/2 - 40))
        window.blit(self.ganhou, (1280/2 - self.ganhou.get_width()/2, 720/2 - self.ganhou.get_height()/2 - 180))
        window.blit(self.pontuacao_final, (1280/2 - self.pontuacao_final.get_width()/2, 720/2 - self.pontuacao_final.get_height()/2 + 5))

        # Desenha botões
        for botao in self.botoes:
            botao.desenha(window, False)
            

        # Desenha textos do botões
        window.blit(self.jogar_novamente, (1280/2 - self.jogar_novamente.get_width()/2, 720/2 - self.jogar_novamente.get_height()/2 + 70))
        window.blit(self.menu_principal, (1280/2 - self.menu_principal.get_width()/2, 720/2 - self.menu_principal.get_height()/2 + 150))
        window.blit(self.sair, (1280/2 - self.sair.get_width()/2, 720/2 - self.sair.get_height()/2 + 230))

        # Atualiza a tela
        display.update()

    def atualiza(self):
        # Checa eventos
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