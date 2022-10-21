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
    
    def comprar_propriedade(self, jogador: Jogador) -> bool:
        """
            Conforme condições comprar propriedade.
        """
        operador = self.jogadores[jogador[0]]['jogador']
        propriedade = self.cidade
        if not self.verificar_propriedade_vendida():
            if jogador[0] == 'aleatorio':
                if operador.comprar_aleatorio(propriedade):
                    return True
                return False
            if jogador[0] == 'cauteloso':                
                if operador.comprar_cauteloso(propriedade, 
                                    operador.saldo_atual):
                    return True
                return False
            if jogador[0] == 'exigente':                
                if operador.comprar_exigente(propriedade):
                    return True
                return False
            if jogador[0] == 'impulsivo':                
                if operador.comprar_impulsivo(propriedade):
                    return True            
            return False
        self.pagar_aluguel(jogador)
        print('=' * 100)
        return False

    def verificar_propriedade_vendida(self) -> bool:
        resposta = self.cidade.propriedade_atual['vendida']
        if resposta:
            print('propriedade ja vendida para {}!'.format(
                self.cidade.propriedade_atual['proprietario']))
        return resposta

    def pagar_aluguel(self, jogador: Jogador) -> bool:
        """
            Paga o alguel para o proprietario, caso não seja ele mesmo
        """
        cidade_atual = self.cidade.propriedade_atual
        if jogador[0] == cidade_atual['proprietario']:
            print(f'jogador {jogador[0]} e o proprietario e nao paga aluguel')
            return True
        
        if cidade_atual['alugar'] <= jogador[1]['jogador'].saldo_atual:
            jogador[1]['jogador'].saldo_atual -= cidade_atual['alugar']
            self.jogadores[cidade_atual['proprietario']]['jogador'].saldo_atual += cidade_atual['alugar']
            print(f"Pagando aluguel {jogador[0]} -> {cidade_atual['alugar']} -> {cidade_atual['proprietario']}")
            return True
        print(f'{jogador[0]} sem saldo para jogar!')
        return False
            
    def verificar_estado_jogo(self, jogador: Jogador) -> bool:
        """
            Verifica estado para o jogo continuar
        """
        self.rodadas -= 1
        self.cidade.propriedade_atual = self.cidade.propriedades[jogador[1]['posicao'] - 1]
        return self.rodadas == 0

    def verificar_jogador_rodando(self, jogador: Jogador) -> bool:
        """ 
            Verifica o estado do jogador.
        """
        joga = jogador[0]
        saldo_atual = self.jogadores[joga]['jogador'].saldo_atual
        resposta = saldo_atual > 0
        if not resposta:
            print(f'jogador {joga} nao tem mais saldo!')
            if saldo_atual < 0:
                self.limpar_propriedades(jogador)        
        return not resposta
            
    def jogar_dado(self, jogador: Jogador) -> None:
        """
            Joga o dado.
        """
        if (posicao := randint(1, DADO)) + jogador[1]['posicao'] <= PROPRIEDADES:
            jogador[1]['posicao'] += posicao
        else:
            jogador[1]['posicao'] = PROPRIEDADES - jogador[1]['posicao'] + posicao
            
        print(f'{jogador[0]}: Jogando dado... deu {posicao}, posicao atual {jogador[1]["posicao"]}')
                
    def finalizar_jogo(self) -> None:
        print('Propriedades vendidas:')
        jogadores = [jogador for jogador in self.jogadores]
        for jogador in jogadores:
            for propriedades in self.cidade.propriedades:
                if propriedades['vendida'] and propriedades['proprietario'] == jogador:
                    print(propriedades)
            print('-' * 10)
        print('=' * 100)
        
        for jogador in jogadores:
            print(f"Saldo restante: {jogador} {self.jogadores[jogador]['jogador'].saldo_atual}")
                    
    def limpar_propriedades(self, jogador) -> None:
        for propriedades in self.cidade.propriedades:
            if propriedades['proprietario'] == jogador[1]:
                propriedades['vendida'] = False
                propriedades['proprietario'] = None        
            
    def main(self) -> None:
        """
            Aonde o jogo acontece.
        """ 
        while True:     
            for jogador in self.jogadores.items():
                if self.verificar_jogador_rodando(jogador):
                    continue
                self.jogar_dado(jogador)
                if self.verificar_estado_jogo(jogador):
                    print('Jogo acabou!')
                    self.finalizar_jogo()
                    return
                self.comprar_propriedade(jogador)
                print('---' * 100)