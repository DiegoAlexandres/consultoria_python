#%%
import pandas as pd

#%%
df = pd.read_excel("../dados/base_denis.xlsx")
df.head()

#%%
# Etapa 1

df["ANOMES"] = pd.to_datetime(df["ANOMES"], format="%Y%m", errors="coerce")
df.head()

#%%
df = df.rename(columns={"ANOMES" : "DATA"})
df.head()

#%%
# Etapa 2 - Criar coluna do cod_grupo

df["COD_GRUPO"] = None
df.head()

#%%
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Pessoal", na=False), "COD_GRUPO"] = "1"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Juros", na=False), "COD_GRUPO"] = "2"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Outras", na=False), "COD_GRUPO"] = "3"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Investimentos", na=False), "COD_GRUPO"] = "4"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Inversoes", na=False), "COD_GRUPO"] = "5"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Amortizacao", na=False), "COD_GRUPO"] = "6"
df.loc[df["DES_GRUPO_DESPESA"].str.startswith("Reserva", na=False), "COD_GRUPO"] = "9"

df.head(10)


#%%
# Etapa 3
df["RPPS"] = "Não"
df.head()

#%%
codigo_rpps = [1801261, 2801261, 1802262, 2802262, 1802202, 2802202]

#%%
df.loc[df["COD_FONTE_MAE"].isin(codigo_rpps), "RPPS"] = "Sim"
df.tail()

#%%
df["RPPS"].unique()
