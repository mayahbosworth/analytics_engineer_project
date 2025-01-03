from db_connection_function import connect_to_db
from sqlalchemy import text


def create_dim_product_table():
    try:
        print("starting 'create_dim_product_table' function", flush=True)
        
        engine = connect_to_db()
        print("database connection established", flush=True)
        
        with engine.connect() as connection:
            print("starting to create 'dim_product' table", flush=True)
            
            # create the dim_product table
            create_table_query = text(r"""
                CREATE TABLE IF NOT EXISTS dim_product (
                    product_id INT PRIMARY KEY,
                    category VARCHAR(255)
                );
            """)
            connection.execute(create_table_query)
            print("Table 'dim_product' created successfully.", flush=True)
            
            # populate the dim_product table with duplicate prevention
            print("Starting to populate 'dim_product' table.", flush=True)
            
            populate_table_query = text(r"""
                INSERT INTO dim_product (product_id, category)
                SELECT
                    CAST(REGEXP_REPLACE(product_id::TEXT, '\.0$', '') AS INT) AS product_id,
                    category
                FROM raw_products
                WHERE product_id IS NOT NULL
                  AND CAST(product_id AS TEXT) ~ '^[0-9]+(\.0)?$'
                ON CONFLICT (product_id) DO UPDATE 
                SET 
                    category = EXCLUDED.category
            """)
            connection.execute(populate_table_query)
            print("data successfully inserted/updated in 'dim_product' table without duplicates", flush=True)
    
    except Exception as e:
        print("failed to create or populate 'dim_product' table", flush=True)
        print("error:", e, flush=True)
    
    finally:
        if engine:
            engine.dispose()
            print("🔌 SQLAlchemy engine disposed", flush=True)


