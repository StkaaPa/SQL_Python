import pandas as pd

def transformar_csv(**context):
    ti=context["ti"]
    transformarCSV=ti.xcom_pull(task_ids="ler_csv")

    transformarCSV = transformarCSV[transformarCSV["cidade"] == "Porto"]
    print(transformarCSV)
    return transformarCSV