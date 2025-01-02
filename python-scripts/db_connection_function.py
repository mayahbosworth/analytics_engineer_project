from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def connect_to_db():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    dbname = os.getenv('DB_NAME')
    
    return create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

