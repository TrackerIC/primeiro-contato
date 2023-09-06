from pandas._libs.tslibs.timestamps import Timestamp
import pandas as pd
import json
import matplotlib.pyplot as plt
from tkinter import simpledialog, messagebox
# Leitura do Arquivo
arquivo = 'seuarquivo_convertido.csv'
planilha = pd.read_csv(arquivo)

# Seleção do dia e TCU com o simpledialog do tkinter, (Título, Mensagem):
entrada_Dia = simpledialog.askinteger("Dia", "Digite o dia desejado:")
entrada_TCU = simpledialog.askinteger("TCU", "Digite o TCU desejado:")



# Convertendo a coluna 'ncu.datetime' para o formato de datetime
planilha['ncu.datetime'] = pd.to_datetime(planilha['ncu.datetime'])

# Filtrando os valores apenas do dia 16
planilha_filtered = planilha[planilha['ncu.datetime'].dt.day == entrada_Dia]

# Extraindo as horas dessa coluna filtrada, formatando para forma "hora:minuto"
hours_of_day = planilha_filtered['ncu.datetime'].dt.strftime('%H:%M')

# Exibindo as horas como lista
listaHoras_dia = hours_of_day.tolist()
arquivo_selec = pd.read_csv('seuarquivo_convertido.csv', nrows=len(listaHoras_dia))

# Criando um JSON a partir da lista, apenas por estética do print
# print(json.dumps(listaHoras_dia, indent=4))


padrao = 'ncu.tcus\[(\d+)\]\.data.Position_a1_rad_s1'
colunas_com_padrao = [coluna for coluna in planilha.columns if pd.Series(coluna).str.match(padrao).any()]
# Calculando o número de colunas com o padrão
numero_de_colunas_com_padrao = len(colunas_com_padrao)
# print(f"Número de colunas com o padrão '{padrao}': {numero_de_colunas_com_padrao}")

diaMin = min(planilha['ncu.datetime'].dt.day)
diaMax = max(planilha['ncu.datetime'].dt.day)






# GRAFICO
if (entrada_Dia >= diaMin and entrada_Dia <= diaMax) and (entrada_TCU>0 and entrada_TCU<=numero_de_colunas_com_padrao):

    # Pega o valor do TCU
    listaPosTCU = arquivo_selec[f'ncu.tcus[{entrada_TCU}].data.Position_a1_rad_s1'].tolist()
    # Suas duas listas de valores
    lista_x = listaHoras_dia
    lista_y = listaPosTCU

    # Configura os eixos e formata o estilo do gráfico
    plt.plot(lista_x, lista_y, 'r-')

    # Rotacionar rótulos do eixo X para melhor legibilidade (opcional)
    intervalo_legendas = 10 # Configura o intervalo dos termos do eixo
    plt.xticks(range(0, len(lista_x), intervalo_legendas), rotation=90)


    # Adicionar rótulos aos eixos
    plt.xlabel('Data/Hora')
    plt.ylabel(f'Posição TCU{entrada_TCU}')

    # Adicionar título ao gráfico
    plt.title(f'Gráfico de Posição do TCU{entrada_TCU} Dia {entrada_Dia}')

    # Ajustar layout para evitar cortes nos rótulos
    plt.tight_layout()

    # Mostrar o gráfico
    plt.show()
elif(entrada_Dia < diaMin or entrada_Dia > diaMax):
    messagebox.showinfo("Alerta", f"O número do dia é menor que {diaMin} ou maior que {diaMax}")
elif(entrada_TCU < 0 or entrada_TCU > numero_de_colunas_com_padrao):
    messagebox.showinfo("Alerta", f"O número do TCU não está presente na planilha")
print("Testando o camanda")
