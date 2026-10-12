from pathlib import Path

file_name = Path('jokes.txt')
# file_name = Path(r'D:\practice\goit_python_softwear\test\test_1\jokes.txt')

try:
    file = open(file_name, "r", encoding="utf-8")

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