from pathlib import Path

# Створення об'єкту Path для директорії
# directory = Path("./picture")
directory = Path(".")

# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)
