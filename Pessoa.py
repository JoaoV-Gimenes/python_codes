class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self.idade = idade
        self.profissao = profissao
        self.aniversario = True

    def __str__(self):
        return f'Nome: {self._nome} , idade: {self.idade} anos, profissão: {self.profissao}'

    def func_aniversario(self):
        if self.aniversario:
            self.idade += 1
            print(f"Feliz Aniversário! agora você tem {self.idade} anos")
            print(f'Nome: {self._nome} , idade: {self.idade} anos, profissão: {self.profissao}')
            return self.idade
        else:
            return "Hoje não é seu aniversário"

    def saudacao(self):
        return f'Olá {self.profissao}'


resultado = Pessoa("João", 18, "ajsjhasjb")

print(resultado.func_aniversario())