from pathlib import Path

folder_name = Path('./test/test_2/Temp')
# file_name = Path(r'D:\practice\goit_python_softwear\test\test_1\jokes.txt')

for el in folder_name.iterdir():
    print(el.name)

try:
    file = open(folder_name / "jokes.txt", "r", encoding="utf-8")

    try:
        while True:
            line = file.readline()

            if not line:
                break

            print(line, end="")
    except OSError:
        print("Error while reading file.")
    finally:
        file.close()
except OSError:
    print("OSError")