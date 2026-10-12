from pathlib import Path

directory_name = Path("./test/test_6_mkdir/ABC")
complex_directory_name = Path("./test/test_6_mkdir/ABCD/Temp/check/exist")

# if not directory_name.exists():
#     directory_name.mkdir()

directory_name.mkdir(exist_ok=True)

complex_directory_name.mkdir(exist_ok=True, parents=True)