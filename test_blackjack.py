from blackjack import Carta, Baralho, Mao, Jogador

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

def test_calcular_pontos_com_as_valendo_11():
    mao = Mao()
    mao.adicionar_carta(Carta("Copas", "A"))
    mao.adicionar_carta(Carta("Ouros", "9"))
    assert mao.calcular_pontos() == 20

def test_calcular_pontos_com_as_valendo_1_se_estourar():
    mao = Mao()
    mao.adicionar_carta(Carta("Copas", "A"))
    mao.adicionar_carta(Carta("Ouros", "K"))
    mao.adicionar_carta(Carta("Paus", "Q"))
    assert mao.calcular_pontos() == 21

def test_mao_estourou_quando_pontos_maior_que_21():
    mao = Mao()
    mao.adicionar_carta(Carta("Copas", "10"))
    mao.adicionar_carta(Carta("Ouros", "K"))
    mao.adicionar_carta(Carta("Paus", "5"))
    assert mao.estourou() is True

def test_mao_eh_blackjack_com_duas_cartas_somando_21():
    mao = Mao()
    mao.adicionar_carta(Carta("Copas", "A"))
    mao.adicionar_carta(Carta("Ouros", "K"))
    assert mao.eh_blackjack() is True

def test_jogador_inicia_com_nome_mao_e_fichas():
    jogador = Jogador("Zeca", fichas=100)
    assert jogador.nome == "Zeca"
    assert jogador.fichas == 100
    assert isinstance(jogador.mao, Mao)
    assert len(jogador.mao.cartas) == 0

def test_jogador_pode_fazer_aposta_valida():
    jogador = Jogador("Bob", fichas=100)
    aposta = jogador.fazer_aposta(20)
    assert aposta == 20
    assert jogador.fichas == 80