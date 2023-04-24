# ===== Inicialização =====
# Importa pacotes
from pygame import *
from config import *
from assets import *
from perguntas_e_respostas import *
from funcoes import *


# Inicia módulos do Pygame
init()
mixer.init()


# ----- Gera tela principal
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()
display.set_caption('Quiz Hero')


# Símbolo do Pygame
display.set_icon(simbolo)


# ----- Código principal
rodando = True
while rodando:
    window.fill (BEGE_FUNDO)


    if tela_de_inicio:
        window.blit(logo, (WIDTH/2 - logo.get_width()/2, HEIGHT/2 - logo.get_height()/2 - 80))
        start = fonte_jogo.render('Pressione qualquer tecla para começar', True, (0, 0, 0))
        instrucoes = fonte_jogo.render('Pressione [i] para ler as instruções do jogo', True, (0, 0, 0))
        window.blit(start, (WIDTH/2 - start.get_width()/2, HEIGHT/2 - start.get_height()/2 + 80))
        window.blit(instrucoes, (WIDTH/2 - instrucoes.get_width()/2, HEIGHT/2 - instrucoes.get_height()/2 + 120))


    else:




        if tela_de_instrucoes:
            instrucoes = fonte_jogo.render('Instruções', True, LARANJA)
            instrucoes_detalhe = fonte_jogo.render('----------', True, (0, 0, 0))
            regras = fonte_jogo.render('Assim que o jogo for iniciado surgirá uma tela', True, (0, 0, 0))
            regras1 = fonte_jogo.render('com uma pergunta e quatro opções de resposta.', True, (0, 0, 0))
            regras2 = fonte_jogo.render('O jogador deverá escolher a resposta correta', True, (0, 0, 0))
            regras3 = fonte_jogo.render('antes do tempo acabar, caso contrário o jogador', True, (0, 0, 0))
            regras4 = fonte_jogo.render('perderá e o jogo será finalizado.', True, (0, 0, 0))
            regras5 = fonte_jogo.render('Caso o jogador responda corretamente, ele poderá', True, (0, 0, 0))
            regras6 = fonte_jogo.render('continuar com as perguntas e a pontuação do jogo', True, (0, 0, 0))
            regras7 = fonte_jogo.render('será aumentada.', True, (0, 0, 0))
            regras8 = fonte_jogo.render('Ao progredir no jogo, o nível das questões irá', True, (0, 0, 0))
            regras9 = fonte_jogo.render('aumentar, fazendo com que as perguntas fiquem', True, (0, 0, 0))
            regras10 = fonte_jogo.render('mais difíceis e o tempo de resposta diminua.', True, (0, 0, 0))
            regras11 = fonte_jogo.render('Para ganhar o jogo, o jogador precisa responder', True, (0, 0, 0))
            regras12 = fonte_jogo.render('todas as perguntas corretamente sem errar nenhuma.', True, (0, 0, 0))
            inicio = fonte_jogo.render('Pressione [i] para voltar a tela inicial', True, LARANJA)

            window.blit(instrucoes, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 - 200))
            window.blit(instrucoes_detalhe, (WIDTH/2 - instrucoes_detalhe.get_width()/2 - 220, HEIGHT/2 - instrucoes_detalhe.get_height()/2 - 185))
            window.blit(regras, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 - 150))
            window.blit(regras1, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 - 130))
            window.blit(regras2, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 - 100))
            window.blit(regras3, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 - 80))
            window.blit(regras4, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 - 60))
            window.blit(regras5, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 - 30))
            window.blit(regras6, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 - 10))
            window.blit(regras7, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 + 10))
            window.blit(regras8, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 + 40))
            window.blit(regras9, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 + 60))
            window.blit(regras10, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 + 80))
            window.blit(regras11, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 + 110))
            window.blit(regras12, (WIDTH/2 - instrucoes.get_width()/2 - 220, HEIGHT/2 - instrucoes.get_height()/2 + 130))
            window.blit(inicio, (WIDTH/2 - inicio.get_width()/2, HEIGHT/2 - inicio.get_height()/2 + 180))






        elif inicio_jogo:
            # Pergunta do jogo
            titulo = fonte_jogo.render(questao_sorteada_facil['titulo'], True, LARANJA)
            opcoes = questao_sorteada_facil['opcoes']
            opcao_a = fonte_jogo.render(opcoes['A'], True, PRETO)
            opcao_b = fonte_jogo.render(opcoes['B'], True, PRETO)
            opcao_c = fonte_jogo.render(opcoes['C'], True, PRETO)
            opcao_d = fonte_jogo.render(opcoes['D'], True, PRETO)
            resposta = questao_sorteada_facil['correta']
            window.blit (titulo, (WIDTH/2 - titulo.get_width()/2 - 300, HEIGHT/10 - titulo.get_height()/2 + 50))
            window.blit (opcao_a, (WIDTH/2 - opcao_a.get_width()/2 - 300, HEIGHT/10 - opcao_a.get_height()/2 + 300))
            window.blit (opcao_b, (WIDTH/2 - opcao_b.get_width()/2 - 300, HEIGHT/10 - opcao_b.get_height()/2 + 400))
            window.blit (opcao_c, (WIDTH/2 - opcao_c.get_width()/2 + 300, HEIGHT/10 - opcao_c.get_height()/2 + 300))
            window.blit (opcao_d, (WIDTH/2 - opcao_d.get_width()/2 + 300, HEIGHT/10 - opcao_d.get_height()/2 + 400))
            
            
            # Criando retangulo
            window.blit(retangulo_a,(200, 200))
            window.blit(retangulo_b,(100, 100))
            window.blit(retangulo_c,(200, 200))
            window.blit(retangulo_d,(300, 300))


            # Texto/Dificuldade
            nivel = fonte_jogo.render(questao_sorteada_facil['nivel'], True, LARANJA)
            window.blit (nivel, (WIDTH/2 - nivel.get_width()/2 + 400, HEIGHT/10 - nivel.get_height()/2))
        





        elif tela_fim_de_jogo:
            window.blit(logo, (WIDTH/2 - logo.get_width()/2, HEIGHT/2 - logo.get_height()/2 - 80))
            mensagem = fonte_jogo.render('Você errou a pergunta...', True, (0, 0, 0))
            mensagem2 = fonte_jogo.render('Se quiser jogar novamente, pressione [r]', True, (0, 0, 0))
            mensagem3 = fonte_jogo.render('Se quiser voltar ao menu inicial, pressione [m]', True, (0, 0, 0))
            sair = fonte_jogo.render('Se quiser sair do jogo, pressione [ESC]', True, (0, 0, 0))
            window.blit(mensagem, (WIDTH/2 - mensagem.get_width()/2, HEIGHT/2 - mensagem.get_height()/2 + 80))
            window.blit(mensagem2, (WIDTH/2 - mensagem2.get_width()/2, HEIGHT/2 - mensagem2.get_height()/2 + 120))
            window.blit(mensagem3, (WIDTH/2 - mensagem3.get_width()/2, HEIGHT/2 - mensagem3.get_height()/2 + 160))
            window.blit(sair, (WIDTH/2 - sair.get_width()/2, HEIGHT/2 - sair.get_height()/2 + 200))









    # Verifica eventos e consequência
    for evento in event.get():
        # Verifica se o usuário quer fechar a janela
        if evento.type == QUIT or evento.type == KEYDOWN and evento.key == K_ESCAPE:
            rodando = False

        # Verifica se o usuário apertou alguma tecla
        elif evento.type == KEYDOWN:


            if tela_de_inicio:
                if evento.key == K_i:
                    tela_de_inicio = False
                    tela_de_instrucoes = True
                else:
                    tela_de_inicio = False
                    inicio_jogo = True
                    questao_sorteada_facil = sorteia_questao(dicionario_classificado, 'facil')


            elif tela_de_instrucoes:
                if evento.key == K_i:
                    tela_de_instrucoes = False
                    tela_de_inicio = True


            elif inicio_jogo:
                if evento.key == K_SPACE:
                    inicio_jogo = False
                    tela_fim_de_jogo = True


            elif tela_fim_de_jogo:
                if evento.key == K_r:
                    tela_fim_de_jogo = False
                    inicio_jogo = True
                    questao_sorteada_facil = sorteia_questao(dicionario_classificado, 'facil')
                elif evento.key == K_m:
                    tela_fim_de_jogo = False
                    tela_de_inicio = True
                
            
    clock.tick(FPS)
    display.update()


# ===== Finalização =====
quit()