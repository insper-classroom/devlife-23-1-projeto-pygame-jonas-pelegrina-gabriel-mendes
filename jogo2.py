# ===== Inicialização =====
# Importa pacotes
from pygame import *
from config import *
from assets import *


# Inicia módulos do Pygame
init()
mixer.init()


# ----- Gera tela principal
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()
display.set_caption('Fast Game')


# Símbolo do Pygame
display.set_icon(simbolo)


# ----- Código principal
rodando = True
while rodando:
    window.fill ((230, 226, 216))

    if tela_de_inicio:
        window.blit(logo, (WIDTH/2 - logo.get_width()/2, HEIGHT/2 - logo.get_height()/2 - 80))
        fonte = fonte_jogo.render('Pressione qualquer tecla para começar', True, (0, 0, 0))
        window.blit(fonte, (WIDTH/2 - fonte.get_width()/2, HEIGHT/2 - fonte.get_height()/2 + 80))

    else:
        
        if inicio_jogo:
            fonte = fonte_jogo.render('Jogo iniciou', True, (0, 0, 0))
            window.blit (fonte, (WIDTH/2 - fonte.get_width()/2, HEIGHT/2 - fonte.get_height()/2))


    # Verifica eventos e consequência
    for evento in event.get():
        # Verifica se o usuário quer fechar a janela
        if evento.type == QUIT:
            rodando = False
        elif evento.type == KEYDOWN:
            if tela_de_inicio:
                inicio_jogo = True
                tela_de_inicio = False

    clock.tick(FPS)
    display.update()


# ===== Finalização =====
quit()