import os

def get_csv_path(file_name):
    """
    Dynamically generates the absolute path to a CSV file in the 'csv' directory.

    Args:
        file_name (str): The name of the CSV file (e.g., 'orders/orders.csv').

    Returns:
        str: The absolute path to the CSV file.
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    csv_path = os.path.join(project_root, 'csv', file_name)
    return csv_path