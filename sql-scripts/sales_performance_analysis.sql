
-- Aggregated sales metrics by month, customer, and product -------------------
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

-- SEE TOP 5 SPENDING CUSTOMERS
SELECT 
    customer_name,
    SUM(total_revenue) AS total_revenue_generated
FROM sales_performance
GROUP BY customer_name, customer_id
ORDER BY SUM(total_revenue) DESC
LIMIT(5);

-- SEE REVENUE BY CUSTOMER SEGMENTS
SELECT 
    segment,
    SUM(total_revenue) AS total_revenue_generated
FROM sales_performance
GROUP BY segment
ORDER BY SUM(total_revenue) DESC;

-- SEE PRODUCT CATEGORY PERFORMANCE
SELECT
    category,
    SUM(total_revenue) AS total_revenue_generated
FROM sales_performance
GROUP BY category
ORDER BY SUM(total_revenue) DESC;

-- SEE REGION PERFORMANCE
SELECT 
    region,
    SUM(total_revenue) AS total_revenue_generated
FROM sales_performance
GROUP BY region
ORDER BY SUM(total_revenue) DESC;

-- SEE TOP 3 PERFORMING MONTHS
SELECT 
    order_month,
    SUM(total_revenue) AS total_revenue_generated
FROM sales_performance
GROUP BY order_month
ORDER BY SUM(total_revenue) DESC
LIMIT(3);

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

