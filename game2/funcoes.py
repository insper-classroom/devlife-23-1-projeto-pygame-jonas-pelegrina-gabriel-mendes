from pygame import *
from random import *
from textwrap import *

window = display.set_mode((1280, 720))

def classifica_nivel (perguntas):
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
    questao = choice(dicionario[nivel])
    return questao

def define_nivel (pontuacao):
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
    if nivel == 'Fácil':
        questao_sorteada = sorteia_questao (dicionario_classificado, 'Fácil')
    elif nivel == 'Médio':
        questao_sorteada = sorteia_questao (dicionario_classificado, 'Médio')
    elif nivel == 'Difícil':
        questao_sorteada = sorteia_questao (dicionario_classificado, 'Difícil')
    return questao_sorteada

def timer_nivel (nivel):
    if nivel == 'Fácil':
        timer = 30
    elif nivel == 'Médio':
        timer = 20
    elif nivel == 'Difícil':
        timer = 10
    return timer


def quebra_alternativa(txt, largura):
    lista = wrap(txt, largura,break_long_words=True)
    return '\n'.join(lista)


def desenha_linhas_pygame(txt, fonte, cor, x, y):
    for linha in txt.splitlines():
        window.blit(fonte.render(linha, 1, cor), (x, y))
        y += fonte.get_height()