from banco_imobiliario.__init__ import *

class CidadeImobiliaria():

    def __init__(self) -> None:
        """ Gera a cidade para o jogo."""
        self._index: int = 0
        valor_minimo_alugar: int = 5
        valor_maximo_alugar: int = 50
        valor_minimo_venda: int = 30
        valor_maximo_venda: int = 100
        
        self.propriedade_atual = {}                
        self.propriedades: list = [{
            'propriedade': p + 1,
            'alugar': randint(valor_minimo_alugar,
                      valor_maximo_alugar),
            'venda': randint(valor_minimo_venda,
                     valor_maximo_venda),
        } for p in range(PROPRIEDADES)]
        
    def __next__(self) -> list:
        if self._index < PROPRIEDADES:
            item = self.propriedades[self._index]
            self.propriedade_atual = item
            self._index += 1
            return item
        self._index = 0
        item = self.propriedades[self._index]
        self.propriedade_atual = item
        return self.propriedades[self._index]
        
    def __iter__(self) -> list:
        return self
        
    def __str__(self) -> str:
        propriedades = ''
        for propriedade in self.propriedades:
            propriedades += str(propriedade) + '\n'
        return f'PROPRIEDADES\n{propriedades}'
    