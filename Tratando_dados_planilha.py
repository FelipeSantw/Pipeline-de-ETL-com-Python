"""Separar string a cada 2 caracteres

Original file is located at
    https://colab.research.google.com/drive/17KJJqsPOsxPfIzjrrFtdK28NVCEA7Wet

# **Trabalhando com dados**

**Linguagem: Python;
Plataforma utilizada: Google Colab;**

Objetivo:

- Export: Coletar dados de uma planilha excel contendo uma série de endereços MAC;
- Tranform: aplicar formatação da coluna "MAC", realizando separação dos dados a cada 2 caracteres, inserindo o valor ":". Padronizando estes endereços MAC;
- Carregar essa planilha atualizada em um computador local.
"""

import pandas as pd
from google.colab import files

# Carregando o arquivo Excel
uploaded = files.upload()

coluna_alvo = 'MAC'

# Leitura do DataFrame
df = pd.read_excel(next(iter(uploaded)), engine='openpyxl')

# Aplica a separação de dois em dois caracteres com ":"
df[coluna_alvo] = df[coluna_alvo].apply(lambda x: ':'.join(x[i:i+2] for i in range(0, len(x), 2)))

# Salve o DataFrame de volta no arquivo Excel
output_file = 'resultado.xlsx'
df.to_excel(output_file, sheet_name='mac_att', index=False)

# Faça o download do arquivo resultante
files.download(output_file)

print("Strings divididas e arquivo de saída gerado com sucesso!")
