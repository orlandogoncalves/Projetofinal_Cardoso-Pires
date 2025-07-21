import pandas as pd
from scipy.stats import chisquare

# Caminho do ficheiro Excel (pode ser relativo ou absoluto)
ficheiro_excel = "dados.xlsx"

# Lê os dados do ficheiro Excel (necessário ter o openpyxl instalado)
df = pd.read_excel(ficheiro_excel)  # Por padrão lê a primeira folha

# Verifica as primeiras linhas (opcional para depuração)
print("Dados lidos do Excel:")
print(df.head())

# Garante que as colunas necessárias existem
if 'Observado' in df.columns and 'Esperado' in df.columns:
    observado = df['Observado']
    esperado = df['Esperado']

qui2, p_valor = chisquare(f_obs=observado, f_esp=esperado)

print(f"Qui-quadrado: {round(qui2, 3)}")
print(f"Valor-p: {round(p_valor, 4)}")