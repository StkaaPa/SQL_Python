# Projeto 1 — ETL Básico com Python e PostgreSQL

Primeiro projeto da série. É um pipeline ETL mínimo que lê um ficheiro CSV de transações bancárias, aplica uma limpeza simples com Pandas e carrega o resultado numa tabela PostgreSQL através do SQLAlchemy.

O objetivo foi perceber o ciclo **Extract → Transform → Load** de ponta a ponta, antes de acrescentar staging, logging e orquestração nos projetos seguintes.

## Arquitetura

```
data/transactions.csv  ──►  extract()  ──►  transform()  ──►  load()  ──►  PostgreSQL
      (origem)             (Pandas)         (Pandas)        (SQLAlchemy)   banking_dw.transactions
```

Cada fase está isolada no seu próprio módulo, e o `main.py` limita-se a encadeá-las.

## Stack

| Componente | Utilização |
|---|---|
| Python 3 | Linguagem do pipeline |
| Pandas | Leitura do CSV e transformação |
| SQLAlchemy | Ligação e carga para a base de dados |
| psycopg2 | Driver PostgreSQL |
| PostgreSQL | Destino dos dados |

## Estrutura

```
PROJETO1/
├── main.py                # Ponto de entrada: extract → transform → load
├── data/
│   └── transactions.csv   # Dados de entrada
├── Sql/
│   └── create_table.sql   # DDL da tabela de destino
└── src/
    ├── extract.py         # Leitura do CSV
    ├── transform.py       # Regras de limpeza
    └── load.py            # Carga para o PostgreSQL
```

## Dados

O ficheiro `data/transactions.csv` contém transações bancárias com as colunas:

| Coluna | Descrição |
|---|---|
| `transaction_id` | Identificador da transação |
| `account_id` | Identificador da conta |
| `transaction_date` | Data da transação |
| `transaction_type` | `DEPOSIT` ou `WITHDRAWAL` |
| `amount` | Montante |

Exemplo:

```csv
transaction_id,account_id,transaction_date,transaction_type,amount
1,1001,2026-06-01,DEPOSIT,1000
2,1001,2026-06-01,WITHDRAWAL,200
3,1002,2026-06-01,DEPOSIT,500
4,1003,2026-06-01,WITHDRAWAL,-50
```

## Transformações

Em `src/transform.py`:

1. **Filtro de montantes:** só ficam os registos com `amount > 0`.
2. **Conversão de tipos:** `transaction_date` passa de texto para `datetime`.

Com os dados de exemplo, são lidos 4 registos e carregados 3 (a transação 4 tem montante negativo e é descartada).

## Modelo de dados

```sql
CREATE TABLE transactions (
    transaction_id BIGINT,
    account_id BIGINT,
    transaction_date DATE,
    transaction_type VARCHAR(20),
    amount NUMERIC(12,2)
);
```

## Como executar

**Pré-requisitos:** Python 3 e um servidor PostgreSQL acessível.

1. Criar a base de dados `banking_dw` e a tabela de destino:

   ```bash
   psql -U postgres -c "CREATE DATABASE banking_dw;"
   psql -U postgres -d banking_dw -f Sql/create_table.sql
   ```

2. Ajustar a *connection string* em `src/load.py` (utilizador, palavra-passe, host e porta) para o teu ambiente.

3. Instalar as dependências:

   ```bash
   pip install pandas sqlalchemy psycopg2-binary
   ```

4. Executar a partir da pasta do projeto (o caminho do CSV é relativo):

   ```bash
   cd PROJETO1
   python main.py
   ```

Saída esperada (resumida):

```
A iniciar ETL
A ler ficheiro CSV...
A transformar dados....
A carregar dados para PostgreSQL...
Carregamento concluída.
ETL terminado com sucesso.
```

Para confirmar o resultado:

```sql
SELECT * FROM transactions;
```

## Limitações conhecidas

Este projeto é deliberadamente simples. Os pontos abaixo são o que os projetos seguintes vão resolver:

- **Sem idempotência:** a carga usa `if_exists="append"` e a tabela não tem chave primária, por isso correr o pipeline duas vezes duplica os registos.
- **Sem tabela de staging:** os dados vão diretamente para a tabela final.
- **Logging com `print`:** não há ficheiro de log nem níveis de severidade.
- **Sem controlo de execuções:** não fica registo de quantas linhas foram lidas/carregadas nem do estado da execução.
- **Credenciais no código:** a *connection string* está escrita em `load.py`.

## O que aprendi

- Estruturar um ETL em funções/módulos separados por fase.
- Ler, filtrar e converter dados com Pandas.
- Carregar um `DataFrame` em PostgreSQL com `to_sql` e SQLAlchemy.
- Definir o DDL da tabela de destino separadamente do código Python.

