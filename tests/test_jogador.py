from banco_imobiliario.jogador import Jogador, TipoJogar
from unittest import TestCase
from unittest.mock import MagicMock


class TestJogador(TestCase):
        
    def test_comprar_impulsivo_saldo_ok(self) -> None:
        """Testa a compras"""
        tipo_jogador = TipoJogar.impulsivo
        jogador = Jogador(tipo_jogador)
        self.assertTrue(jogador.comprar_impulsivo(FAKE_CIDADE(10, 100)))

    def test_comprar_impulsivo_saldo_insuficiente(self) -> None:
        """Testa a compras"""
        tipo_jogador = TipoJogar.impulsivo
        jogador = Jogador(tipo_jogador)
        self.assertFalse(jogador.comprar_impulsivo(FAKE_CIDADE(10, 301)))

    def test_comprar_cauteloso_saldo_ok(self) -> None:
        """Testa a compras"""
        tipo_jogador = TipoJogar.cauteloso
        jogador = Jogador(tipo_jogador)
        self.assertTrue(jogador.comprar_cauteloso(FAKE_CIDADE(10, 80)))

    def test_comprar_cauteloso_saldo_insuficiente(self) -> None:
        """Testa a compras"""
        tipo_jogador = TipoJogar.cauteloso
        jogador = Jogador(tipo_jogador)     
        self.assertFalse(jogador.comprar_cauteloso(FAKE_CIDADE(10, 81)))
        self.assertFalse(jogador.comprar_cauteloso(FAKE_CIDADE(10, 301)))

    def test_comprar_aleatorio_saldo_ok(self) -> None:
        """Testa a compras"""
        tipo_jogador = TipoJogar.aleatorio
        jogador = Jogador(tipo_jogador)
        jogador.comprar_aleatorio(FAKE_CIDADE(10, 200))   

    def test_comprar_aleatorio_saldo_insuficiente(self) -> None:
        """Testa a compras"""
        tipo_jogador = TipoJogar.aleatorio
        jogador = Jogador(tipo_jogador)
        self.assertFalse(jogador.comprar_aleatorio(FAKE_CIDADE(10, 301)) )
        
    def test_comprar_exigente_saldo_ok(self) -> None:
        """Testa a compras"""
        tipo_jogador = TipoJogar.exigente
        jogador = Jogador(tipo_jogador)
        self.assertTrue(jogador.comprar_exigente(FAKE_CIDADE(50, 10)))               
        self.assertFalse(jogador.comprar_exigente(FAKE_CIDADE(49, 10)))               

    def test_comprar_exigente_saldo_insuficiente(self) -> None:
        """Testa a compras"""
        tipo_jogador = TipoJogar.exigente
        jogador = Jogador(tipo_jogador)
        self.assertFalse(jogador.comprar_exigente(FAKE_CIDADE(301, 10)))
                
    def test_pular_impulsivo(self) -> None:
        """Testa a compraspular impulsivo"""
        tipo_jogador = TipoJogar.impulsivo
        jogador = Jogador(tipo_jogador)
        jogador.pular(7)

    def test_pular_cauteloso(self) -> None:
        """Testa a compraspular cauteloso"""
        tipo_jogador = TipoJogar.cauteloso
        jogador = Jogador(tipo_jogador)
        jogador.pular(7)        

    def test_pular_aleatorio(self) -> None:
        """Testa a compraspular aleatorio"""
        tipo_jogador = TipoJogar.aleatorio
        jogador = Jogador(tipo_jogador)
        jogador.pular(7)

    def test_pular_exigente(self) -> None:
        """Testa a pular exigente"""
        tipo_jogador = TipoJogar.exigente
        jogador = Jogador(tipo_jogador)
        jogador.pular(7)        
        

def FAKE_CIDADE(alugar,
                venda):
    cidade_mock = MagicMock()
    cidade_mock.propriedade_atual = {'propriedade': 1,
                            'alugar': alugar, 'venda': venda}
    return cidade_mock