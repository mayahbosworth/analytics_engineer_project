-- SEE REGION PERFORMANCE
SELECT 
    region,
    SUM(total_revenue) AS total_revenue_generated
FROM sales_performance
GROUP BY region
ORDER BY SUM(total_revenue) DESC;
