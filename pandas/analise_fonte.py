#%%
import pandas as pd

#%%
pd.options.display.float_format = "{:.2f}".format

#%%
#===============================Importando receitas e despesas=====================
from analise_receitas import df

#%%
df_receitas = df
df

#%%
from analise_despesas import df

#%%
df_despesas = df
df

#%%
df_receitas.head()

#%%
df_despesas.head()

#%%
#===============================Filtrando a tabela de receitas=====================
df_receitas_2025 = df_receitas[df_receitas["ANOMES"].dt.year == 2025]
df_receitas_2025

#%%
df_receitas_2025.info()

#%%
#===============================Alterando o tipo para string=====================
df_receitas_2025["COD_FONTE_MAE_RPPS"] = df_receitas_2025["COD_FONTE_MAE_RPPS"].astype(str)
df_receitas_2025

#%%
df_receitas_2025.info()

#%%
df_receitas_2025 = df_receitas_2025.rename(columns={"COD_FONTE_MAE_RPPS": "COD_FONTE_MAE"})
df_receitas_2025

#%%
#===============================Agrupoando por codigo fonte=====================
df_receitas_2025 = df_receitas_2025.groupby("COD_FONTE_MAE")["Receita Líquida"].sum()
df_receitas_2025

#%%
df_receitas_2025

#%%
#===============================Filtrando a tabela de despesas=====================
df_despesas_2025 = df_despesas[df_despesas["DATA"].dt.year == 2025]
df_despesas_2025

#%%
#===============================Alterando o tipo para string=====================
df_despesas_2025["COD_FONTE_MAE"] = df_despesas_2025["COD_FONTE_MAE"].astype(str)

#%%
df_despesas_2025.info()

#%%
#===============================Filtrando a tabela pelo codigo fonte 1=====================
df_despesas_2025_fr1 = df_despesas_2025.loc[df_despesas_2025["COD_FONTE_MAE"].str.startswith("1", na=False)]
df_despesas_2025_fr1

#%%
df_despesas_2025_fr1["COD_FONTE_MAE"].unique()

#%%
#===============================Agrupoando por codigo fonte despesas=====================
df_receitas_2025

#%%
df_despesas_2025_fr1

#%%
df_despesas_2025_fr1 = df_despesas_2025_fr1.groupby("COD_FONTE_MAE")["PAGO"].sum()
df_despesas_2025_fr1

#%%
#===============================Agrupoando por codigo fonte df final=====================
df_final = pd.concat([df_receitas_2025, df_despesas_2025_fr1], axis=1)
df_final

#%%
df_final["Receitas - Despesas"] = df_final["Receita Líquida"] - df_final["PAGO"]
df_final

#%%
df_final = df_final.fillna(0)

#%%
df_final

#%%
df_negativo = df_final[df_final["Receitas - Despesas"] < 0]
df_negativo

#%%
df_positivo = df_final[df_final["Receitas - Despesas"] > 0]
df_positivo

#%%
df_positivo["Receitas - Despesas"].unique()

#%%
df_final.style.format(
    precision=2,
    decimal=",",
    thousands="."
)

#%%
df_negativo

#%%
def milhar(milhar):
    return milhar.style.format(
    precision=2,
    decimal=",",
    thousands="."
)

#%%
def somar(numero_1, numero_2):
    return numero_1 + numero_2

#%%
somar(2, 2)

#%%
milhar(df_negativo)

#%%
df_negativo.style.format(
    precision=2,
    decimal=",",
    thousands="."
)
#%%
milhar(df_final)

#%%
type(df_final)


#%%
teste = milhar(df_final)
teste