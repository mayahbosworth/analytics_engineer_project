import chardet

def detect_encoding(file_path):
    try:
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read(1024))
            encoding = result['encoding']
            print(f"Detected encoding: {encoding}")
            return encoding if encoding else 'utf-8'
    except Exception as e:
        print("Failed to detect file encoding. Using default 'utf-8'.")
        print("Error:", e)
        return 'utf-8'
