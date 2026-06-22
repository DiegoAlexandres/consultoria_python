# Consultoria Python: Análise Fiscal de Receitas e Despesas Públicas

Projeto de consultoria em Python aplicado a um caso real de cliente do setor público: tratamento de bases de receitas e despesas orçamentárias para apuração do Resultado Primário, com ensino prático de pandas ao longo do processo.

## Sobre o projeto

A demanda do cliente era tratar bases brutas de receitas e despesas para chegar ao Resultado Primário — métrica fiscal que exclui operações financeiras (juros, RPPS, amortizações) e considera apenas receitas e despesas primárias. O trabalho envolveu classificação de natureza orçamentária, identificação de receitas/despesas previdenciárias (RPPS), e construção de relatório comparativo mês a mês entre exercícios.

## O que foi feito

**Despesas**
- Classificação por grupo de despesa (Pessoal, Juros, Investimentos, Amortização, Reserva)
- Identificação de despesas RPPS por código de fonte
- Construção do código de natureza orçamentária (categoria + grupo + modalidade + elemento)
- Classificação primário vs financeiro por padrão de natureza
- Cálculo de total pago (incluindo exercício anterior)
- Relatório mensal comparativo com variação absoluta e percentual

**Receitas**
- Identificação de receitas RPPS por código de fonte
- Classificação primário vs financeiro por padrão de natureza
- Relatório mensal comparativo com variação absoluta e percentual

**Resultado Primário**
- Cruzamento de receitas e despesas primárias por mês
- Duas abordagens de consolidação: `merge` e `concat`
- Cálculo do resultado primário mensal (receitas − despesas)

## Estrutura

consultoria_python/

├── dados/                  → bases de receitas e despesas

├── fundamentos/            → scripts numerados por tópico de Python

├── pandas/                 → scripts de análise e tratamento

│   ├── analise_despesas.py

│   ├── analise_receitas.py

│   └── resultado_primario.py

├── main.py

├── pyproject.toml

├── requirements.txt

└── uv.lock

## Tecnologias

![Python](https://img.shields.io/badge/Python_3.14-FFD43B?style=flat-square&logo=python&logoColor=blue)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9?style=flat-square&logo=uv&logoColor=white)

## Técnicas aplicadas

- Leitura e tratamento de planilhas Excel (`read_excel`, `openpyxl`)
- Conversão de tipos e datas (`astype`, `to_datetime`)
- Classificação condicional em massa (`loc`, `str.contains`, regex)
- Agregações temporais (`groupby`, `pivot_table`)
- Combinação de bases (`merge`, `concat`)
- Formatação de saída para relatório (`style.format`)

## Como executar

Projeto migrado de `pip` para `uv` durante o desenvolvimento. Ambas as formas funcionam:

**Com uv (recomendado)**
```bash
uv sync
uv run main.py
```

**Com pip**
```bash
pip install -r requirements.txt
python main.py
```

---

📫 [openbiinteligencia.com.br](https://openbiinteligencia.com.br/)
