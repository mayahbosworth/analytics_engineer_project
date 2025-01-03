from db_connection_function import connect_to_db
from sqlalchemy import text


def create_fact_sales_table():
    """
    Create and populate the 'fact_sales' table from 'raw_orders', avoiding duplicate order_id entries.
    """
    try:
        engine = connect_to_db()
        print("Database connection established.", flush=True)
        
        with engine.connect() as connection:
            print("Starting to create 'fact_sales' table.", flush=True)
            
            # Create the fact_sales table
            create_table_query = text(r"""
                CREATE TABLE IF NOT EXISTS fact_sales (
                    order_id INT PRIMARY KEY,
                    customer_id INT,
                    product_id INT,
                    customer_name VARCHAR(255),
                    order_date DATE,
                    total_amount NUMERIC(10, 2),
                    total_revenue NUMERIC(10, 2)
                );
            """)
            connection.execute(create_table_query)
            print("Table 'fact_sales' created successfully.", flush=True)
            
            # Populate the fact_sales table with duplicate prevention
            print("Starting to populate 'fact_sales' table.", flush=True)
            
            populate_table_query = text(r"""
                WITH cleaned_orders AS (
                    SELECT DISTINCT ON (order_id)
                        CAST(REGEXP_REPLACE(order_id::TEXT, '\.0$', '') AS INT) AS order_id,
                        CAST(REGEXP_REPLACE(customer_id::TEXT, '\.0$', '') AS INT) AS customer_id,
                        CAST(REGEXP_REPLACE(product_id::TEXT, '\.0$', '') AS INT) AS product_id,
                        CASE 
                            WHEN order_date = '2024-02-30' THEN '2024-02-29'
                            WHEN order_date = '2023-02-29' THEN '2023-02-28'
                            ELSE order_date
                        END::DATE AS order_date,
                        CAST(total_amount AS NUMERIC(10, 2)) AS total_amount,
                        CAST(total_amount AS NUMERIC(10, 2)) AS total_revenue
                    FROM raw_orders
                    WHERE customer_id IS NOT NULL
                      AND product_id IS NOT NULL
                    ORDER BY order_id, order_date
                )
                INSERT INTO fact_sales (order_id, customer_id, product_id, customer_name, order_date, total_amount, total_revenue)
                SELECT
                    cte.order_id,
                    cte.customer_id,
                    cte.product_id,
                    dc.customer_name,
                    cte.order_date,
                    cte.total_amount,
                    cte.total_revenue
                FROM cleaned_orders cte
                JOIN dim_customer dc ON cte.customer_id = dc.customer_id
                WHERE cte.customer_id IN (SELECT customer_id FROM dim_customer)
                  AND cte.product_id IN (SELECT product_id FROM dim_product)
                ON CONFLICT (order_id) DO UPDATE 
                SET 
                    customer_id = EXCLUDED.customer_id,
                    product_id = EXCLUDED.product_id,
                    customer_name = EXCLUDED.customer_name,
                    order_date = EXCLUDED.order_date,
                    total_amount = EXCLUDED.total_amount,
                    total_revenue = EXCLUDED.total_revenue;
            """)
            connection.execute(populate_table_query)
            print("Data successfully inserted/updated in 'fact_sales' table without duplicates.", flush=True)
    
    except Exception as e:
        print("Failed to create or populate 'fact_sales' table.", flush=True)
        print("Error:", e, flush=True)
    
    finally:
        if engine:
            engine.dispose()
            print("SQLAlchemy engine disposed.", flush=True)
