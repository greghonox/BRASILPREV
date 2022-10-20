from banco_imobiliario.jogador import Jogador, TipoJogar
from unittest import TestCase


class TestJogador(TestCase):
        
    def test_comprar_impulsivo(self) -> None:
        """Testa a compras"""
        tipo_jogador = TipoJogar.impulsivo
        jogador = Jogador(tipo_jogador)
        self.assertTrue(jogador.tipo_jogador.comprar_impulsivo())

    def test_comprar_cauteloso(self) -> None:
        """Testa a compras"""
        reserva = 80
        tipo_jogador = TipoJogar.cauteloso
        jogador = Jogador(tipo_jogador)
        self.assertTrue(jogador.tipo_jogador.comprar_cauteloso(reserva))
        self.assertFalse(jogador.tipo_jogador.comprar_cauteloso(reserva - 1))

    def test_comprar_aleatorio(self) -> None:
        """Testa a compras"""
        tipo_jogador = TipoJogar.aleatorio
        jogador = Jogador(tipo_jogador)
        jogador.tipo_jogador.comprar_aleatorio()   

    def test_comprar_exigente(self) -> None:
        """Testa a compras"""
        valor_aluguel = 50
        tipo_jogador = TipoJogar.exigente
        jogador = Jogador(tipo_jogador)
        self.assertTrue(jogador.tipo_jogador.comprar_exigente(valor_aluguel))               
        self.assertFalse(jogador.tipo_jogador.comprar_exigente(valor_aluguel - 1))               
                    
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