from pathlib import Path

# parent_folder_path = Path(r'D:\practice\goit_python_softwear\test\demo_1')
# parent_folder_path = Path(r'D:\practice\goit_python_softwear')
parent_folder_path = Path(r'D:\practice\goit_python_softwear\.venv')

def parse_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            print(f"Parse folder: This folder's name is - {element.name}")
            parse_folder(element)
        if element.is_file():
            print(f"Parse file: This file's name is - {element.name}")
        if element.name == "adapter.py":
            break

parse_folder(parent_folder_path)