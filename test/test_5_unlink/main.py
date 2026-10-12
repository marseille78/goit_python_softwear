from pathlib import Path

file_name = Path("./test/test_5_unlink/test.txt")

# try:
#     file_name.unlink()
# except:
#     pass

# try:
#     file_name.unlink()
# except FileNotFoundError:
#     pass

file_name.unlink(missing_ok=True)