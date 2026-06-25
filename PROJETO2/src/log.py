import logging

logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()