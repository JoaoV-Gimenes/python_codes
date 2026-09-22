import requests
import pandas as pd
from pandas.core.methods.selectn import SelectNSeries

# 1) Endereço da API (endpoint)
url = "https://api.open-meteo.com/v1/forecast"

# 2) As 10 variáveis que queremos
variaveis = [
    "temperature_2m",             # temperatura do ar (°C)
    "apparent_temperature",       # sensação térmica (°C)
    "relative_humidity_2m",       # umidade relativa (%)
    "precipitation",              # chuva acumulada na hora (mm)
    "precipitation_probability",  # probabilidade de chuva (%)
    "cloud_cover",                # cobertura de nuvens (%)
    "wind_speed_10m",             # velocidade do vento (km/h)
    "wind_direction_10m",         # direção do vento (°)
    "pressure_msl",               # pressão ao nível do mar (hPa)
    "uv_index",                   # índice UV
]

# 3) Parâmetros da requisição: local, variáveis e fuso horário
params = {
    "latitude": -23.55,           # São Paulo
    "longitude": -46.63,
    "hourly": ",".join(variaveis),
    "timezone": "America/Sao_Paulo",
}

# 4) Chamada à API
resp = requests.get(url, params=params, timeout=10)
resp.raise_for_status()           # para o programa se a API retornar erro
dados = resp.json()               # converte a resposta JSON em dicionário Python

# 5) Transformar em DataFrame
df = pd.DataFrame(dados["hourly"])
df["time"] = pd.to_datetime(df["time"])

# 6) (Opcional) Renomear as colunas para português
df = df.rename(columns={
    "time": "data_hora",
    "temperature_2m": "temperatura",
    "apparent_temperature": "sensacao_termica",
    "relative_humidity_2m": "umidade",
    "precipitation": "chuva_mm",
    "precipitation_probability": "prob_chuva",
    "cloud_cover": "nuvens",
    "wind_speed_10m": "vento_kmh",
    "wind_direction_10m": "vento_direcao",
    "pressure_msl": "pressao",
    "uv_index": "indice_uv",
})

df.head()


## 1. Utilizando os dados da API anterior, responda as seguinte perguntas:

##a) Quais os valores médios, medianos, min e max das colunas temperatura, "sensacao_termica",
##"umidade", "chuva_mm".

colunas = ["temperatura", "sensacao_termica", "umidade", "chuva_mm"]
df[colunas].agg(["min", "max", "mean", "median"])

## b) Em função da temperatura mediana, crie uma coluna que compara cada linha da coluna temperatura com a temperatura mediana e traga a informação se está abaixo, acima ou igual a mediana.
mediana = df["temperatura"].median()
df["status"] = df["temperatura"].apply(
    lambda x: "baixo" if x < mediana
    else "alto" if x > mediana
    else "igual" if x == mediana
    else None
)
print(df[["temperatura", "status"]])

#c) Plote a temperatura e sensacao_térmica em um único gráfico.

# Plote temperatura e sensacao_térmica
import matplotlib.pyplot as plt

x = df['data_hora']
y1 = df['temperatura']
y2 = df['sensacao_termica']
y3 = df['pressao']

plt.plot(x, y1, x, y2, x, y3)
plt.xlabel("Data")
plt.ylabel("Temperatura e Sensação Térmica e Pressão")
plt.legend(['Temperatura', 'Sensação Térmica', 'Pressão'])
plt.show()