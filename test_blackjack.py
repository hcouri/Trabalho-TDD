import pytest
from blackjack import Carta, Baralho, Mao, Jogador, Dealer, JogoBlackjack

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

def test_jogador_nao_pode_apostar_mais_do_que_possui():
    jogador = Jogador("Bob", fichas=50)
    with pytest.raises(ValueError, match="Fichas insuficientes"):
        jogador.fazer_aposta(100)

def test_jogador_pode_receber_ganhos():
    jogador = Jogador("Alice", fichas=100)
    jogador.receber_ganhos(50)
    assert jogador.fichas == 150

def test_dealer_inicia_com_nome_padrao_e_mao():
    dealer = Dealer()
    assert dealer.nome == "Dealer"
    assert isinstance(dealer.mao, Mao)
    assert len(dealer.mao.cartas) == 0

def test_dealer_deve_pedir_carta_se_pontos_menor_que_17():
    dealer = Dealer()
    dealer.mao.adicionar_carta(Carta("Copas", "10"))
    dealer.mao.adicionar_carta(Carta("Ouros", "6"))
    assert dealer.deve_pedir_carta() is True

    dealer.mao.adicionar_carta(Carta("Paus", "2"))
    assert dealer.deve_pedir_carta() is False

def test_jogo_distribui_duas_cartas_iniciais_para_jogador_e_dealer():
    jogador = Jogador("Alice", fichas=100)
    jogo = JogoBlackjack(jogador)
    jogo.distribuir_cartas_iniciais()

    assert len(jogo.jogador.mao.cartas) == 2
    assert len(jogo.dealer.mao.cartas) == 2
    assert len(jogo.baralho.cartas) == 48

def test_jogador_pode_pedir_carta():
    jogador = Jogador("Alice", fichas=100)
    jogo = JogoBlackjack(jogador)
    jogo.distribuir_cartas_iniciais()
    jogo.jogador_pedir_carta()

    assert len(jogo.jogador.mao.cartas) == 3
    assert len(jogo.baralho.cartas) == 47

def test_turno_dealer_compra_cartas_ate_atingir_pelo_menos_17():
    jogador = Jogador("Alice", fichas=100)
    jogo = JogoBlackjack(jogador)
    jogo.dealer.mao.adicionar_carta(Carta("Copas", "5"))
    jogo.dealer.mao.adicionar_carta(Carta("Ouros", "5"))  # Total = 10 (< 17)
    
    jogo.turno_dealer()
    
    assert jogo.dealer.mao.calcular_pontos() >= 17

def test_avaliar_vencedor_jogador_vence_quando_tem_mais_pontos():
    jogador = Jogador("Alice")
    jogo = JogoBlackjack(jogador)
    jogo.jogador.mao.adicionar_carta(Carta("Copas", "10"))
    jogo.jogador.mao.adicionar_carta(Carta("Ouros", "10"))  # 20
    jogo.dealer.mao.adicionar_carta(Carta("Paus", "10"))
    jogo.dealer.mao.adicionar_carta(Carta("Espadas", "8"))   # 18
    assert jogo.avaliar_vencedor() == "Jogador"

def test_avaliar_vencedor_dealer_vence_se_jogador_estourar():
    jogador = Jogador("Alice")
    jogo = JogoBlackjack(jogador)
    jogo.jogador.mao.adicionar_carta(Carta("Copas", "10"))
    jogo.jogador.mao.adicionar_carta(Carta("Ouros", "10"))
    jogo.jogador.mao.adicionar_carta(Carta("Paus", "5"))   # 25 (Estourou)
    assert jogo.avaliar_vencedor() == "Dealer"

def test_avaliar_vencedor_empate_pontos_iguais():
    jogador = Jogador("Alice")
    jogo = JogoBlackjack(jogador)
    jogo.jogador.mao.adicionar_carta(Carta("Copas", "10"))
    jogo.jogador.mao.adicionar_carta(Carta("Ouros", "9"))  # 19
    jogo.dealer.mao.adicionar_carta(Carta("Paus", "10"))
    jogo.dealer.mao.adicionar_carta(Carta("Espadas", "9"))  # 19
    assert jogo.avaliar_vencedor() == "Empate"

def test_pagar_aposta_vitoria_normal_paga_1_para_1():
    jogador = Jogador("Alice", fichas=100)
    jogo = JogoBlackjack(jogador)
    jogador.fazer_aposta(20)
    
    jogo.jogador.mao.adicionar_carta(Carta("Copas", "10"))
    jogo.jogador.mao.adicionar_carta(Carta("Ouros", "9"))
    jogo.dealer.mao.adicionar_carta(Carta("Paus", "10"))
    jogo.dealer.mao.adicionar_carta(Carta("Espadas", "8"))
    
    jogo.pagar_aposta(20)
    assert jogador.fichas == 120

def test_pagar_aposta_blackjack_natural_paga_3_para_2():
    jogador = Jogador("Alice", fichas=100)
    jogo = JogoBlackjack(jogador)
    jogador.fazer_aposta(20)
    
    jogo.jogador.mao.adicionar_carta(Carta("Copas", "A"))
    jogo.jogador.mao.adicionar_carta(Carta("Ouros", "K"))
    jogo.dealer.mao.adicionar_carta(Carta("Paus", "10"))
    jogo.dealer.mao.adicionar_carta(Carta("Espadas", "8"))
    
    jogo.pagar_aposta(20)
    assert jogador.fichas == 130

def test_pagar_aposta_empate_devolve_aposta():
    jogador = Jogador("Alice", fichas=100)
    jogo = JogoBlackjack(jogador)
    jogador.fazer_aposta(20)
    
    jogo.jogador.mao.adicionar_carta(Carta("Copas", "10"))
    jogo.jogador.mao.adicionar_carta(Carta("Ouros", "9"))
    jogo.dealer.mao.adicionar_carta(Carta("Paus", "10"))
    jogo.dealer.mao.adicionar_carta(Carta("Espadas", "9"))
    
    jogo.pagar_aposta(20)
    assert jogador.fichas == 100