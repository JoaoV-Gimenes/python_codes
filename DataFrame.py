import pandas as pd

df = pd.DataFrame({
    "pedido": [1001, 1002, 1003, 1004, 1005, 1006],
    "produto": ["Notebook", "Mouse", "Monitor",
                "Teclado", "Notebook", "Webcam"],
    "categoria": ["Informatica", "Acessorio",
                  "Informatica", "Acessorio",
                  "Informatica", "Acessorio"],
    "regiao": ["SP", "RJ", "SP", "MG", "RJ", "SP"],
    "preco": [4200.0, 89.9, 1350.0,
              210.0, 3990.0, 149.9],
    "qtd": [2, 10, 3, 5, 1, 4],
})

print(df)
