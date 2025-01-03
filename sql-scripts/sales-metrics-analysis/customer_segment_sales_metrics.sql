-- SEE REVENUE BY CUSTOMER SEGMENTS
SELECT 
    segment,
    SUM(total_revenue) AS total_revenue_generated
FROM sales_performance
GROUP BY segment
ORDER BY SUM(total_revenue) DESC;