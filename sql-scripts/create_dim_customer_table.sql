

CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    region VARCHAR(100),
    segment VARCHAR(100)
);

INSERT INTO dim_customer (customer_id, customer_name, region, segment)
SELECT
    CAST(REGEXP_REPLACE(customer_id::TEXT, '\.0$', '') AS INT) AS customer_id,
    customer_name,
    LOWER(region) AS region,
    segment
FROM raw_customers
WHERE customer_id IS NOT NULL
  AND CAST(customer_id AS TEXT) ~ '^[0-9]+(\.0)?$'
ON CONFLICT (customer_id) DO UPDATE 
SET 
    customer_name = EXCLUDED.customer_name,
    region = EXCLUDED.region,
    segment = EXCLUDED.segment;
