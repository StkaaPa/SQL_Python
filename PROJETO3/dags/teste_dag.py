from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

#from src.validation import validar_csv

def validar_csv():
    print("Validation OK!")

with DAG(
    dag_id="teste_dag",
    start_date=datetime(2026, 8, 1),
    schedule=None,
    catchup=False,
):

    inicio = EmptyOperator(
        task_id="inicio"
    )

    validar = PythonOperator(
        task_id="validar_csv",
        python_callable=validar_csv,
    )

    fim = EmptyOperator(
        task_id="fim"
    )

    inicio >> validar >> fim