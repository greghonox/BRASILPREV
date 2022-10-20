from banco_imobiliario.jogador import TipoJogar
from unittest import TestCase


class TestTipoJogador(TestCase):
        
    def test_compra_impulsivo(self) -> None:
        """Como o impulsivo compra"""
        tipo_jogador = TipoJogar.impulsivo
        self.assertEqual(tipo_jogador.value['compra'], 100)
        self.assertTrue(tipo_jogador.comprar_impulsivo())

    def test_compra_cauteloso(self) -> None:
        """Como o cauteloso compra"""
        reserva = 80
        tipo_jogador = TipoJogar.cauteloso
        self.assertEqual(tipo_jogador.value['compra'], 80)
        self.assertTrue(tipo_jogador.comprar_cauteloso(reserva, 300))

    def test_compra_aleatorio(self) -> None:
        """Como o aleatorio compra"""
        tipo_jogador = TipoJogar.aleatorio
        self.assertEqual(tipo_jogador.value['compra'], 0)
        
    def test_compra_exigente(self) -> None:
        """Como o exigente compra"""
        valor_aluguel = 50
        tipo_jogador = TipoJogar.exigente
        self.assertEqual(tipo_jogador.value['compra'], 50)
        self.assertTrue(tipo_jogador.comprar_exigente(valor_aluguel))
        self.assertFalse(tipo_jogador.comprar_exigente(valor_aluguel - 1))
