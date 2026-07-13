def transformar_csv(**context):
    ti = context["ti"]

    df = ti.xcom_pull(task_ids="ler_csv")

    df = df[df["cidade"] == "Porto"]

    print(df)

    return df