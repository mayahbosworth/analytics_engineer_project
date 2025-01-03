
-- CHECK REVENUE TOTALS
SELECT 
    SUM(total_revenue)
FROM sales_performance;

SELECT 
    SUM(total_revenue)
FROM fact_sales;

SELECT 
    SUM(CAST(total_amount AS FLOAT))
FROM raw_orders;

