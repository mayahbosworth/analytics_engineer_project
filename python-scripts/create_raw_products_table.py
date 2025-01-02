from loading_function import load_csv_to_db
from find_path_function import get_csv_path
from detect_encoding_function import detect_encoding

def create_raw_products_table():
    try:
        # get the path to the CSV file
        csv_path = get_csv_path('products.csv')
        
        # detect encoding dynamically
        detected_encoding = detect_encoding(csv_path)
        
        # load data into the database
        load_csv_to_db(
            table_name='raw_products',
            file_path='products.csv',
            unique_column='product_id',
            encoding=detected_encoding
        )
    
    except Exception as e:
        print("Failed to populate 'raw_products' table.")
        print("Error:", e)