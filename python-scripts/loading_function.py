from find_path_function import get_file_path
from db_connection_function import create_engine_connection
from detect_encoding_function import detect_encoding
import pandas as pd


def load_csv_to_db(table_name, file_name, unique_column=None):
    try:
        engine = create_engine_connection()
        csv_path = get_file_path('csv', file_name) 
        print(f"loading data from {file_name} into {table_name}...", flush=True)
        
        encoding = detect_encoding(csv_path)
        df = pd.read_csv(csv_path, encoding=encoding)
        
        if unique_column:
            existing_ids = pd.read_sql_query(f"SELECT {unique_column} FROM {table_name}", engine)[unique_column].unique()
            df = df[~df[unique_column].isin(existing_ids)]
        
        if df.empty:
            print(f"no new data to insert into '{table_name}'... skipping", flush=True)
            return
        
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"data loaded into '{table_name}' successfully", flush=True)
    
    except FileNotFoundError as e:
        print(f"CSV file not found: {file_name}", flush=True)
        print("error:", e, flush=True)
    except Exception as e:
        print(f"failed to load data into '{table_name}'", flush=True)
        print("error:", e, flush=True)
    
    finally:
        if engine:
            engine.dispose()
            print("SQLAlchemy engine disposed", flush=True)
