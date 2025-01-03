from find_path_function import get_csv_path
from db_connection_function import connect_to_db
import pandas as pd


def load_csv_to_db(table_name, file_path, unique_column=None, encoding='utf-8'):
    try:
        engine = connect_to_db()
        
        csv_path = get_csv_path(file_path)
        
        try:
            df = pd.read_csv(csv_path, encoding=encoding)
        except UnicodeDecodeError:
            print(f"encoding error while reading {file_path}... trying 'utf-16le' instead")
            df = pd.read_csv(csv_path, encoding='utf-16le')
        
        print(f"data from {file_path} loaded successfully into a temporary dataframe")
        
        if unique_column:
            existing_ids = pd.read_sql_query(f"SELECT {unique_column} FROM {table_name}", engine)[unique_column].unique()
            original_length = len(df)
            df = df[~df[unique_column].isin(existing_ids)]
            new_length = len(df)
            
            print(f"rows before deduplication: {original_length}")
            print(f"rows after deduplication: {new_length}")
        
        if df.empty:
            print(f"no new data to insert into table '{table_name}'... skipping database insertion")
            return
        
        # insert data into the table
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"data successfully inserted into table '{table_name}'.")
    
    except Exception as e:
        print("failed to load data from CSV to the database")
        print("error:", e)
    
    finally:
        if engine:
            engine.dispose()
            print("SQLAlchemy engine disposed")

