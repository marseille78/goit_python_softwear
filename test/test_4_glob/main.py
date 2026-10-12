from pathlib import Path

file_name = Path("./test/test_4_glob/")

for elem in file_name.glob("*/"):
    print(elem)