from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

def dizer_ola():
    print("Olá! Este é o meu primeiro PythonOperator!")

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

    preparar=EmptyOperator(
        task_id="preparar",
        python_callable=dizer_ola,
    )

    fim=EmptyOperator(
        task_id="fim"
    )

    inicio>>preparar>>fim