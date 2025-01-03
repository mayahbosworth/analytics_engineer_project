from run_sql_script import run_sql_script
from loading_function import load_csv_to_db


def run_etl():
    try:
        print("starting ETL pipeline...", flush=True)
        
        # step 1: load raw data
        print("\nstep 1: loading raw data...", flush=True)
        load_csv_to_db('raw_customers', 'customers.csv', unique_column='customer_id')
        load_csv_to_db('raw_orders', 'orders.csv', unique_column='order_id')
        load_csv_to_db('raw_products', 'products.csv', unique_column='product_id')
        print("raw data loaded successfully\n", flush=True)
        
        # step 2: create raw tables
        print("step 2: creating raw tables...", flush=True)
        run_sql_script('create_raw_customers_table.sql')
        run_sql_script('create_raw_orders_table.sql')
        run_sql_script('create_raw_products_table.sql')
        print("raw tables created successfully\n", flush=True)
        
        # step 3: create dimensional tables
        print("step 3: creating dimensional tables...", flush=True)
        run_sql_script('create_dim_customer_table.sql')
        run_sql_script('create_dim_product_table.sql')
        print("dimensional tables created successfully\n", flush=True)
        
        # step 4: create fact table
        print("step 4: creating fact table...", flush=True)
        run_sql_script('create_fact_sales_table.sql')
        print("fact table created successfully\n", flush=True)
        
        print("ETL pipeline completed successfully", flush=True)
    
    except Exception as e:
        print("\nETL pipeline failed", flush=True)
        print("error:", e, flush=True)
    
    finally:
        print("ETL pipeline finished", flush=True)
