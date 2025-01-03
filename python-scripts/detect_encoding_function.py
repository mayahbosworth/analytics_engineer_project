import chardet

def detect_encoding(file_path):

    try:
        with open(file_path, 'rb') as file:
            result = chardet.detect(file.read())
            encoding = result['encoding']
            print(f"detected encoding: {encoding}", flush=True)
            return encoding
    except Exception as e:
        print("failed to detect file encoding", flush=True)
        print("error:", e, flush=True)
        return 'utf-8'
