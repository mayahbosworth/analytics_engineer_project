import os

def get_file_path(directory, file_name):
    try:
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        file_path = os.path.join(project_root, directory, file_name)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"file not found: {file_path}")
        
        return file_path
    except Exception as e:
        print("failed to resolve file path", flush=True)
        print("error:", e, flush=True)
        return None

