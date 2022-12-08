from tkinter.filedialog import askopenfilenames
import pandas as pd
import ntpath

diretorio_arquivos = askopenfilenames()

lista_dados = []

for diretorio_atual in diretorio_arquivos:
    nome_tabela = ntpath.basename(diretorio_atual)
    df = pd.read_excel(diretorio_atual, usecols="I", skiprows=6)

    #lista_dados.append(df.values.tolist())
    valores_lista = df.values.tolist()
    for valor in valores_lista:
        lista_dados.append(valor[0])

valor_maximo = max(lista_dados)
lista_dados_pu = [(x / valor_maximo)*100 for x in lista_dados]

print(lista_dados)
print("-------")
print(valor_maximo)
print("-------")
print(lista_dados_pu)

with open('dados.txt', 'w') as f:
    for valor in lista_dados_pu:
        f.write(str(valor))
        f.write('\n')