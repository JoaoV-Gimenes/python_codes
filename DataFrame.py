import pandas as pd

dados = pd.read_csv("manutencao_preditiva.csv")

##dadosL = dados[dados["Tipo"] == "L"]
##dadosH = dados[dados["Tipo"] == "H"]
##dadosM = dados[dados["Tipo"] == "M"]

######################################

##print(dados["Tipo"].value_counts())

########################################

##print(dados["Tipo da Falha"].value_counts())

##############################################

#df = dados[dados["Tipo da Falha"] == "Power Failure"]

#########################################

#print(df["Tipo"].value_counts())

########################################

x = dados['UDI']
y1 = dados['Temperatura Processo [K]']
y2 = dados['Velocidade Rotacao [rpm]']
y3 = dados['Torque [Nm]']

import matplotlib.pyplot as plt

plt.plot(x, y3)
plt.show()
 ####################################

dados1 = dados[(dados["Tipo de Falha"] == "Power Failure") & (dados["Tipo"] == "M")]