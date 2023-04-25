# ===== Inicialização =====
# Importa pacotes
from pygame import *
from classes_e_objetos import *
from config import *
from assets import *
from perguntas_e_respostas import *
from funcoes import *

# Inicia módulos do Pygame
init()
mixer.music.load('assets/sons/fundo.mp3')
success = mixer.Sound('assets/sons/success.mp3')
fail = mixer.Sound('assets/sons/fail.mp3')



# ----- Gera tela principal
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()
display.set_caption('Quiz Hero')
# Símbolo do Pygame
display.set_icon(simbolo)


# ----- Código principal
rodando = True
while rodando:
    window.fill(BEGE_FUNDO)

    # Tela de início
    if tela_de_inicio:
        window.blit(logo, (WIDTH/2 - logo.get_width()/2, HEIGHT/2 - logo.get_height()/2 - 180))
    
        # Cria dimensões dos botões
        botoes = []
        largura = 120
        altura = 60
        x = WIDTH/2 - largura/2
        y = 350
        

        # Cria botões
        botao_jogar = Botao(x, y, largura, altura)
        botao_instrucoes = Botao(x, y + 100, largura, altura)
        botao_sair = Botao(x, y + 200, largura, altura)
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

    else:

        # Tela de instruções
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
            
            # Cria dimensão do botão
            largura = 120
            altura = 60
            x = WIDTH/2 - largura/2
            y = 550

            # Cria e desenha botão
            botao_voltar = Botao(x, y, largura, altura)
            botao_voltar.desenha(window, False)


            # Desenha texto dos botão
            voltar = fonte_jogo.render('Voltar', True, (0, 0, 0))
            window.blit(voltar, (WIDTH/2 - voltar.get_width()/2, HEIGHT/2 - voltar.get_height()/2 + 220))




        elif inicio_jogo:
            # Pergunta do jogo
            draw.rect(window, LARANJA, (WIDTH/2 - 500, HEIGHT/10, 1000, 100))
            titulo = fonte_jogo.render(questao_sorteada_Fácil['titulo'], True, PRETO)


            # Opções de respostas
            opcoes = questao_sorteada_Fácil['opcoes']


            # Desenha as opções na tela
            opcao_a = fonte_jogo.render('A: ' + opcoes['A'], True, PRETO)
            opcao_b = fonte_jogo.render('B: ' + opcoes['B'], True, PRETO)
            opcao_c = fonte_jogo.render('C: ' + opcoes['C'], True, PRETO)
            opcao_d = fonte_jogo.render('D: ' + opcoes['D'], True, PRETO)


            # Reposta correta
            resposta = questao_sorteada_Fácil['correta']


            # Desenha o título na tela
            window.blit (titulo, (WIDTH/2 - 450, HEIGHT/10 - titulo.get_height()/2 + 50))


            # Cria botões
            botoes_jogo = []
            botao_a = Botao(350, 300, 220, 100)
            botao_b = Botao(600, 300 ,220, 100)
            botao_c = Botao(350, 420, 220, 100)
            botao_d = Botao(600, 420, 220, 100)
            botoes_jogo.append(botao_a)
            botoes_jogo.append(botao_b)
            botoes_jogo.append(botao_c)
            botoes_jogo.append(botao_d)

            # Desenha botões
            for botao in botoes_jogo:
                botao.desenha(window,False)
                
            # Desenha texto dos botões
            window.blit (opcao_a, (WIDTH/2 - opcao_a.get_width()/2 - 200, HEIGHT/10 - opcao_a.get_height()/2 + 280))
            window.blit (opcao_b, (WIDTH/2 - opcao_c.get_width()/4, HEIGHT/10 - opcao_c.get_height()/2 + 280))
            window.blit (opcao_c, (WIDTH/2 - opcao_b.get_width()/2 - 200, HEIGHT/10 - opcao_b.get_height()/2 + 400))
            window.blit (opcao_d, (WIDTH/2 - opcao_d.get_width()/2, HEIGHT/10 - opcao_d.get_height()/2 + 400))
            
            # Texto/Dificuldade
            nivel = fonte_jogo.render(questao_sorteada_Fácil['nivel'], True, BRANCO)
            window.blit (nivel, (WIDTH/2 - nivel.get_width()/2 + 400, HEIGHT/5 - nivel.get_height()/2))

            # Pontuação	do jogador
            nivel = fonte_jogo.render("Pontuação: " + str(pontuacao), True, BRANCO)
            window.blit (nivel, (WIDTH/2 - nivel.get_width()/2 + 400, HEIGHT/6 - nivel.get_height()))

            # Timer do jogo
            window.blit(fonte_jogo.render(texto, True, (0, 0, 0)), (32, 48))
        

        # Tela de fim de jogo
        elif tela_fim_de_jogo:
            window.blit(logo, (WIDTH/2 - logo.get_width()/2, HEIGHT/2 - logo.get_height()/2 - 180))
            mensagem = fonte_jogo.render('Você perdeu...', True, LARANJA)
            window.blit(mensagem, (WIDTH/2 - mensagem.get_width()/2, HEIGHT/2 - mensagem.get_height()/2 - 40))

            # Cria dimensões dos botões
            botoes = []
            largura = 200
            altura = 60
            x = WIDTH/2 - largura/2
            y = 370
            

            # Cria botões
            botao_jogar_novamente = Botao(x, y, largura, altura)
            botao_menu_principal = Botao(x, y + 80, largura, altura)
            botao_sair = Botao(WIDTH/2 - 120/2, y + 160, 120, altura)
            botoes.append(botao_jogar_novamente)
            botoes.append(botao_menu_principal)
            botoes.append(botao_sair)

            # Desenha botões
            for botao in botoes:
                botao.desenha(window, False)
            

            # Desenha textos do botões
            jogar_novamente = fonte_jogo.render('Jogar novamente', True, (0, 0, 0))
            window.blit(jogar_novamente, (WIDTH/2 - jogar_novamente.get_width()/2, HEIGHT/2 - jogar_novamente.get_height()/2 + 40))
            menu_principal = fonte_jogo.render('Menu principal', True, (0, 0, 0))
            window.blit(menu_principal, (WIDTH/2 - menu_principal.get_width()/2, HEIGHT/2 - menu_principal.get_height()/2 + 120))
            sair = fonte_jogo.render('Sair', True, (0, 0, 0))
            window.blit(sair, (WIDTH/2 - sair.get_width()/2, HEIGHT/2 - sair.get_height()/2 + 200))
                


            
            



        # Tela de vitória
        elif tela_venceu_jogo:
            window.blit(logo, (WIDTH/2 - logo.get_width()/2, HEIGHT/2 - logo.get_height()/2 - 80))
            mensagem = fonte_jogo.render('Você venceu!', True, (0, 0, 0))
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

        if tela_de_inicio:
            if evento.type == MOUSEBUTTONUP:
                if evento.button == 1:
                    if botao_jogar.verifica_clique(evento.pos[0], evento.pos[1]):
                        mixer.music.play()
                        tela_de_inicio = False
                        inicio_jogo = True
                        questao_sorteada_Fácil = sorteia_questao(dicionario_classificado, 'Fácil')
                        pontuacao = 0
                        # Timer do jogo
                        timer, texto = 5, '5'.rjust(3)
                        time.set_timer(USEREVENT, 1000)
                    elif botao_instrucoes.verifica_clique(evento.pos[0], evento.pos[1]):
                        tela_de_inicio = False
                        tela_de_instrucoes = True
                    elif botao_sair.verifica_clique(evento.pos[0], evento.pos[1]):
                        rodando = False
                        


        elif tela_de_instrucoes:
            if evento.type == MOUSEBUTTONUP:
                if evento.button == 1:
                    if botao_voltar.verifica_clique(evento.pos[0], evento.pos[1]):
                        tela_de_instrucoes = False
                        tela_de_inicio = True


        elif inicio_jogo:
            if evento.type == USEREVENT: 
                timer -= 1
                texto = str(timer).rjust(3) 
                if timer == 0:
                    inicio_jogo = False
                    tela_fim_de_jogo = True
                    mixer.music.pause()
                    fail.play()

            if evento.type == MOUSEBUTTONUP:
                if evento.button == 1:
                    if botao_a.verifica_clique(evento.pos[0], evento.pos[1]):
                        if resposta == "A":
                            botao_a.desenha(window,True)
                            pontuacao += 1
                            success.play()
                            questao_sorteada_Fácil = sorteia_questao(dicionario_classificado, 'Fácil')

                            # Timer do jogo
                            timer, texto = 5, '5'.rjust(3)
                            time.set_timer(USEREVENT, 1000)
                        else:
                            inicio_jogo = False
                            tela_fim_de_jogo = True
                            mixer.music.pause()
                            fail.play()

                    elif botao_b.verifica_clique(evento.pos[0], evento.pos[1]):
                        if resposta == "B":
                            botao_b.desenha(window,True)
                            pontuacao += 1
                            success.play()
                            inicio_jogo = True
                            questao_sorteada_Fácil = sorteia_questao(dicionario_classificado, 'Fácil')

                            # Timer do jogo
                            timer, texto = 5, '5'.rjust(3)
                            time.set_timer(USEREVENT, 1000)
                        else:
                            inicio_jogo = False
                            tela_fim_de_jogo = True
                            mixer.music.pause()
                            fail.play()

                    elif botao_c.verifica_clique(evento.pos[0], evento.pos[1]):
                        if resposta == "C":
                            botao_c.desenha(window,True)
                            pontuacao += 1
                            success.play()
                            inicio_jogo = True
                            questao_sorteada_Fácil = sorteia_questao(dicionario_classificado, 'Fácil')

                            # Timer do jogo
                            timer, texto = 5, '5'.rjust(3)
                            time.set_timer(USEREVENT, 1000)
                        else:
                            inicio_jogo = False
                            tela_fim_de_jogo = True
                            mixer.music.pause()
                            fail.play()

                    elif botao_d.verifica_clique(evento.pos[0], evento.pos[1]):
                        if resposta == "D":
                            botao_d.desenha(window,True)
                            pontuacao += 1
                            success.play()
                            inicio_jogo = True
                            questao_sorteada_Fácil = sorteia_questao(dicionario_classificado, 'Fácil')

                            # Timer do jogo
                            timer, texto = 5, '5'.rjust(3)
                            time.set_timer(USEREVENT, 1000)
                        else:
                            inicio_jogo = False
                            tela_fim_de_jogo = True
                            mixer.music.pause()
                            fail.play()


            elif evento.type == KEYDOWN and evento.key == K_a:
                inicio_jogo = False
                tela_venceu_jogo = True


        elif tela_fim_de_jogo:
            if evento.type == MOUSEBUTTONUP:
                if evento.button == 1:
                    if botao_jogar_novamente.verifica_clique(evento.pos[0], evento.pos[1]):
                        mixer.music.play()
                        tela_fim_de_jogo = False
                        inicio_jogo = True
                        questao_sorteada_Fácil = sorteia_questao(dicionario_classificado, 'Fácil')
                        pontuacao = 0
                
                        # Timer do jogo
                        timer, texto = 5, '5'.rjust(3)
                        time.set_timer(USEREVENT, 1000)
                    
                    elif botao_menu_principal.verifica_clique(evento.pos[0], evento.pos[1]):
                        tela_fim_de_jogo = False
                        tela_de_inicio = True


                    elif botao_sair.verifica_clique(evento.pos[0], evento.pos[1]):
                        rodando = False


        
        elif tela_venceu_jogo:
            if evento.type == KEYDOWN and evento.key == K_r:
                mixer.music.play()
                tela_venceu_jogo = False
                inicio_jogo = True
                questao_sorteada_Fácil = sorteia_questao(dicionario_classificado, 'Fácil')
                
                # Timer do jogo
                timer, texto = 5, '5'.rjust(3)
                time.set_timer(USEREVENT, 1000)


            elif evento.type == KEYDOWN and evento.key == K_m:
                tela_venceu_jogo = False
                tela_de_inicio = True

                
            
    clock.tick(FPS)
    display.update()


# ===== Finalização =====
quit()