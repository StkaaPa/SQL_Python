import pandas as pd

def transform(df):

    print("A transformar dados....")

    df = df[df["amount"] > 0]

    df["transaction_date"] = pd.to_datetime(df["transaction_date"])

    print("Após transformação:")
    print(df)

    return(df)