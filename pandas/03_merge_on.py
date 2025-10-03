#%%
import pandas as pd
#%%
df_financeiro = pd.DataFrame({
    'Id_Funcionario': [101, 102, 103, 104],
    'Salario': [7000, 8200, 6500, 9500]
})

df_financeiro

#%%
df_rh = pd.DataFrame({
    'Id_Empregado': [101, 102, 103, 105], 
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Departamento': ['TI', 'Marketing', 'TI', 'Vendas']
})

df_rh

#%%
df_projetos = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Ana'],
    'Departamento': ['TI', 'Vendas', 'TI', 'Marketing'], 
    'Projeto': ['Sistema X', 'Campanha Y', 'Sistema Z', 'Feira W']
})

df_projetos

#%%
df = pd.merge(
    df_financeiro,
    df_rh,
    on="Id_Funcionario",
    how="left")
df.head()
#%%
df = pd.merge(
    df_financeiro,
    df_rh,
    left_on="Id_Funcionario",
    right_on="Id_Empregado",
    how="left")
df.head()

#%%
df_rh_novo_id = df_rh.rename(columns={'Id_Empregado': 'Id_Funcionario'})
df_rh_novo_id

#%%
df = pd.merge(
    df_financeiro,
    df_rh_novo_id,
    on="Id_Funcionario",
    how="left")
df.head()