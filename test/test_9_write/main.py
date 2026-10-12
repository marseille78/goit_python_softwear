from pathlib import Path

base = "./test/test_9_write"

file_path = Path(f"{base}/Temp/test_data.txt")

data = ["First line", "Second line", "Third line", "Fourth line"]

with open(file_path, "w", encoding="utf-8") as file:

    # for line in data:
    #     file.write(f"{line}\n")

    file.write("\n".join(data))


with open(file_path, "a") as file:
    file.writelines(["First line\n", "Second line\n", "Third line\n", "Fourth line\n"])