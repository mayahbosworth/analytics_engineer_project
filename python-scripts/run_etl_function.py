from create_raw_orders_table import create_raw_orders_table
from create_raw_customers_table import create_raw_customers_table
from create_raw_products_table import create_raw_products_table

from create_dim_customer_table import create_dim_customer_table
from create_dim_product_table import create_dim_product_table

from create_fact_sales_table import create_fact_sales_table


def run_etl():
    try:
        print("starting ETL pipeline...", flush=True)
        
        # step 1: load raw tables
        print("\nstep 1: loading raw tables...", flush=True)
        create_raw_customers_table()
        create_raw_orders_table()
        create_raw_products_table()
        print("raw tables loaded successfully", flush=True)
        
        # step 2: create dimensional tables
        print("\nstep 2: creating dimensional tables...", flush=True)
        create_dim_customer_table()
        create_dim_product_table()
        print("dimensional tables created successfully", flush=True)
        
        # step 3: create fact table
        print("\nstep 3: creating fact table...", flush=True)
        create_fact_sales_table()
        print("fact table created successfully", flush=True)
        
        print("\nETL pipeline completed successfully!", flush=True)
    
    except Exception as e:
        print("\nETL pipeline failed!", flush=True)
        print("error:", e, flush=True)
    
    finally:
        print("ETL pipeline finished", flush=True)

