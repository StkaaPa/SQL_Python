from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

def gerar_nome():
    print("A gerar o nome...")
    return "Sam"

def mostrar_nome(**context):
    ti=context["ti"]
    nome=ti.xcom_pull(task_ids="gerar_nome")
    print(f"Olá {nome}")

with DAG(
    dag_id="first_dag",
    start_date=datetime(2026,6,16),
    schedule=None,
    catchup=False,
    tags=["learning"],
) as dag:
    inicio = EmptyOperator(
        task_id="inicio"
    )

    gerar = PythonOperator(
        task_id="gerar_nome",
        python_callable=gerar_nome,
    )

    mostrar = PythonOperator(
        task_id="mostrar_nome",
        python_callable=mostrar_nome,
    )

    fim=EmptyOperator(
        task_id="fim"
    )

    inicio>>gerar>>mostrar>>fim