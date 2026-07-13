from src.database import get_engine

def carregar_csv(**context):

    ti = context["ti"]

    df = ti.xcom_pull(task_ids="transformar_csv")

    engine = get_engine()

    df.to_sql(
        name="stg_clientes_proj3",
        con=engine,
        if_exists="append",
        index=False,
    )

    print(f"{len(df)} registos carregados para a tabela stg_clientes.")

    return len(df)