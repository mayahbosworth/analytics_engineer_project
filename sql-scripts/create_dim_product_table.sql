CREATE TABLE IF NOT EXISTS dim_product (
    product_id INT PRIMARY KEY,
    category VARCHAR(100)
);

INSERT INTO dim_product (product_id, category)
SELECT
    CAST(REGEXP_REPLACE(product_id::TEXT, '\.0$', '') AS INT) AS product_id,
    category
FROM raw_products
WHERE product_id IS NOT NULL
  AND CAST(product_id AS TEXT) ~ '^[0-9]+(\.0)?$'
ON CONFLICT (product_id) DO UPDATE 
SET 
    category = EXCLUDED.category;
