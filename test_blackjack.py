from blackjack import Carta, Baralho

def test_criar_carta_com_naipe_e_valor():
    carta = Carta("Copas", "A")
    assert carta.naipe == "Copas"
    assert carta.valor == "A"