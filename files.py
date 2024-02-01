import base64

def upload_file(self, file_path):
    with open(file_path, "rb") as file:
        file_content = base64.b64encode(file.read()).decode('utf-8')