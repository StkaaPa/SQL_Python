# 🚀 Projeto 1 — Simple ETL with Python

🎯 Objetivo:
O primeiro projeto teve como objetivo compreender os fundamentos de um processo ETL, utilizando Python para extrair dados de um ficheiro CSV, realizar transformações e carregar os dados numa base de dados PostgreSQL.
O pipeline implementado segue o fluxo:

CSV
\\↓
\\Extract
\\↓
\\Transform
\\↓
\\Load
\\↓
\\PostgreSQL

🛠️ Tecnologias

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- CSV
- VS Code

🔄 Processo ETL

1. Extract

Os dados são lidos a partir de um ficheiro CSV utilizando Pandas.

df = pd.read_csv("data.csv") 2. Transform

São aplicadas algumas transformações aos dados, como:

- Filtragem de transações
- Conversão de datas
- Tratamento dos dados antes da carga

Exemplo:

df = df[df["amount"] > 0]
df["transaction_date"] = pd.to_datetime(df["transaction_date"]) 3. Load

Depois de transformados, os dados são carregados para PostgreSQL utilizando SQLAlchemy e Pandas.

df.to_sql("transactions",engine,if_exists="append",index=False)

📁 Estrutura

O projeto foi posteriormente organizado de forma modular:

PROJETO1/
│
├── data/
│ └── transactions.csv
│
├── extract.py
├── transform.py
├── load.py
├── main.py
│
└── README.md

Esta separação permite manter responsabilidades diferentes em módulos independentes:

- extract.py → Extração
- transform.py → Transformação
- load.py → Carregamento
- main.py → Orquestração

🧠 Principais conceitos aprendidos

- Estrutura de um pipeline ETL
- Leitura e manipulação de CSV com Pandas
- Transformação de dados
- Conversão de tipos
- Ligação Python → PostgreSQL
- SQLAlchemy
- Modularização de código Python
- Separação de responsabilidades
