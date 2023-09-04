import pandas as pd
# import math
import matplotlib.pyplot as plt
# import json
import numpy as np
# import pytz


arquivo = 'Ribeirao_Bonito-SP.TCU_NCU1.csv'
dataframe = pd.read_csv(arquivo)

# Converter a coluna de Unix para data normal em horario de brasilia
dataframe['ncu.datetime'] = pd.to_datetime(dataframe['ncu.datetime'], unit='s')
dataframe['ncu.datetime'] = dataframe['ncu.datetime'].dt.tz_localize('UTC').dt.tz_convert('America/Sao_Paulo')


# Converter as colunas de radianos para graus
for i in range (0,12):
  dataframe[f'ncu.tcus[{i}].data.Position_a1_rad_s1'] = np.degrees(dataframe[f'ncu.tcus[{i}].data.Position_a1_rad_s1'])

# Salvar o dataframe de volta como um novo arquivo CSV
novo_nome_arquivo = "seuarquivo_convertido.csv"
dataframe.to_csv(novo_nome_arquivo, index=False)

print("Conversão concluída e arquivo salvo:", novo_nome_arquivo)
