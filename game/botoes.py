from pygame import *
from config import *

# Classe que representa um botão
class Botao:   
    def __init__(self, x, y, largura, altura, cor):
        """Cria um botão"""
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor

    def verifica_clique(self, x, y):
        """Verifica se o clique do mouse está dentro do botão"""
        if self.x <= x <= self.x + self.largura and self.y <= y <= self.y + self.altura:
            return True
        return False

    def desenha(self, window, pressed):
        """Desenha o botão na tela"""
        if pressed == False:
            draw.rect(window, self.cor, (self.x, self.y, self.largura, self.altura), border_radius = 15)
        else:
            draw.rect(window, LARANJA, (self.x, self.y, self.largura, self.altura), border_radius = 15)