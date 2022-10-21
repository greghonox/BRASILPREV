from banco_imobiliario.cidade_imobiliaria import CidadeImobiliaria
from banco_imobiliario.banco_imobiliario import BancoImobiliario
from banco_imobiliario.jogador import Jogador, TipoJogar
from unittest import TestCase
from unittest.mock import MagicMock


class TestBancoImobiliario(TestCase):

    def test_gerar_jogo(self) -> None:
        """
            Verifica o estado do jogador para continuar jogando.
        """
        jogador_impulsivo = TipoJogar.impulsivo
        jogador_cauteloso = TipoJogar.cauteloso
        jogador_aleatorio = TipoJogar.aleatorio
        jogador_exigente = TipoJogar.exigente
        
        jogadores = []        
        for jogador in [jogador_impulsivo,
                        jogador_cauteloso,
                        jogador_aleatorio,
                        jogador_exigente]:
            jogadores.append(Jogador(jogador, f'test {jogador}'))
            
        cidade = CidadeImobiliaria()
        
        banco = BancoImobiliario(jogadores, cidade)
        self.assertEqual(len(banco.jogadores), 4)

    def test_verificar_propriedade_vendida(self) -> None:
        """
            Verifica o estado do jogador para continuar jogando.
        """
        tipo_jogador = TipoJogar.aleatorio
        jogadores = [Jogador(tipo_jogador, 'test 0')]        
        cidade = CidadeImobiliaria()
        next(cidade)
        banco = BancoImobiliario(jogadores, cidade)
        resposta = banco.verificar_propriedade_vendida()
        self.assertFalse(resposta)
