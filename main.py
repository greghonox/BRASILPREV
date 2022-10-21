from banco_imobiliario.cidade_imobiliaria import CidadeImobiliaria
from banco_imobiliario.banco_imobiliario import BancoImobiliario
from banco_imobiliario.jogador import Jogador, TipoJogar


def gerar_jogor() -> None:
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
    return banco    
if __name__ == '__main__':
    for _ in range(300):
        banco = gerar_jogor()
        banco.main()
        input('Pressione enter para acompanhar nova jogada!')
        del banco