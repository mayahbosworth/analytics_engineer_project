CREATE TABLE IF NOT EXISTS sales_performance (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    customer_id INT NOT NULL,
    region VARCHAR(100),
    segment VARCHAR(100),
    product_id INT NOT NULL,
    category VARCHAR(100),
    order_month INT NOT NULL,
    total_revenue NUMERIC(10, 2)
);