from sqlalchemy import create_engine

def load(df):

    print("A carregar dados para PostgreSQL...")

    engine = create_engine(
        "postgresql://postgres:SUA_PASSWORD@localhost:5432/banking_dw"
    )

    df.to_sql(
        "transactions",
        engine,
        if_exists="append",
        index=False
    )

    print("Carga concluída.")