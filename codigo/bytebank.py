from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nasciemnto_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nasciemnto_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self.nome.strip()   #tirando espaçoes em branco
        nome_quebrado = nome_completo.split(' ') #quebrando o espaço em branco
        return nome_quebrado[-1] #retornando o ultimo elemento

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber um bônus')
        return valor

    def _definindo_diretor(self):
        sobrenomes = ['Vieira', 'Alves', 'Silva', 'Maia', 'Galvão', 'Gonçalves', 'Pereira']
        return (self._salario >= 100000) and (self.sobrenome() in sobrenomes)
        
    def decrescimo_salario(self):
        if self._definindo_diretor():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
