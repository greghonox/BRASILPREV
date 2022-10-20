from banco_imobiliario.__init__ import *

class TipoJogar(Enum):
    impulsivo: Dict = {'tipo': 'impulsivo', 'compra': 100}
    cauteloso: Dict =  {'tipo': 'cauteloso', 'compra': 80}
    aleatorio: Dict = {'tipo': 'aleatorio', 'compra': 0}
    exigente: Dict = {'tipo': 'exigente', 'compra': 50}
    
    def comprar_impulsivo(self) -> bool:
        """Implementa o tipo de compra"""
        print(f'tipo compra cauteloso: True')
        return True

    def comprar_cauteloso(self, reserva: int) -> bool:
        """Implementa o tipo de compra"""
        resposta = reserva >= self.cauteloso.value['compra']        
        print(f'tipo compra cauteloso: {resposta}')
        return resposta

    def comprar_aleatorio(self) -> bool:
        """Implementa o tipo de compra"""
        resposta = choice([True, False])
        print(f'tipo compra aleatorio: {resposta}')
        return resposta

    def comprar_exigente(self, valor_aluguel: int) -> bool:
        """Implementa o tipo de compra"""
        resposta = valor_aluguel >= self.exigente.value['compra']
        print(f'tipo compra exigente: {resposta}')
        return resposta

            
class Jogador:
    def __init__(self, tipo_jogador: TipoJogar, nome_jogador: str=f'Jogador {randint(1, 100)}') -> None:
        """
            Aqui esta o jogador.
        """
        self.tipo_jogador: TipoJogar = tipo_jogador
        self.nome_jogador: str = nome_jogador
        self.saldo_atual: int = SALDO_INICIAL

    def pular(self, numero_dado: int) -> int:
        """
            Faz pulo de casa conforme numero sorteado pelo dado.
        """
        print(f'{self} pulando: {numero_dado} casas')
        return numero_dado
    
    def comprar(self, valor_compra: int=0) -> None:
        if self.saldo_atual >= valor_compra:
            self.saldo_atual = self.saldo_atual - valor_compra
            self.tipo_jogador
            return
        print(f'Nao possivel comprar {self}')
        
    def __str__(self) -> str:
        return 'Jogador: {} Tipo: {} Saldo: {}'.format(self.nome_jogador, 
                                        self.tipo_jogador.value['tipo'], self.saldo_atual)
        
    def __repr__(self) -> str:
        return super().__str__()