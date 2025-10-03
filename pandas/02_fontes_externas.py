#%%
import pandas as pd

#%%
df_receber = pd.read_excel("../dados/fContasReceber.xlsx")
df_receber.head()

#%%
df_categorias = pd.read_excel("../dados/dCategorias.xlsx")
df_categorias.head()

#%%
df = pd.merge(
    df_receber,
    df_categorias,
    left_on="CodCategoria",
    right_on="id_Categoria_Nivel_3",
    how="left"
)

df.head()

#%%
df_2 = df_receber.merge(df_categorias, left_on="CodCategoria", right_on="id_Categoria_Nivel_3", how="left")
df_2.head()

#%%
df.groupby("Status")["Valor"].sum()