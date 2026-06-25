CREATE TABLE stg_transactions_proj2 (
    transaction_id BIGINT,
    account_id BIGINT,
    transaction_date DATE,
    transaction_type VARCHAR(20),
    amount NUMERIC(12,2)
);

CREATE TABLE transactions_proj2 (
    transaction_id BIGINT,
    account_id BIGINT,
    transaction_date DATE,
    transaction_type VARCHAR(20),
    amount NUMERIC(12,2)
);

CREATE TABLE p_control_proj2 (
    process_name VARCHAR(100),
    execution_date TIMESTAMP,
    rows_read INTEGER,
    rows_loaded INTEGER,
    status VARCHAR(20),
    error_message VARCHAR(500)
);