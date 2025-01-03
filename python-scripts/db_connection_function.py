from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()

def create_engine_connection():
    try:
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        dbname = os.getenv('DB_NAME')
        
        engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")
        print("database connection established", flush=True)
        return engine
    
    except Exception as e:
        print("failed to create database engine", flush=True)
        print("error:", e, flush=True)
        return None

