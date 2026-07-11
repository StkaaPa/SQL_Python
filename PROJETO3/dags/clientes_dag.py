from src.extract import ler_csv
from src.validation import validar_csv
from src.load import carregar_csv
from src.transform import transformar_csv
from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
    
with DAG(
    dag_id="clientes_dag",
    start_date=datetime(2026,8,1),
    schedule=None,
    catchup=False,
    tags=["Project3", "clientes"],
) as dag:

    inicio=EmptyOperator(
        task_id="Inicio"
    )

    validar = PythonOperator(
        task_id="validar_csv",
        python_callable=validar_csv,
    )

    extrair = PythonOperator(
        task_id="ler_csv",
        python_callable=ler_csv,
    )

    transformar = PythonOperator(
        task_id="transformar_csv",
        python_callable=transformar_csv,
    )

    carregar=PythonOperator(
        task_id="carregar_csv",
        python_callable=carregar_csv
    )

    fim=EmptyOperator(
        task_id="fim"
    )

inicio>>validar>>extrair>>transformar>>carregar>>fim