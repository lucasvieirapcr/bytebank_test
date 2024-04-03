from codigo.bytebank import Funcionario

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