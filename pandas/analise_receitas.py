#%%
import pandas as pd

#%%
pd.options.display.float_format = "{:.2f}".format

#%%
df = pd.read_excel("../dados/Base_Receitas.xlsx")
df.head()

#%%
df.info()

#%%
#===============================Etapa 1=====================================
df["ANOMES"] = pd.to_datetime(df["ANOMES"], format="%Y%m")

#%%
df.info()

#%%
df["Cod_Natureza"] = df["Cod_Natureza"].astype(str)

#%%
df.info()

#%%
#===============================Etapa 2=====================================
codigo_rpps = [1801261, 2801261, 1802262, 2802262, 1802202, 2802202]     

df["RPPS"] = "Não"

#%% 
df.loc[df["COD_FONTE_MAE_RPPS"].isin(codigo_rpps), "RPPS"] = "Sim"

#%%
df["RPPS"].value_counts()

#%%
#===============================Etapa 3=====================================
# 1321%; 2230%; 21%; 23%; 1990111%; 1922012%; 1990992%

padroes = '^(13|22|21|23)|^1990111|^1922012|^1990992'

#%%
df["PRIMARIO"] = "P"

df.head()

#%%
df.loc[df["Cod_Natureza"].str.contains(padroes, na=False), "PRIMARIO"] = "F"

df.head()
#%%
df["PRIMARIO"].value_counts()

#%%
#===============================Etapa 4=====================================
df_financeiro = df[df["PRIMARIO"] == "F"]
df_financeiro
#%%
df_financeiro["Cod_Natureza"].value_counts()

#%%
df

#%%
#===============================Relatório Etpa 1=====================================
df_novo = df[(df["RPPS"] == "Não") & (df["PRIMARIO"] == "P")].copy()
df_novo

#===============================Relatório Etpa 2=====================================
df_novo["ANO"] = df_novo["ANOMES"].dt.year
df_novo["MES"] = df_novo["ANOMES"].dt.month

df_novo

#%%
#===============================Relatório Etpa 3=====================================
relatorio = df_novo.groupby(["ANO", "MES"])["Receita Líquida"].sum().reset_index()
relatorio

#%%
#===============================Relatório Etpa 4=====================================
relatorio_2 = relatorio.pivot_table(index="MES", columns="ANO", values="Receita Líquida")
relatorio_2.fillna(0)

#===============================Relatório Etpa 4=====================================
relatorio_2["VAR R$"] = relatorio_2[2025] - relatorio_2[2024] 
relatorio_2

#%%
relatorio_2["VAR R$"] = relatorio_2["VAR R$"] - relatorio_2[2024] 
relatorio_2
