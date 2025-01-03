CREATE TABLE IF NOT EXISTS fact_sales (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    customer_name VARCHAR(255),
    order_date DATE,
    total_amount NUMERIC(10, 2),
    total_revenue NUMERIC(10, 2)
);

WITH cleaned_orders AS (
    SELECT DISTINCT ON (order_id)
        CAST(REGEXP_REPLACE(order_id::TEXT, '\.0$', '') AS INT) AS order_id,
        CAST(REGEXP_REPLACE(customer_id::TEXT, '\.0$', '') AS INT) AS customer_id,
        CAST(REGEXP_REPLACE(product_id::TEXT, '\.0$', '') AS INT) AS product_id,
        CASE 
            WHEN order_date = '2024-02-30' THEN '2024-02-29'
            WHEN order_date = '2023-02-29' THEN '2023-02-28'
            ELSE order_date
        END::DATE AS order_date,
        CAST(total_amount AS NUMERIC(10, 2)) AS total_amount,
        CAST(total_amount AS NUMERIC(10, 2)) AS total_revenue
    FROM raw_orders
    WHERE customer_id IS NOT NULL
      AND product_id IS NOT NULL
    ORDER BY order_id, order_date
)
INSERT INTO fact_sales (order_id, customer_id, product_id, customer_name, order_date, total_amount, total_revenue)
SELECT
    cte.order_id,
    cte.customer_id,
    cte.product_id,
    dc.customer_name,
    cte.order_date,
    cte.total_amount,
    cte.total_revenue
FROM cleaned_orders cte
JOIN dim_customer dc ON cte.customer_id = dc.customer_id
JOIN dim_product dp ON cte.product_id = dp.product_id
ON CONFLICT (order_id) DO UPDATE 
SET 
    customer_id = EXCLUDED.customer_id,
    product_id = EXCLUDED.product_id,
    customer_name = EXCLUDED.customer_name,
    order_date = EXCLUDED.order_date,
    total_amount = EXCLUDED.total_amount,
    total_revenue = EXCLUDED.total_revenue;
