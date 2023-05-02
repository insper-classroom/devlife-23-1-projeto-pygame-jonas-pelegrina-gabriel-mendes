from pygame import *
from random import *
from perguntas_e_respostas import *
from textwrap import *
from config import *

window = display.set_mode((WIDTH, HEIGHT))

def classifica_nivel (perguntas):
    """Classifica as perguntas por nível."""
    dicionario = {}
    for e in perguntas:
        for chaves, valores in e.items():
            if chaves == 'nivel':
                if valores in dicionario:
                    dicionario[valores].append (e)
                else:
                    dicionario[valores] = [e]
    return dicionario

def sorteia_questao (dicionario, nivel):
    """Sorteia uma questão de acordo com o nível."""
    questao = choice(dicionario[nivel])
    return questao

def define_nivel (pontuacao):
    """Define o nível de acordo com a pontuação."""
    if pontuacao < 5:
        nivel = 'Fácil'
    elif 5 <= pontuacao < 10:
        nivel = 'Médio'
    elif pontuacao == 10:
        nivel = 'Difícil'
    else:
        nivel = 'Ganhou'
    return nivel

def questao_nivel (nivel, dicionario_classificado):
    """Define a questão de acordo com o nível."""
    if nivel == 'Fácil':
        questao_sorteada = sorteia_questao (dicionario_classificado, 'Fácil')
    elif nivel == 'Médio':
        questao_sorteada = sorteia_questao (dicionario_classificado, 'Médio')
    elif nivel == 'Difícil':
        questao_sorteada = sorteia_questao (dicionario_classificado, 'Difícil')
    return questao_sorteada

def timer_nivel (nivel):
    """Define o timer de acordo com o nível."""
    if nivel == 'Fácil':
        timer = 30
    elif nivel == 'Médio':
        timer = 20
    elif nivel == 'Difícil':
        timer = 10
    return timer


def quebra_alternativa(txt, largura):
    """Quebra o texto da alternativa em linhas."""
    lista = wrap(txt, largura,break_long_words=True)
    return '\n'.join(lista)


def desenha_linhas_pygame(txt, fonte, cor, x, y):
    """Desenha o texto na tela."""
    for linha in txt.splitlines():
        window.blit(fonte.render(linha, 1, cor), (x, y))
        y += fonte.get_height()