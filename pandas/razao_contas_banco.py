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
colunas = ["COCONTACONTABIL", "DALANCAMENTO"]

df[colunas] = df[colunas].astype(str)

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

#==============================Etapa 4==============================
df["DALANCAMENTO"] = df["DALANCAMENTO"].str.replace("00$", "01", regex=True)
df.head()

#%%
#==============================Etapa 3==============================
df["DALANCAMENTO"] = pd.to_datetime(df["DALANCAMENTO"], format="%Y%m%d", errors="coerce")
df.head()

#%%
#==============================Etapa 5 a 9==============================
colunas_2 = ["UGDOC", "GESTAODOC", "NUDOCUMENTO", "COEVENTO", "NOEVENTO"]
df[colunas_2] = df[colunas_2].astype(str)

#%%
df[colunas_2] = df[colunas_2].replace("nan", "0000").fillna("0000")
df.head()

#%%
df["UGDOC"].value_counts()

#==============================Etapa 10==============================
df["ANO"] = df["DALANCAMENTO"].dt.year
df.head()

#%%
fr_25 = df[df["ANO"] == 2025].groupby("FR")["VALANCAMENTO"].sum().reset_index()
fr_25

#%%
saldo_bancario_25 = fr_25["VALANCAMENTO"].sum()
saldo_bancario_25

#%%
#==============================Etapa 11==============================
filtro_dia_31 = df[df["DALANCAMENTO"] == "2025-01-31"]
filtro_dia_31

#%%
fluxo_dia_31 = filtro_dia_31.groupby("FR")["VALANCAMENTO"].sum().reset_index()
fluxo_dia_31 = fluxo_dia_31["VALANCAMENTO"]

fluxo_dia_31

#%%
fr_25["Saldo Inicial"] = saldo_bancario_25 - fluxo_dia_31

#%%
fr_25

#%%
saldo_bancario_25

#Saldo Final - Qual o saldo final do dia 20? Res: Primeiro dia do ano até o dia do filtro (Dia 20) - classificado FR
#Saldo Inicial é Saldo Final - 1 dia (Até dia 19) - classificado FR

#Selecionando dia 20
#Saldo inicial (Dia anterior - (Dia 1 a 19)) - Fluxo de Caixa (Dia Selecionado (Só dia 20)) - Saldo Final (Saldo do dia Selecionado (Dia 1 a 20))

#%%
#==============================Etapa Análise Dinamica==============================
