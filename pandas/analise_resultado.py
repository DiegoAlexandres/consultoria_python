#%%
import pandas as pd

#%%
pd.options.display.float_format = "{:.2f}".format

#%%
#===============================Importando receitas e despesas=====================
from analise_receitas import relatorio_2
from analise_despesas import tabela

#%%
#===============================Lendo as tabelas de receitas e despesas=====================
receitas = relatorio_2
despesas = tabela

#%%
receitas

#%%
despesas

#%%
#===============================Tratando da tabela despesas=====================
despesas = despesas.rename(columns={"VAR $":"VAR R$", "VAR. %": "VAR %"})
despesas

#%%
#===============================Forma 1 - Merge=====================
receitas

#%%
despesas

#%%
df_1 = pd.merge(receitas, despesas, on="MES", how="left", suffixes=("-RECEITAS", "-DESPESAS"))
df_1

#%%
remover_2024 = ["2024-RECEITAS", "VAR R$-RECEITAS", "VAR %-RECEITAS", "2024-DESPESAS", "VAR R$-DESPESAS", "VAR %-DESPESAS"]

#%%
df_1 = df_1.drop(columns=remover_2024)

#%%
df_1

#%%
df_1["RESULTADO-2025"] = df_1["2025-RECEITAS"] - df_1["2025-DESPESAS"]
df_1


#%%
despesas = despesas.rename(columns={'Var. $':'Var. R$', 'Var %':'Var. %'})
despesas
#%%
#Mesclar = merge
df_1 = pd.merge(receitas, despesas, on='MÊS', how='left', suffixes=('-RECEITAS', '-DESPESAS'))
df_1 = pd.merge(receitas, despesas, on="MES", how="left", suffixes=("-RECEITAS", "-DESPESAS"))
df_1