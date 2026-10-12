import shutil
from pathlib import Path
from random import randint, choice, choices

base_path = "./test/test_10"

MESSAGE = "Hello, Привіт"

def get_random_filename():
    random_value = '()+,-0123456789;=@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz' \
                '{}~абвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'

    return "".join(choices(random_value, k=8))

# print(get_random_filename())
# print(get_random_filename())
# print(get_random_filename())

def generate_text_file(path):
    documents = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    with open(path / f"{get_random_filename()}.{choice(documents).lower()}", "wb") as f:
        f.write(MESSAGE.encode())

# parent_folder_path = Path(f"{base_path}/Temp")
# generate_text_file(parent_folder_path)
# generate_text_file(parent_folder_path)

def generate_archive_file(path):
    archive = ('ZIP', 'GZTAR', 'TAR')
    shutil.make_archive(f"{path}/{get_random_filename()}", f"{choice(archive).lower()}", path)

def generate_folders(path):
    folder_name = ['temp', 'folder', 'dir', 'tmp', 'OMG', 'is_it_true', 'no_way', 'find_it']
    folder_path = Path(
        f"{path}" + "/".join(choices(folder_name, weights=[10, 10, 1, 1, 1, 1, 1, 1], k=randint(5, len(folder_name))))
    )
    folder_path.mkdir(parents=True, exist_ok=True)

def generate_folder_forest(path):
    for _ in range(0, randint(2, 5)):
        generate_folders(path)

def generate_random_files(path):
    for _ in range(3, randint(5, 7)):
        function_list = [generate_text_file, generate_archive_file]
        choice(function_list)(path)

def parse_folder_recursion(path):
    for element in path.iterdir():
        if element.is_dir():
            generate_random_files(path)
            parse_folder_recursion(element)

def exist_parent_folder(path):
    path.mkdir(exist_ok=True, parents=True)

def file_generator(path):
    exist_parent_folder(path)
    generate_folder_forest(path)
    parse_folder_recursion(path)

if __name__ == "__main__":
    parent_folder_path = Path(f"{base_path}/Temp/")
    # generate_folders(parent_folder_path)
    # generate_folder_forest(parent_folder_path)
    # generate_random_files(parent_folder_path)
    parse_folder_recursion(parent_folder_path)