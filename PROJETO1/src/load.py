from sqlalchemy import create_engine

def load(df):

    print("A carregar dados para PostgreSQL...")

    engine = create_engine(
        "postgresql://postgres:***@localhost:5432/bankingDW"
    )

    df.to_sql(
        "transactions",
        engine,
        if_exists="append",
        index=False
    )

    print("Carregamento concluída.")