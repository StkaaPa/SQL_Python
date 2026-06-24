import pandas as pd

def extract():
    print("A ler ficheiro CSV...")

    df = pd.read_csv("transactions.csv")

    print("Registos Lidos:")
    print(df)

    return df