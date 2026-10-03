import random

class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def obter_valor_base(self):
        if self.valor.isdigit():
            return int(self.valor)
        if self.valor in ["J", "Q", "K"]:
            return 10
        if self.valor == "A":
            return 11
        return 0

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
        return sum(carta.obter_valor_base() for carta in self.cartas)