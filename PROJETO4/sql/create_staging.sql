CREATE TABLE IF NOT EXISTS staging_sales (
    sale_id INTEGER,
    sale_date DATE,
    customer_name VARCHAR(100),
    country VARCHAR(100),
    product_name VARCHAR(100),
    category VARCHAR(100),
    quantity INTEGER,
    unit_price NUMERIC(10, 2)
);