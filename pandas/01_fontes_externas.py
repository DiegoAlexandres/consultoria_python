#%%
import pandas as pd

# dados = pd.read_csv("../dados/fContasReceber.csv")
dados = pd.read_excel("../dados/fContasReceber.xlsx")
dados.head()

#%%
type(dados)
dados.info()

#%%
colunas = ['DataCompetencia', 'DataVencimento', 'DataPagamento']

for item in colunas:
    dados[item] = pd.to_datetime(dados[item], errors='coerce')
dados.head()

#%%
dados.info()

#%%
recebidos = dados[dados['Status'] == 'RECEBIDO'].copy()
recebidos.head()

#%%
recebidos['Valor']
recebidos[recebidos['Valor'] > 100] 

#%%
total_mensal = recebidos.groupby(recebidos['DataPagamento'].dt.month)['Valor'].sum()
total_mensal

#%%
total_ano = recebidos.groupby(recebidos['DataPagamento'].dt.year)['Valor'].sum()
total_ano

#%%
total_ano = recebidos.groupby(recebidos['DataPagamento'].dt.year)['Valor'].mean()
total_ano

#%%
valor_janeiro = recebidos.groupby(recebidos['DataPagamento'].dt.month == 1)['Valor'].sum()
valor_janeiro

#%%
dados_clientes = pd.read_excel('../dados/dClientes.xlsx')
dados_clientes.head()

#%%
dados_completos = pd.merge(recebidos, dados_clientes, on='CodCliente', how='left')
dados_completos


#%%
dados_completos['Status'].unique()

#%%
dados['Status'].unique()

#%%
dados_pendentes = dados[dados['Status'] == "PENDENTE"]
dados_pendentes

#%%