from pathlib import Path

folder_name = Path('./test/test_2/Temp')

try:
    with open(folder_name / "jokes.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")

except Exception as e:
    print(f"{e} with file")