from pathlib import Path

src_name = Path("./test/test_7_rename/test.py")
dst_name = Path("./test/test_7_rename/ABC/test.py")

src_name.rename(dst_name)