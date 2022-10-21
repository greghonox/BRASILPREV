## ***Simulador do jogo banco imobiliario***
### Projeto desenvolvido para cumprir desafio.

## Para resolver o problema dessa simulação foi utilizado:
#### 1. Testes unitários.
#### 2. Arquitetura de projeto singleton.
#### 3. Logico github com suas branch's.
#### 4. Integração com ambiente unix.
#### 5. Makefile

## Tela dos testes e ambiente de desenvolviemento
![img](https://github.com/greghonox/BRASILPREV/blob/main/resources/tela.png)

## Historico de desenvolvimento
![img](https://github.com/greghonox/BRASILPREV/blob/main/resources/grafico.png)
## Projeto foi desenvolvido com base no desafio pdf
### [Desafio pdf esta aqui!](https://github.com/greghonox/BRASILPREV/blob/main/resources/%20Desafio%20T%C3%A9cnico%20-%20Python-%20SPRINT%20%2331%20(1).pdf)

## Saida do projeto 
[Link para txt](https://files.fm/u/5zvmzf477)

## Como rodar o projeto?!

```python
git clone git@github.com:greghonox/BRASILPREV.git
cd BRASILPREV
python main.py > saida.txt
```
### *O comando acima não é necessário usar* `> saida.txt`

## Deficies tecnicos
#### 1. Se deixar o jogador ficar negativo fica disparando na direção estranha e só um jogador ganha.
#### 2. Se continuar com a regra de negativo, muitas vezes o jogo fica em loop até timeout.
#### 3. Precisava aumentar a cobertura de testes.
#### 4. Faltou tempo para resolver os casos anteriores.
## Um rascunho da saida abaixo
``` python
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
aleatorio: Jogando dado... deu 5, posicao atual 19
propriedade ja vendida para exigente!
aleatorio sem saldo para jogar!
====================================================================================================
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
exigente: Jogando dado... deu 3, posicao atual 4
propriedade ja vendida para impulsivo!
exigente sem saldo para jogar!
====================================================================================================
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
impulsivo: Jogando dado... deu 5, posicao atual 12
propriedade ja vendida para cauteloso!
Pagando aluguel impulsivo -> 11 -> cauteloso
====================================================================================================
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cauteloso: Jogando dado... deu 5, posicao atual 19
propriedade ja vendida para exigente!
cauteloso sem saldo para jogar!
====================================================================================================
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
aleatorio: Jogando dado... deu 6, posicao atual 7
Saldo insuficiente test TipoJogar.aleatorio: Tipo: aleatorio Saldo: 23
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
exigente: Jogando dado... deu 2, posicao atual 6
propriedade ja vendida para aleatorio!
exigente sem saldo para jogar!
====================================================================================================
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
impulsivo: Jogando dado... deu 4, posicao atual 16
Saldo insuficiente test TipoJogar.impulsivo: Tipo: impulsivo Saldo: 19
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cauteloso: Jogando dado... deu 2, posicao atual 3
Saldo insuficiente test TipoJogar.cauteloso: Tipo: cauteloso Saldo: 20
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
aleatorio: Jogando dado... deu 5, posicao atual 12
propriedade ja vendida para cauteloso!
Pagando aluguel aleatorio -> 11 -> cauteloso
====================================================================================================
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
exigente: Jogando dado... deu 5, posicao atual 11
Jogo acabou!
Propriedades vendidas:
{'propriedade': 1, 'vendida': True, 'proprietario': 'impulsivo', 'alugar': 14, 'venda': 83}
{'propriedade': 4, 'vendida': True, 'proprietario': 'impulsivo', 'alugar': 57, 'venda': 138}
{'propriedade': 8, 'vendida': True, 'proprietario': 'impulsivo', 'alugar': 10, 'venda': 70}
{'propriedade': 11, 'vendida': True, 'proprietario': 'impulsivo', 'alugar': 63, 'venda': 63}
{'propriedade': 14, 'vendida': True, 'proprietario': 'impulsivo', 'alugar': 44, 'venda': 97}
{'propriedade': 17, 'vendida': True, 'proprietario': 'impulsivo', 'alugar': 46, 'venda': 76}
{'propriedade': 20, 'vendida': True, 'proprietario': 'impulsivo', 'alugar': 67, 'venda': 35}
----------
{'propriedade': 2, 'vendida': True, 'proprietario': 'cauteloso', 'alugar': 55, 'venda': 57}
{'propriedade': 12, 'vendida': True, 'proprietario': 'cauteloso', 'alugar': 11, 'venda': 85}
{'propriedade': 13, 'vendida': True, 'proprietario': 'cauteloso', 'alugar': 21, 'venda': 37}
----------
{'propriedade': 6, 'vendida': True, 'proprietario': 'aleatorio', 'alugar': 49, 'venda': 38}
{'propriedade': 9, 'vendida': True, 'proprietario': 'aleatorio', 'alugar': 11, 'venda': 42}
{'propriedade': 10, 'vendida': True, 'proprietario': 'aleatorio', 'alugar': 16, 'venda': 142}
----------
{'propriedade': 5, 'vendida': True, 'proprietario': 'exigente', 'alugar': 63, 'venda': 81}
{'propriedade': 18, 'vendida': True, 'proprietario': 'exigente', 'alugar': 57, 'venda': 37}
{'propriedade': 19, 'vendida': True, 'proprietario': 'exigente', 'alugar': 53, 'venda': 72}
----------
====================================================================================================
Saldo restante: impulsivo 19
Saldo restante: cauteloso 31
Saldo restante: aleatorio 12
Saldo restante: exigente 2
```