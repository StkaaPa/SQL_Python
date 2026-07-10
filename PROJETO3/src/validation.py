from pathlib import Path

def validar_csv():

    caminho = Path("/opt/airflow/data/clientes.csv")

    if not caminho.exists():
        raise FileNotFoundError(f"O ficheiro {caminho} não existe.")

    if caminho.stat().st_size == 0:
        raise ValueError("O ficheiro está vazio!")
        
    print(f"Ficheiro encontrado: {caminho}")
    
    return str(caminho)
    
    