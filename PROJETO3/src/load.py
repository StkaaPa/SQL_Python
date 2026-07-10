from src.database import get_engine

def carregar_csv(**context):
    ti=context["ti"]
    carregarcsv=ti.xcom_pull(task_ids="transformar_csv")

    engine = get_engine()

    carregarcsv.to_sql(
        name="stg_clientes_proj3",
        con=engine,
        if_exists="append",
        index=False
    )
    
    print(f"{len(carregarcsv)} registos carregado para staging_clientes_proj3")