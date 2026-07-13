from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator


def ola():
    print("Olá Airflow!")


with DAG(
    dag_id="teste_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    inicio = EmptyOperator(task_id="inicio")

    teste = PythonOperator(
        task_id="teste",
        python_callable=ola,
    )

    fim = EmptyOperator(task_id="fim")

    inicio >> teste >> fim