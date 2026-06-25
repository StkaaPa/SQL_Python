from src.log import logger

def transform(df):
    logger.info("A validar dados")

    df = df[df["amount"] > 0]

    df = df[df["transaction_type"].isin(["DEPOSIT","WITHDRAWAL"])]

    return df