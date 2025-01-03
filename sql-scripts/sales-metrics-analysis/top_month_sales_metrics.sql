-- SEE TOP 3 PERFORMING MONTHS
SELECT 
    order_month,
    SUM(total_revenue) AS total_revenue_generated
FROM sales_performance
GROUP BY order_month
ORDER BY SUM(total_revenue) DESC
LIMIT(3);