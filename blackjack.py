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
        pontos = sum(carta.obter_valor_base() for carta in self.cartas)
        aces = sum(1 for carta in self.cartas if carta.valor == "A")
        
        while pontos > 21 and aces > 0:
            pontos -= 10
            aces -= 1
            
        return pontos

    def estourou(self):
        return self.calcular_pontos() > 21

    def eh_blackjack(self):
        return len(self.cartas) == 2 and self.calcular_pontos() == 21

class Jogador:
    def __init__(self, nome, fichas=100):
        self.nome = nome
        self.fichas = fichas
        self.mao = Mao()

    def fazer_aposta(self, valor):
        if valor > self.fichas:
            raise ValueError("Fichas insuficientes")
        self.fichas -= valor
        return valor