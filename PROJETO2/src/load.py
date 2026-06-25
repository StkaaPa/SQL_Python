from src.log import logger
from sqlalchemy import create_engine

from config import (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)

def get_engine():
    conection_string = (
        f"postgresql://"
        f"{DB_USER}:"
        f"{DB_PASSWORD}@"
        f"{DB_HOST}:"
        f"{DB_PORT}/"
        f"{DB_NAME}"
    )

    return create_engine(conection_string)

def load_stg(df):
    logger.info("A carregar dados para STG_TRANSACTIONS_PROJ2")

    engine = get_engine()

    df.to_sql(
        "stg_transactions_proj2",
        engine,
        if_exists = "replace",
        index=False
    )

    logger.info(f"{len(df)} registos carregados na tabela staging")

def load_target(df):
    logger.info("A carregar dados para TRANSACTIONS_PROJ2")

    engine = get_engine()

    df.to_sql(
        "transactions_proj2",
        engine,
        if_exists = "replace",
        index=False
    )

    logger.info(f"{len(df)} registos carregados na tabela target")