-- SEE TOP 5 SPENDING CUSTOMERS
SELECT 
    customer_name,
    SUM(total_revenue) AS total_revenue_generated
FROM sales_performance
GROUP BY customer_name, customer_id
ORDER BY SUM(total_revenue) DESC
LIMIT(5);