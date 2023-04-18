from random import *
from perguntas_e_respostas import *

def sorteia_questao(perguntas,nivel):
    dicionario = {}
    for e in perguntas:
        for chaves, valores in e.items():
            if chaves == 'nivel':
                if valores in dicionario:
                    dicionario[valores].append (e)
                else:
                    dicionario[valores] = [e]
    questao = choice(dicionario[nivel])
    return questao