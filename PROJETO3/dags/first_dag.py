from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

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
        task_id="preparar"
    )

    fim=EmptyOperator(
        task_id="fim"
    )

    inicio>>preparar>>fim