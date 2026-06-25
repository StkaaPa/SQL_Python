from src.extract import extract
from src.transform import transform
from src.load import (load_stg, load_target)
from src.log import logger

try:
    logger.info("Início do ETL")

    df = extract()

    load_stg(df)

    df = transform(df)

    load_target(df)

    logger.info("ETL concluído com sucesso!")

except Exception as e:
    logger.error(str(e))

    raise