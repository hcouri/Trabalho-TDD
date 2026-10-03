import random

class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

class Baralho:
    def __init__(self, preencher=True):
        self.cartas = []
        if preencher:
            naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
            valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
            self.cartas = [Carta(n, v) for n in naipes for v in valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def comprar(self):
        return self.cartas.pop()

class Mao:
    def __init__(self):
        self.cartas = []

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def calcular_pontos(self):
        pontos = 0
        for carta in self.cartas:
            if carta.valor.isdigit():
                pontos += int(carta.valor)
        return pontos