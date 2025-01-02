from loading_function import load_csv_to_db

def create_raw_customers_table():
    
    try:
        load_csv_to_db(
            table_name='raw_customers',
            file_path='customers.csv',
            unique_column='customer_id',
            encoding='utf-8'
        )
    except Exception as e:
        print("Failed to populate 'raw_orders' table.")
        print("Error:", e)
