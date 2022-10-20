from banco_imobiliario.__init__ import *
from banco_imobiliario.cidade_imobiliaria import CidadeImobiliaria

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
    
    def comprar_impulsivo(self, cidade: CidadeImobiliaria) -> bool:
        valor_compra = cidade.propriedade_atual['venda']
        if self.saldo_atual >= valor_compra:
            if self.tipo_jogador.comprar_impulsivo():
                self.saldo_atual = self.saldo_atual - valor_compra
                print(f'Compra feita no valor {valor_compra} {self}')
                return True
        print(f'Saldo insuficiente {self}')
        return False

    def comprar_cauteloso(self, cidade: CidadeImobiliaria) -> bool:
        reserva = cidade.propriedade_atual['venda']
        if self.saldo_atual >= reserva:
            if self.tipo_jogador.comprar_cauteloso(reserva):
                self.saldo_atual = self.saldo_atual - reserva
                print(f'Compra feita no valor {reserva} {self}')
                return True
            print(f'{self} não quis comprar')
            return False
        print(f'Saldo insuficiente {self}')        
        return False

    def comprar_aleatorio(self, cidade: CidadeImobiliaria) -> bool:
        valor_compra = cidade.propriedade_atual['venda']
        if self.saldo_atual >= valor_compra:
            if self.tipo_jogador.comprar_aleatorio():
                self.saldo_atual = self.saldo_atual - valor_compra
                print(f'Compra feita no valor {valor_compra} {self}')
                return True
            print(f'{self} não quis comprar')
            return False
        print(f'Saldo insuficiente {self}')        
        return False

    def comprar_exigente(self, cidade: CidadeImobiliaria) -> bool:
        valor_aluguel = cidade.propriedade_atual['alugar']
        if self.saldo_atual >= valor_aluguel:
            if self.tipo_jogador.comprar_exigente(valor_aluguel):
                self.saldo_atual = self.saldo_atual - valor_aluguel
                print(f'Compra feita no valor {valor_aluguel} {self}')
                return True
            print(f'{self} não quis comprar')
            return False
        print(f'Saldo insuficiente {self}')        
            
    def __str__(self) -> str:
        return '{}: Tipo: {} Saldo: {}'.format(self.nome_jogador, 
                                        self.tipo_jogador.value['tipo'], self.saldo_atual)
        
    def __repr__(self) -> str:
        return super().__str__()