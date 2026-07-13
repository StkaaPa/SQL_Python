import pandas as pd


def ler_csv(**context):
    ti = context["ti"]

    caminho = ti.xcom_pull(task_ids="validar_csv")

    df = pd.read_csv(caminho)

    print(df)

    return df