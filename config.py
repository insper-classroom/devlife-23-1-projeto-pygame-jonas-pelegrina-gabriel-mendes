from perguntas_e_respostas import *
from funcoes import *
# Dados gerais do jogo.
WIDTH = 640 # Largura da tela
HEIGHT = 480 # Altura da tela
FPS = 60 # Frames por segundo

# Variáveis
tela_de_inicio = True
inicio_jogo = False

questao_sorteada = sorteia_questao(perguntas,'medio')
