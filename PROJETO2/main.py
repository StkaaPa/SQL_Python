from src.extract import extract
from src.transform import transform
from src.load import (load_stg, load_target)
from src.p_control import (insert_p_control_proj2)
from src.log import logger

try:
    logger.info("Início do ETL")

    df = extract()

    load_stg(df)

    rows_read = len(df)

    df = transform(df)

    rows_loaded = len(df)

    load_target(df)

    insert_p_control_proj2(
        rows_read,
        rows_loaded,
        "SUCCESS"
    )

    logger.info("ETL concluído com sucesso!")

except Exception as e:
    logger.error(str(e))

    insert_p_control_proj2(
        0,
        0,
        "ERROR",
        str(e)
    )

    raise