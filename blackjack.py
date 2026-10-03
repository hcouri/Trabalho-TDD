import random

class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

class Baralho:
    def __init__(self):
        naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        self.cartas = []
        for n in naipes:
            for v in valores:
                self.cartas.append(Carta(n, v))

    def embaralhar(self):
        random.shuffle(self.cartas)

    def comprar(self):
        return self.cartas.pop()