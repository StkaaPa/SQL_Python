from src.log import logger
import pandas as pd

def extract():
    logger.info("A ler CSV")

    df = pd.read_csv("data/transactions.csv")
    
    return df