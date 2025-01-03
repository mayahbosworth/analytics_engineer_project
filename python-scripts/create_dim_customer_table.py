from db_connection_function import connect_to_db
from sqlalchemy import text


def create_dim_customer_table():
    try:
        print("starting 'create_dim_customer_table' function", flush=True)
        
        engine = connect_to_db()
        print("database connection established", flush=True)
        
        with engine.connect() as connection:
            print("starting to create 'dim_customer' table", flush=True)
            
            # create the dim_customer table
            create_table_query = text(r"""
                CREATE TABLE IF NOT EXISTS dim_customer (
                    customer_id INT PRIMARY KEY,
                    customer_name VARCHAR(255),
                    region VARCHAR(100),
                    segment VARCHAR(100)
                );
            """)
            connection.execute(create_table_query)
            print("table 'dim_customer' created successfully", flush=True)
            
            # populate the dim_customer table with duplicate prevention
            print("starting to populate 'dim_customer' table", flush=True)
            
            populate_table_query = text(r"""
                INSERT INTO dim_customer (customer_id, customer_name, region, segment)
                SELECT
                    CAST(REGEXP_REPLACE(customer_id::TEXT, '\.0$', '') AS INT) AS customer_id,
                    customer_name,
                    LOWER(region) AS region,
                    segment
                FROM raw_customers
                WHERE customer_id IS NOT NULL
                  AND CAST(customer_id AS TEXT) ~ '^[0-9]+(\.0)?$'
                ON CONFLICT (customer_id) DO UPDATE 
                SET 
                    customer_name = EXCLUDED.customer_name,
                    region = EXCLUDED.region,
                    segment = EXCLUDED.segment;
            """)
            connection.execute(populate_table_query)
            print("data successfully inserted/updated in 'dim_customer' table without duplicates", flush=True)
    
    except Exception as e:
        print("failed to create or populate 'dim_customer' table", flush=True)
        print("error:", e, flush=True)
    
    finally:
        if engine:
            engine.dispose()
            print("SQLAlchemy engine disposed", flush=True)


