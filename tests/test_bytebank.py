from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_200_deve_retornar_22(self):
        #Given(contexto)
        entrada = '14/05/2004'
        esperado = 20

        funcionario_test = Funcionario('Teste', entrada, 3400)

        #Whewn(Ação)
        resultado = funcionario_test.idade()


        #Then(Desfecho)
        assert resultado == esperado

    def test_quando_sobrenome_recebe_lucas_vieira_deve_retornar_vieira(self):
        entrada = 'Lucas Vieira '
        esperado = 'Vieira'

        lucasVieira = Funcionario(entrada, '14/05/2004', 3400)

        resultado = lucasVieira.sobrenome()

        assert resultado == esperado

    def test_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada = 100000
        entrada_nome = 'Mariana Vieira'
        esperado = 90000

        funcionario_test = Funcionario('Mariana Vieira', '11/11/2001', entrada)
        funcionario_test.decrescimo_salario()

        resultado = funcionario_test.salario
        assert resultado == esperado

    @mark.calcular_bonus        #pytest -v -m calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_test = Funcionario('maria', '11/11/2001', entrada)
        resultado = funcionario_test.calcular_bonus()

        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):      #NO FINAL VAI LEVAR A UMA EXCEPTION
            entrada = 1000000

            funcionario_test = Funcionario('teste', '11/11/2020', entrada)
            resultado = funcionario_test.calcular_bonus()

            assert resultado

