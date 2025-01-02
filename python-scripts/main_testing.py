from db_connection_function import connect_to_db

def main():
    connection = connect_to_db()
    if connection:
        print("Performing database tasks...")
        # Example: Run some SQL queries here
        connection.close()
        print("🔌 Connection closed successfully.")

if __name__ == '__main__':
    main()