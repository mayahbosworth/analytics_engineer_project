-- CALCULATE MONTHLY REVENUE
SELECT
    order_month,
    SUM(total_revenue) AS monthly_revenue
FROM
    sales_performance
GROUP BY
    order_month
ORDER BY
    order_month;