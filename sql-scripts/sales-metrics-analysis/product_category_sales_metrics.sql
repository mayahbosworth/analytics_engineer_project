-- SEE PRODUCT CATEGORY PERFORMANCE
SELECT
    category,
    SUM(total_revenue) AS total_revenue_generated
FROM sales_performance
GROUP BY category
ORDER BY SUM(total_revenue) DESC;