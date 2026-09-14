class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self.idade = idade
        self.profissao = profissao
        self.aniversario = True

    def __str__(self):
        return f'Nome: {self._nome} , idade: {self.idade} anos, profissão: {self.profissao}'

    def aniverssario(self):
        if self.aniversario:
            self.idade += 1
            return f"Feliz Aniversário! agora você tem {self.idade} anos"
        else:
            return "Hoje não é seu aniversário"

    def saudacao(self):
        return f'Olá {self.profissao}'

nome = input("nome --> ")
idade = int(input("idade --> "))
profissao = input("profissao --> ")

resultado = Pessoa(nome, idade, profissao)

print(resultado.aniversario)