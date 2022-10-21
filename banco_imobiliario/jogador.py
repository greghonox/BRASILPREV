from banco_imobiliario.__init__ import *
from banco_imobiliario.cidade_imobiliaria import CidadeImobiliaria

class TipoJogar(Enum):
    impulsivo: Dict = {'tipo': 'impulsivo', 'compra': 100}
    cauteloso: Dict =  {'tipo': 'cauteloso', 'compra': 80}
    aleatorio: Dict = {'tipo': 'aleatorio', 'compra': 0}
    exigente: Dict = {'tipo': 'exigente', 'compra': 50}
    
    def comprar_impulsivo(self) -> bool:
        """Implementa o tipo de compra"""
        print(f'impulsivo tentando fazer compra, resposta: True')
        return True

    def comprar_cauteloso(self, reserva: int, saldo_atual: int) -> bool:
        """Implementa o tipo de compra"""
        resposta = (self.cauteloso.value['compra'] - reserva) <= saldo_atual
        print(f'cauteloso tentando fazer compra, resposta: {resposta}')
        return resposta

    def comprar_aleatorio(self) -> bool:
        """Implementa o tipo de compra"""
        resposta = choice([True, False])
        print(f'aleatorio tentando fazer compra, resposta: {resposta}')
        return resposta

    def comprar_exigente(self, valor_aluguel: int) -> bool:
        """Implementa o tipo de compra"""
        resposta = valor_aluguel >= self.exigente.value['compra']
        print(f'exigente tentando fazer compra, resposta: {resposta}')
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
                cidade.propriedade_atual['vendida'] = True
                cidade.propriedade_atual['proprietario'] = 'impulsivo'
                self.saldo_atual = self.saldo_atual - valor_compra
                print(f'Compra feita no valor {valor_compra} {self}')
                return True
        print(f'Saldo insuficiente {self}')
        return False

    def comprar_cauteloso(self, cidade: CidadeImobiliaria, saldo_atual: int) -> bool:
        reserva = cidade.propriedade_atual['venda']
        if self.saldo_atual >= reserva:
            if self.tipo_jogador.comprar_cauteloso(reserva, saldo_atual):
                cidade.propriedade_atual['vendida'] = True
                cidade.propriedade_atual['proprietario'] = 'cauteloso'
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
                cidade.propriedade_atual['vendida'] = True
                cidade.propriedade_atual['proprietario'] = 'aleatorio'
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
                cidade.propriedade_atual['vendida'] = True
                cidade.propriedade_atual['proprietario'] = 'exigente'
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