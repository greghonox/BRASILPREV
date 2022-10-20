from random import choice, randint
from typing import Dict
from enum import Enum

class TipoJogar(Enum):
    impulsivo: Dict = {'tipo': 'impulsivo', 'compra': 100}
    cauteloso: Dict =  {'tipo': 'cauteloso', 'compra': 80}
    aleatorio: Dict = {'tipo': 'aleatorio', 'compra': 0}
    exigente: Dict = {'tipo': 'exigente', 'compra': 50}
    
    def comprar_impulsivo(self) -> bool:
        """Implementa o tipo de compra"""
        return True

    def comprar_cauteloso(self, reserva: int) -> bool:
        """Implementa o tipo de compra"""
        return reserva >= self.cauteloso.value['compra']        

    def comprar_aleatorio(self) -> bool:
        """Implementa o tipo de compra"""
        return choice([True, False])

    def comprar_exigente(self, valor_aluguel: int) -> bool:
        """Implementa o tipo de compra"""
        return valor_aluguel >= self.exigente.value['compra']

            
class Jogador:
    def __init__(self, tipo_jogador: TipoJogar, nome_jogador: str=f'Jogador {randint(1, 100)}') -> None:
        """
            Aqui esta o jogador.
        """
        self.tipo_jogador = tipo_jogador
        self.nome_jogador = nome_jogador
    
    def comprar(self) -> None:
        """
            Realiaza a compra conforme o tipo.
        """
        
    @classmethod
    def pular(cls, numero_dado: int) -> None:
        """
            Faz pulo de casa conforme numero sorteado pelo dado.
        """
        
    def __str__(self) -> str:
        return 'Jogador: {} Tipo: {}'.format(self.nome_jogador, 
                                        self.tipo_jogador.value['tipo'])