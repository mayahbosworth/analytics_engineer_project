from db_connection_function import create_engine_connection
from sqlalchemy import text
import os
import pandas as pd


def run_analysis_queries():
    try:
        engine = create_engine_connection()
        if engine is None:
            raise Exception("Failed to establish database connection.")
        
        # define the path to the analysis SQL scripts folder
        analysis_folder = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', 'sql-scripts', 'sales-metrics-analysis'
        ))
        
        if not os.path.exists(analysis_folder):
            raise FileNotFoundError(f"analysis folder not found: {analysis_folder}")
        
        # list all .sql files in the folder
        analysis_scripts = [
            os.path.join(analysis_folder, f) 
            for f in os.listdir(analysis_folder) 
            if f.endswith('.sql')
        ]
        
        if not analysis_scripts:
            print("no SQL analysis scripts found in the folder", flush=True)
            return
        
        print(f"found {len(analysis_scripts)} SQL analysis scripts...\n", flush=True)
        
        with engine.connect() as connection:
            for script_path in analysis_scripts:
                script_name = os.path.basename(script_path)
                print(f"executing analysis script: {script_name}", flush=True)
                
                with open(script_path, 'r') as sql_file:
                    query = sql_file.read().strip()
                    
                    if query:
                        result = connection.execute(text(query))
                        
                        if result.returns_rows:
                            df = pd.DataFrame(result.fetchall(), columns=result.keys())
                            print(df.to_string(index=False), flush=True)
                        else:
                            print("query executed successfully (no rows returned)", flush=True)
                    else:
                        print(f"script {script_name} is empty... skipping.", flush=True)
        
        print("\nall analysis queries executed successfully", flush=True)
    
    except FileNotFoundError as e:
        print(f"analysis folder or script not found: {e}", flush=True)
    except Exception as e:
        print("failed to execute analysis queries", flush=True)
        print("error:", e, flush=True)
    
    finally:
        if engine:
            engine.dispose()
            print("SQLAlchemy engine disposed", flush=True)
