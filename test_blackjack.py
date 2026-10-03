from blackjack import Carta, Baralho

def test_criar_carta_com_naipe_e_valor():
    carta = Carta("Copas", "A")
    assert carta.naipe == "Copas"
    assert carta.valor == "A"

def test_baralho_inicia_com_52_cartas():
    baralho = Baralho()
    assert len(baralho.cartas) == 52

def test_baralho_pode_ser_embaralhado():
    baralho1 = Baralho()
    baralho2 = Baralho()
    baralho2.embaralhar()
    assert baralho1.cartas != baralho2.cartas