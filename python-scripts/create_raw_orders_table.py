from loading_function import load_csv_to_db
from find_path_function import get_csv_path
from detect_encoding_function import detect_encoding

def create_raw_orders_table():
    try:
        # get the path to the CSV file
        csv_path = get_csv_path('orders.csv')
        
        # detect encoding dynamically
        detected_encoding = detect_encoding(csv_path)
        
        # load data into the database
        load_csv_to_db(
            table_name='raw_orders',
            file_path='orders.csv',
            unique_column='order_id',
            encoding=detected_encoding
        )
    
    except Exception as e:
        print("Failed to populate 'raw_orders' table.")
        print("Error:", e)
