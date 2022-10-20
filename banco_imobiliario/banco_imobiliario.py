from banco_imobiliario.__init__ import *
from banco_imobiliario.jogador import Jogador, TipoJogar
from banco_imobiliario.cidade_imobiliaria import CidadeImobiliaria


class BancoImobiliario:
    def __init__(self, jogadores: Jogador, cidade: CidadeImobiliaria) -> None:
        """
            Simulador de banco imobiliario.
            Aqui é jogo com suas regras.
        """
        self.rodadas: int = TIMEOUT
        self.jogadores: Dict = {}
        self.gerar_jogadores(jogadores)
        self.cidade: CidadeImobiliaria = cidade
        
    def gerar_jogadores(self, jogadores: list) -> None:
        """
            Gera os jogadores com seus estados.
        """
        print(f'GERANDO jogadores, quantidade: {len(jogadores)}')
        for jogador in jogadores:
            self.jogadores[jogador.tipo_jogador.name] = {
                    'jogador': jogador,
                    'vitorias': 0,
                    'posicao': 0,
            }
            
    def verifica_estado_jogador(self, jogador: Jogador) -> bool:
        """ 
            Verifica o estado do jogador.
        """
        saldo_atual = self.jogadores[jogador]['jogador'].saldo_atual
        return saldo_atual >= 0
    
    def comprar_propriedade(self, jogador: Jogador) -> bool:
        """
            Conforme condições comprar propriedade.
        """
        operador = self.jogadores[jogador.name]['jogador']
        propriedade = self.cidade
        if not self.verificar_propriedade_vendida():
            if jogador.value['tipo'] == 'aleatorio':
                if operador.comprar_aleatorio(propriedade):
                    return True
                return False
            if jogador.value['tipo'] == 'cauteloso':                
                if operador.comprar_cauteloso(propriedade, 
                                    operador.saldo_atual):
                    return True
                return False
            if jogador.value['tipo'] == 'exigente':                
                if operador.comprar_exigente(propriedade):
                    return True
                return False
            if jogador.value['tipo'] == 'impulsivo':                
                if operador.comprar_impulsivo(propriedade):
                    return True            
            return False
        return False
        
    def verificar_propriedade_vendida(self) -> bool:
        return self.cidade.propriedade_atual['vendida']

    def pagar_aluguel(self, propriedade: CidadeImobiliaria) -> bool:
        """
            Paga o alguel para o proprietario, caso não seja ele mesmo
        """
            
    def verifica_estado_jogo(self) -> bool:
        """
            Verifica estado para o jogo continuar
        """
        return self.rodadas == 0 
        
    def jogar_dado(self) -> int:
        """
            Joga o dado.
        """
        return randint(1, DADO)
                
    def main(self) -> None:
        """
            Aonde o jogo acontece.
        """ 
        