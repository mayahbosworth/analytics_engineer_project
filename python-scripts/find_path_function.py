import os

def get_csv_path(file_name):

    project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
    csv_path = os.path.join(project_root, 'csv', file_name)
    return csv_path