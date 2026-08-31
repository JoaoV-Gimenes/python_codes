import pandas as pd

class mercado:
    def __init__(self):
        self.lista = {}

    def adicionar(self):
        item = input("Item --> ")
        while True:
            try:
                preco = float(input("Preço do produto --> "))
                quantidade = int(input("Quantidade --> "))
                break

            except ValueError:
                print("Valor inserido não é válido")

        preco_final = preco * quantidade
        compra = [preco, quantidade, preco_final]
        self.lista[item] = compra
        df = pd.DataFrame(self.lista)
        print(df)
        return self.lista

    def resetar(self):
        print("deletando lista")
        return self.lista.clear()

    def deletar(self):
        item_deletar = input("Item a ser deletado --> ")
        return self.lista.pop(item_deletar)

classe = mercado()
acoes = {
        1: classe.adicionar,
        2: classe.deletar,
        3: classe.resetar,
    }
while True:
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - remover produto")
    print("4 - sair")

    acao = int(input("ação --> "))

    if acao in acoes:
        acao = acoes[acao]
        acao()

    elif acao == 4:
        print("Saindo do programa!")
        break

    else:
        print("ação inválida")