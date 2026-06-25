from sqlalchemy import text
from src.load import get_engine

def insert_p_control_proj2(
        rows_read,
        rows_loaded,
        status,
        error_message=None
):
    engine = get_engine()

    query = text("""
                
                INSERT INTO P_CONTROL_PROJ2 
                (
                    process_name,
                    execution_date,
                    rows_read,
                    rows_loaded,
                    status,
                    error_message
                )
                VALUES
                (
                    'DAILY_ETL',
                    CURRENT_TIMESTAMP,
                    :rows_read,
                    :rows_loaded,
                    :status,
                    :error_message
                )
                """)
    
    with engine.begin() as conn:

        conn.execute(
            query,
            {
                "rows_read": rows_read,
                "rows_loaded": rows_loaded,
                "status": status,
                "error_message": error_message
            }
        )