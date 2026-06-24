from src.extract import extract
from src.transform import transform
from src.load import load

print("A iniciar ETL")

df = extract()

df = transform(df)

load(df)

print("ETL terminado com sucesso.")