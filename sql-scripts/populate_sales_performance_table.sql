INSERT INTO sales_performance (order_id, customer_name, customer_id, region, segment, 
            product_id, category, order_month, total_revenue)
SELECT 
    f.order_id,
    f.customer_name,
    f.customer_id,
    c.region,    
    c.segment,
    f.product_id,
    p.category,
    EXTRACT(MONTH FROM f.order_date) AS order_month,
    f.total_revenue
FROM fact_sales f
LEFT JOIN dim_customer c ON f.customer_id = c.customer_id
LEFT JOIN dim_product p ON f.product_id = p.product_id
ON CONFLICT (order_id) DO UPDATE
SET 
    customer_name = EXCLUDED.customer_name,
    customer_id = EXCLUDED.customer_id,
    region = EXCLUDED.region,
    segment = EXCLUDED.segment,
    product_id = EXCLUDED.product_id,
    category = EXCLUDED.category,
    order_month = EXCLUDED.order_month,
    total_revenue = EXCLUDED.total_revenue;
