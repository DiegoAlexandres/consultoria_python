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
#===============================Caminhho 1 - Utilizando Merge=====================
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
#===============================Caminhho 2 - Criar um novo df com concat=====================
receitas

#%%
despesas

#%%
receitas_2025 = receitas[2025]
receitas_2025

#%%
despesas_2025 = despesas[2025]
despesas_2025

#%%
df_2 = pd.concat([receitas_2025, despesas_2025], axis=1)
df_2

#%%
novas_colunas = ["Receitas Primárias", "Despesas Primárias"]

#%%
df_2.columns = novas_colunas
df_2

#%%
df_2["Resultado Primário"] = df_2["Receitas Primárias"] - df_2["Despesas Primárias"]
df_2

#%%
# df_2["Resultado Primário"] = receitas_2025 - despesas_2025
# df_2

#%%
df_2

#%%
df_2.style.format(
    precision=2,    # Casas decimais
    decimal=",",    # Separador de decimal 
    thousands="."   # Separador de muilhar
)

#%%
type(df_2)

#%%
from analise_fonte import teste

#%%
teste