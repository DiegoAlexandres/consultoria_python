#%%
import pandas as pd

#%%
pd.options.display.float_format = "{:.2f}".format

#%%
from analise_receitas import relatorio_2
from analise_despesas import tabela

#%%
receitas = relatorio_2
despesas = tabela

#%%
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
def fx_resultado(receita, despesa):
    resultado = pd.concat([receita, despesa], axis=1)
    resultado.columns = ["Receitas 2025", "Despesas 2025"]
    resultado["Resultado"] = resultado["Receitas 2025"] - resultado["Despesas 2025"]
    resultado = resultado.style.format(precision=2, decimal=",", thousands=".")
    
    return resultado

#%%
fx_resultado(receitas_2025, despesas_2025)
