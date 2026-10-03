from blackjack import Carta, Baralho, Mao

def test_criar_carta_com_naipe_e_valor():
    carta = Carta("Copas", "A")
    assert carta.naipe == "Copas"
    assert carta.valor == "A"

def test_baralho_inicia_sem_cartas():
    baralho = Baralho(preencher=False)
    assert len(baralho.cartas) == 0

def test_baralho_inicia_com_52_cartas():
    baralho = Baralho()
    assert len(baralho.cartas) == 52

def test_baralho_pode_ser_embaralhado():
    baralho1 = Baralho()
    baralho2 = Baralho()
    baralho2.embaralhar()
    assert baralho1.cartas != baralho2.cartas

def test_baralho_pode_comprar_carta():
    baralho = Baralho()
    carta = baralho.comprar()
    assert isinstance(carta, Carta)
    assert len(baralho.cartas) == 51

def test_mao_inicia_sem_cartas():
    mao = Mao()
    assert len(mao.cartas) == 0

def test_mao_pode_adicionar_carta():
    mao = Mao()
    carta = Carta("Copas", "A")
    mao.adicionar_carta(carta)
    assert len(mao.cartas) == 1
    assert mao.cartas[0] == carta

def test_calcular_pontos_com_cartas_numericas():
    mao = Mao()
    mao.adicionar_carta(Carta("Copas", "2"))
    mao.adicionar_carta(Carta("Ouros", "5"))
    assert mao.calcular_pontos() == 7

def test_calcular_pontos_com_figuras():
    mao = Mao()
    mao.adicionar_carta(Carta("Copas", "J"))
    mao.adicionar_carta(Carta("Ouros", "Q"))
    mao.adicionar_carta(Carta("Paus", "K"))
    assert mao.calcular_pontos() == 30