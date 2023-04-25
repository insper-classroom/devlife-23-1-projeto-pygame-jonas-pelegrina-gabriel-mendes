from pygame import *
from config import *


class Botao:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def verifica_clique(self, x, y):
        if self.x <= x <= self.x + self.largura and self.y <= y <= self.y + self.altura:
            return True
        return False

    def desenha(self, window):
        draw.rect(window, LARANJA, (self.x, self.y, self.largura, self.altura),border_radius = 15)