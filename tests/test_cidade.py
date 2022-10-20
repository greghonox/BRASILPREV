from banco_imobiliario.cidade_imobiliaria import CidadeImobiliaria
from unittest import TestCase

class TestCidade(TestCase):
    def test_gerar_cidade(self) -> None:
        cidade = CidadeImobiliaria()
        self.assertIsInstance(cidade.propriedades, list)

    def test_percorrer_propriedades(self) -> None:
        cidade = CidadeImobiliaria()
        for contador, propriedade in enumerate(cidade):
            if contador == len(cidade.propriedades):
                break
            print(propriedade)
