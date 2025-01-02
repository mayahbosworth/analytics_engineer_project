import os
import psycopg2
from dotenv import load_dotenv

def connect_to_db():
    try:
        # environment variables
        host = os.getenv('DB_HOST')
        dbname = os.getenv('DB_NAME')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        port = os.getenv('DB_PORT')
        
        # establish connection
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        print("✅ Database connection successful!")
        # database connection object
        return conn
    
    except Exception as e:
        print("❌ Failed to connect to the database.")
        print("Error:", e)
        return None