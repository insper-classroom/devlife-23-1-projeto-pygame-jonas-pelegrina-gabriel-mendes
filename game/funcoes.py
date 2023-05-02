from pygame import *
from random import *
from perguntas_e_respostas import *
from textwrap import *
from config import *

window = display.set_mode((WIDTH, HEIGHT))

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
    if pontuacao < 10:
        nivel = 'Fácil'
    elif 10 <= pontuacao < 15:
        nivel = 'Médio'
    elif 15 <= pontuacao < 18:
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

def define_cor_nivel (nivel):
    if nivel == 'Fácil':
        cor_nivel = VERDE
    elif nivel == 'Médio':
        cor_nivel = AMARELO
    elif nivel == 'Difícil':
        cor_nivel = VERMELHO
    else:
        cor_nivel = PRETO
    return cor_nivel


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