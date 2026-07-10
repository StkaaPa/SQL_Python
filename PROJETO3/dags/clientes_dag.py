from src.extract import ler_csv
from src.validation import validar_csv
from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

def caminho_csv(**context):
    ti=context["ti"]
    directory=ti.xcom_pull(task_ids="validar_csv")
    print(f"O caminho é: {directory}")
    
with DAG(
    dag_id="clientes_dag",
    start_date=datetime(2026,08,01),
    schedule=None,
    catchup=False,
    tags=["Project3"],
) as dag:

    inicio=EmptyOperator(
        task_id="Inicio"
    )

    validar = PythonOperator(
        task_id="Validar_csv",
        python_callable=ler_csv,
    )

    fim=EmptyOperator(
        task_id="fim"
    )

inicio>>extrair>>fim