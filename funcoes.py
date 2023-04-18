from random import *
from perguntas_e_respostas import *

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

def sorteia_questao(dicionario, nivel):
    questao = choice(dicionario[nivel])
    return (questao)