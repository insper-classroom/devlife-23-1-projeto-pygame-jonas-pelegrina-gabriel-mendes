from pygame import *
from config import *


class Botao:
    def __init__(self, x, y, largura, altura, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor

    def verifica_clique(self, x, y):
        """Verifica se o botão foi clicado"""
        if self.x <= x <= self.x + self.largura and self.y <= y <= self.y + self.altura:
            return True
        return False

    def desenha(self, window, pressed):
        """Desenha o botão"""
        if pressed == False:
            draw.rect(window, self.cor, (self.x, self.y, self.largura, self.altura), border_radius = 15)
        else:
            draw.rect(window, LARANJA, (self.x, self.y, self.largura, self.altura), border_radius = 15)