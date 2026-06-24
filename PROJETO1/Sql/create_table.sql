CREATE TABLE transactions (
    transaction_id BIGINT,
    account_id BIGINT,
    transaction_date DATE,
    transaction_type VARCHAR(20),
    amount NUMERIC(12,2)
);