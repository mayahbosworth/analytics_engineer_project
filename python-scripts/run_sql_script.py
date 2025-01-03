from db_connection_function import create_engine_connection
from sqlalchemy import text
import os


def run_sql_script(file_name):
    
    try:
        engine = create_engine_connection()
        sql_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sql-scripts', file_name))
        
        if not os.path.exists(sql_path):
            raise FileNotFoundError(f"SQL script not found: {sql_path}")
        
        print(f"executing SQL script: {sql_path}", flush=True)
        
        with engine.connect() as connection:
            with open(sql_path, 'r') as sql_file:
                sql_script = sql_file.read()
                connection.execute(text(sql_script))
                print(f"successfully executed SQL script: {sql_path}", flush=True)
    
    except FileNotFoundError as e:
        print("SQL script file not found", flush=True)
        print("error:", e, flush=True)
    except Exception as e:
        print("failed to execute SQL script", flush=True)
        print("error:", e, flush=True)
    
    finally:
        if engine:
            engine.dispose()
            print("SQLAlchemy engine disposed", flush=True)
