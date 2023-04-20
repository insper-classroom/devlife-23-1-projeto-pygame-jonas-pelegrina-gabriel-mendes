from perguntas_e_respostas import *
from funcoes import *


# Dados gerais do jogo.
WIDTH = 1280 # Largura da tela
HEIGHT = 720 # Altura da tela
FPS = 60 # Frames por segundo
#CORES
LARANJA = (238, 138, 111)
ROXO = (211,135,244)
PRETO = (0,0,0)
BRANCO = (255,255,255)
BEJE_FUNDO = (230,226,216)

# Variáveis
tela_de_inicio = True
tela_de_instrucoes = False
inicio_jogo = False
pontuacao = 0
dicionario_classificado = classifica_nivel(perguntas)
questao_sorteada_facil = sorteia_questao(dicionario_classificado, 'facil')
questao_sorteada_medio = sorteia_questao(dicionario_classificado, 'medio')

print (perguntas)