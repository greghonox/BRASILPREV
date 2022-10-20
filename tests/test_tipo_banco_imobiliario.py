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

    def test_comprar_propriedade(self) -> None:
        """
            Verifica o estado do jogador para continuar jogando.
        """
        tipo_jogador = TipoJogar.aleatorio
        jogador = [Jogador(tipo_jogador, 'test 0')]        
        cidade = CidadeImobiliaria()
        
        banco = BancoImobiliario(jogador, cidade)
        banco.comprar_propriedade(cidade.propriedades[0], jogador)

    def test_verificar_propriedade_vendida(self) -> None:
        """
            Verifica o estado do jogador para continuar jogando.
        """
        tipo_jogador = TipoJogar.aleatorio
        jogadores = [Jogador(tipo_jogador, 'test 0')]        
        cidade = CidadeImobiliaria()
        
        banco = BancoImobiliario(jogadores, cidade)
        resposta = banco.verificar_propriedade_vendida(0)
        self.assertFalse(resposta)
                    
    def test_comprar_propriedade(self) -> None:
        """
            Compra propriedade.
        """
        jogador_impulsivo = TipoJogar.impulsivo
        jogador_cauteloso = TipoJogar.cauteloso
        jogador_aleatorio = TipoJogar.aleatorio
        jogador_exigente = TipoJogar.exigente
        cidade = CidadeImobiliaria()
        
        jogadores = []        
        for tipo_jogador in [jogador_impulsivo,
                        jogador_cauteloso,
                        jogador_aleatorio,
                        jogador_exigente]:
            jogadores.append(Jogador(tipo_jogador))
            
        banco = BancoImobiliario(jogadores, cidade)
        for jogador in [jogador_impulsivo,
                        jogador_cauteloso,
                        jogador_aleatorio,
                        jogador_exigente]:
            next(cidade)
            print('-' * 100)
            banco.comprar_propriedade(jogador)

    def test_comprar_propriedade_ate_zerar(self) -> None:
        """
            Compra propriedade.
        """
        jogador_cauteloso = TipoJogar.cauteloso
        cidade = CidadeImobiliaria()
        jogador = Jogador(jogador_cauteloso)
        banco = BancoImobiliario([jogador], cidade)
        TIMEOUT = 1000
        for _ in cidade:
            print('-' * 100)
            if jogador.saldo_atual <= 0 or TIMEOUT == 0:
                self.assertEqual(TIMEOUT, 0)
                break
            if banco.comprar_propriedade(jogador_cauteloso):
                print(_, '**************')
            TIMEOUT -= 1
            