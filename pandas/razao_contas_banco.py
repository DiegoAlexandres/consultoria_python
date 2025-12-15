#%%
import pandas as pd

#%%
pd.options.display.float_format = '{:,.2f}'.format

#%%
df = pd.read_excel("../dados/RazaoContasBanco_14102.xlsx")
df.head()

#%%
df.info()

#%%
#==============================Etapa 0==============================
df["COCONTACONTABIL"] = df["COCONTACONTABIL"].astype(str)

#%%
#==============================Etapa 1==============================
df["FR"] = df["COCONTACORRENTE"].str.slice(1, 8)
df.head()

#%%
filtro = df["COCONTACONTABIL"] == "1111102050000"

#%%
filtro.value_counts()

#%%
df.loc[filtro, "FR"] = df.loc[filtro, "COCONTACORRENTE"].str.slice(7, 14)
df.tail()

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 python
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 excel

#%%
#==============================Etapa 2==============================
df["BANCO"] = df["COCONTACORRENTE"].str.slice(-14)
df.head()

#%%
df.loc[df["COCONTACONTABIL"] == "1111102010000", "BANCO"] = "23703739162000"
df.head()

#%%
contas = ["1111130010000", "1111130020000"]

df.loc[df["COCONTACONTABIL"].isin(contas), "BANCO"] = "Agente Arrecadador"
df.tail()

