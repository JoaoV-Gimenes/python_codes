import requests
import pandas as pd

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"

params = {
    "formato": "json",
    "dataInicial": "01/01/2019",
    "dataFinal": "31/12/2025"
}

#resp = requests.get(url.format(codigo=433), params=params)
#resp.raise_for_status()
#dados = resp.json()

#df = pd.DataFrame(dados)

#df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
#df["valor"] = pd.to_numeric(df["valor"])

#######################################################


series = {
    "ipca": 433,          # inflação oficial do mês (%)
    "igpm": 189,          # IGP-M do mês (%)
    "selic": 4390,        # Selic acumulada no mês (%)
    "dolar": 3698,        # dólar comercial – média do mês (R$)
    "desemprego": 24369,  # taxa de desocupação (%)
}

tabelas = []
for nome, codigo in series.items():
    resp = requests.get(url.format(codigo=codigo), params=params)

    resp.raise_for_status()
    parcial = pd.DataFrame(resp.json())

    parcial["data"] = pd.to_datetime(parcial["data"], format="%d/%m/%Y")
    parcial[nome] = pd.to_numeric(parcial["valor"])

    tabelas.append(parcial[["data", nome]].set_index("data"))

df = pd.concat(tabelas, axis=1).reset_index()
print(df)

df.to_excel("dados.xlsx")